import os
from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_file(file_path):
    """
    Extract text from PDF or DOCX resume files.
    """
    if not os.path.exists(file_path):
        return ""

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)

    return ""


def extract_text_from_pdf(file_path):
    text = ""
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception:
        pass
    return text


def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception:
        pass
    return text
