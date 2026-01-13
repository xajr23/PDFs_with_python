import pypdf
import sys

inputs = sys.argv[1:]

writer = pypdf.PdfWriter()

for pdf in inputs:
    print(f"Adding: {pdf}")
    reader = pypdf.PdfReader(pdf)
    for page in reader.pages:
        writer.add_page(page)

with open("super.pdf", "wb") as output:
    writer.write(output)