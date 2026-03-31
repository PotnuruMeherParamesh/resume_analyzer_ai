from pypdf import PdfReader

def extractpdf(pdf_doc):  # module to load and extract the text from the PDF
    try:
        pdf = PdfReader(pdf_doc) # load the pdf document
        raw_text = ''
        for index,page in enumerate(pdf.pages):    # by index, pages from the loaded document
            text = page.extract_text()  #  from page it will extract the text 
            if text:
                raw_text += text
        return raw_text
    except Exception as e:
        return f'Error in reading the pdf'