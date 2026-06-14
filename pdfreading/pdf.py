import pypdf

with open('/Users/mothilaljadhav/Desktop/Projects/Python/pdfreading/pdfs/sem 8 fees.pdf', 'rb') as file:
    reader = pypdf.PdfReader(file)
    page = reader.pages[0]

    page.rotate(90)

    writer = pypdf.PdfWriter()
    writer.add_page(page)

    with open('/Users/mothilaljadhav/Desktop/Projects/Python/pdfreading/pdfs/rotated.pdf', 'wb') as new_file:
        writer.write(new_file)