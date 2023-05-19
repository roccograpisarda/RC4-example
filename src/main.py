import streamlit as st
from RC4 import *

# Streamlit app
def main():
    st.title("RC4 Encryption/Decryption")

    # Get mode (encryption or decryption) from the user
    mode = st.radio("Select mode:", ("Encryption", "Decryption"))

    # Get input (plaintext or ciphertext) from the user
    input_text = st.text_area("Enter the input:", "")

    # Get key from the user
    key = st.text_input("Enter the key:", "")

    # Perform encryption or decryption based on the selected mode
    if st.button(mode):
        if input_text and key:
            key = key.encode()  # Convert key to bytes

            if mode == "Encryption":
                plaintext = input_text.encode()  # Convert plaintext to bytes
                output_text, keystream = RC4(key, plaintext)
            else:  # Decryption
                ciphertext = input_text.encode("latin-1")  # Use latin-1 encoding to preserve byte values
                output_text, keystream = RC4(key, ciphertext)

            st.success(mode + " Text: " + output_text)
            st.info("Key Length (bytes): " + str(len(key)))
            st.info("Keystream (bytes): " + keystream.hex())
        else:
            st.warning("Please enter both input and key.")

if __name__ == "__main__":
    main()