# 🎯 Resume Tailoring Automation with Azure OpenAI & LaTeX

This Python project automates the process of customizing your LaTeX resume for different job applications using an LLM (Azure OpenAI). It extracts your technical experience section, rewrites it to better match a given job description, and compiles a personalized PDF resume.

---

## 🛠 Features

- 🔍 Reads job descriptions and your technical resume section from text files.
- 🤖 Uses Azure OpenAI (`gpt-4o`) to tailor your resume to match the job description.
- 📝 Replaces the technical experience section in your LaTeX resume.
- 📂 Creates a company-specific output folder with the customized `.tex` and PDF files.
- 📄 Copies the required LaTeX class file.
- 📎 Compiles the resume using `pdflatex`.
- 🧾 Outputs a company-specific PDF: `AndyTaylor_Resume.pdf`.

---

## 📁 File Structure

```bash
.
├── main.tex                           # Your full resume (LaTeX)
├── technical_sections_TeX_text.txt    # Your technical experience section only
├── job_desc.txt                       # The job description text
├── resume.cls                         # LaTeX resume class file
├── tailor.py                          # The main Python script
├── requirements.txt                   # Requirements to run tailoring script
├── prompt.txt                         # Prompt template for LLM
├── README.md                          # This file
└── <CompanyName>/                     # Auto-created per company, contains tailored resume
```

## 🚀 Getting Started
### 1. Install Dependencies
Clone the project, create a new python `venv`, and install dependencies:

```bash
git clone https://github.com/andytaylor823/resume-tailoring.git
cd resume-tailoring
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Ensure pdflatex is installed and available in your system PATH (MiKTeX on Windows).

### 2. Set Environment Variables
You can export them in your terminal or use a .env manager:

```bash
export ENDPOINT_URL="https://<your-endpoint>.openai.azure.com/"
export AZURE_OPENAI_API_KEY="your_api_key"
```

### 3. Run the Script
```bash
python tailor.py
```
You'll be prompted for the company name. The script will:

- Tailor your technical section
- Insert it into your resume
- Compile the LaTeX
- Generate AndyTaylor_Resume.pdf in a new <CompanyName> folder

## ✍️ Author
*Andy Taylor*
This script is tailored for Andy Taylor's resume management workflow. For users with other names, 
edit line 9 in `tailor.py`:
```python
NAME = "<your name here>"
```

## 📄 License
This project is licensed under the MIT License.
