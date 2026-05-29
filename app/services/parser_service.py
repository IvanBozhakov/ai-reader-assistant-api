from pypdf import PdfReader
from docx import Document
from io import BytesIO

async def extract_text(file):
    content = await file.read()

    if file.filename.endswith(".pdf"):
        return extract_pdf(content)

    elif file.filename.endswith(".docx"):
        return extract_docx(content)

    raise ValueError("Unsupported file type")


def extract_pdf(content):
    reader = PdfReader(BytesIO(content))

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text


def extract_docx(content):
    doc = Document(BytesIO(content))

    return "\n".join(
        paragraph.text for paragraph in doc.paragraphs
    )