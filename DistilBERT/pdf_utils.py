import PyPDF2
from io import BytesIO

def extract_text_from_pdf(uploaded_file):
    # Convert the uploaded file to a file-like object using BytesIO
    pdf_file = BytesIO(uploaded_file.read())

    # Now use PyPDF2 to read the PDF from the byte stream
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""

    # Iterate through the pages of the PDF and extract text
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()

    return text