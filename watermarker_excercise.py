from pypdf import PdfReader, PdfWriter
import sys

watermark_pdf = sys.argv[1]
inputs = sys.argv[2:]

watermark_reader = PdfReader(watermark_pdf)
watermark_page = watermark_reader.pages[0]

writer = PdfWriter()

for pdf in inputs:
    reader = PdfReader(pdf)
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

with open("watermarked.pdf", "wb") as output:
    writer.write(output)