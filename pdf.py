import pypdf

with open("dummy.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    #print(reader.get_num_pages())
    print(reader.get_page(0)) #devuelve un page object
    
    #para rotar una página:
    page = reader.get_page(0)
    page.rotate(90)
    
    #para guardar el nuevo pdf y escribir en este:
    writer = pypdf.PdfWriter()
    writer.add_page(page)
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)