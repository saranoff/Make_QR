import streamlit as st
import qrcode
from io import BytesIO

# qr code generation function
def generate_qr_code(data):
    qr = qrcode.QRCode(version=3, box_size=8, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill = 'black', back_color = 'white' )

    buffer = BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

st.title("Make your Own QR")

inp = st.text_input("Enter text or URL:")

if st.button("Make"):
    if inp:
        qr_image = generate_qr_code(inp)
        st.image(qr_image, caption="Congratulations You Made your own QR")
        st.download_button(label="Download", data=qr_image, file_name="qrcode.png", mime="image/png")
    else:
        st.warning("Please Enter the input text")