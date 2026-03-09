from pdf2docx import Converter
from docx2pdf import convert
from pdf2image import convert_from_path
from PIL import Image
import pypandoc

def pdf_to_word(pdf_file, docx_file):
    cv = Converter(pdf_file)
    cv.convert(docx_file)
    cv.close()

def word_to_pdf(docx_file, pdf_file):
    convert(docx_file, pdf_file)

def pdf_to_image(pdf_file, output_prefix):
    images = convert_from_path(pdf_file)
    paths = []
    for i, img in enumerate(images):
        path = f"{output_prefix}_{i}.png"
        img.save(path, "PNG")
        paths.append(path)
    return paths

def image_to_pdf(image_file, pdf_file):
    image = Image.open(image_file)
    image.convert("RGB").save(pdf_file)

def md_to_word(md_file, docx_file):
    pypandoc.convert_file(md_file, "docx", outputfile=docx_file)

def md_to_pdf(md_file, pdf_file):
    pypandoc.convert_file(md_file, "pdf", outputfile=pdf_file)