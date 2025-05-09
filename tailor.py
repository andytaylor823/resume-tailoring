import os
import shutil
import subprocess
import json
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

NAME = 'Andy Taylor' # other users -- edit this line

# === 1. Read job description ===
print('Reading job desc and technical expertise...')
with open("job_desc.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# === 2. Read technical experience section ===
with open("technical_sections_TeX_text.txt", "r", encoding="utf-8") as f:
    technical_section = f.read()

# === 3. Create prompt ===
with open('prompt.txt', 'r') as f:
    prompt = f.read()

prompt = prompt.format(
    job_description=job_description,
    technical_section=technical_section
)

# === 4. Query Azure OpenAI ===
print('Prompting LLM...')
endpoint = os.environ["ENDPOINT_URL"]
subscription_key = os.environ["AZURE_OPENAI_API_KEY"]
deployment = "gpt-4o"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

messages = [{"role": "user", "content": prompt}]
response = client.chat.completions.create(
    model=deployment,
    messages=messages,
    stream=False
)

new_technical_section = json.loads(response.to_json())['choices'][0]['message']['content']

end_doc = "\\end{document}"
if end_doc not in new_technical_section:
    new_technical_section += '\n' + end_doc

# === 5. Read full resume ===
print('Updating resume...')
with open("main.tex", "r", encoding="utf-8") as f:
    full_resume = f.read()

# === 6. Prompt for company name ===
company = input("Enter the company name: ").strip().replace(" ", "_")

# === 7. Create new folder ===
print('Reading job desc...')
os.makedirs(company, exist_ok=True)

# === 8. Replace technical experience section ===
start_marker = "\\begin{rSection}{Employment}"
start_index = full_resume.find(start_marker)
if start_index == -1:
    raise ValueError("Start marker not found in main.tex")

new_resume = full_resume[:start_index] + new_technical_section

# === 9. Write new resume.tex ===
print('Writing new resume...')
new_tex_path = os.path.join(company, "resume.tex")
with open(new_tex_path, "w", encoding="utf-8") as f:
    f.write(new_resume)

# === 10. Copy job description and resume.cls into new folder ===
shutil.copy("resume.cls", os.path.join(company, "resume.cls"))
shutil.copy("job_desc.txt", os.path.join(company, "job_desc.txt"))

# === 11. Call pdflatex ===
print('Calling "pdflatex"...')
subprocess.run(
    ["pdflatex", "-interaction=nonstopmode", "resume.tex"],
    cwd=company,
    check=True,
    stdout=open("log.txt", "w") # pipe 
)

# === 12. Rename PDF ===
old_pdf_path = os.path.join(company, "resume.pdf")
new_pdf_path = os.path.join(company, f"{NAME.replace(' ', '')}_Resume.pdf")
if os.path.exists(new_pdf_path):
    print('Output file already exists -- overwriting')
    os.remove(new_pdf_path)
if os.path.exists(old_pdf_path):
    os.rename(old_pdf_path, new_pdf_path)
else:
    print("PDF not found. Check LaTeX compilation logs.")

print(f"Customized resume generated at: {new_pdf_path}")
