import os
from Crewkickoff import run_ai_workflow
from IPython.display import Markdown, display
from fpdf import FPDF
from google.colab import files
from dotenv import load_dotenv

# Load the .env variables
load_dotenv()

# Get credentials from .env
USERNAME = os.getenv("MY_USERNAME")
PASSWORD = os.getenv("MY_PASSWORD")
#----------------------------------------




# Sample input for an AI-related topic

ai_topic_inputs = {
    "topic": "Latest advancements in AI and deep learning technologies"
}

final_report = run_ai_workflow(ai_topic_inputs) # run ai work -> from Crewkickoff.py
print(final_report)

# ----------------------------------------------------------------------------------------

# Download markdown and PDF files

markdown_filename = "AI_Sustainability_Report.md"
with open(markdown_filename, 'w') as f:
    f.write(final_report)

display(Markdown(f'./{markdown_filename}'))

def save_to_pdf(text: str, filename: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.multi_cell(0, 10, line)
    pdf.output(filename)

pdf_filename = "AI_Sustainability_Report.pdf"
save_to_pdf(final_report, pdf_filename)

files.download(markdown_filename)
files.download(pdf_filename)