from PyPDF2 import PdfReader
from docx import Document

def extract_text(path):
    text = ""
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        for page in reader.pages:
            text += page.extract_text() or ""
    else:
        doc = Document(path)
        for p in doc.paragraphs:
            text += p.text + "\n"
    return text
