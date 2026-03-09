import streamlit as st
import converter
import tempfile
import os

st.title("Universal File Converter")

conversion = st.selectbox(
    "Choose Conversion Type",
    [
        "PDF to Word",
        "Word to PDF",
        "PDF to Image",
        "Image to PDF",
        "MD to Word",
        "MD to PDF"
    ]
)

uploaded = st.file_uploader("Upload file")

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded.read())
        input_path = tmp.name

    if st.button("Convert"):

        output_path = input_path + "_output"

        if conversion == "PDF to Word":
            output = output_path + ".docx"
            converter.pdf_to_word(input_path, output)

        elif conversion == "Word to PDF":
            output = output_path + ".pdf"
            converter.word_to_pdf(input_path, output)

        elif conversion == "Image to PDF":
            output = output_path + ".pdf"
            converter.image_to_pdf(input_path, output)

        elif conversion == "MD to Word":
            output = output_path + ".docx"
            converter.md_to_word(input_path, output)

        elif conversion == "MD to PDF":
            output = output_path + ".pdf"
            converter.md_to_pdf(input_path, output)

        st.success("Conversion done!")

        with open(output, "rb") as f:
            st.download_button("Download", f, file_name=os.path.basename(output))