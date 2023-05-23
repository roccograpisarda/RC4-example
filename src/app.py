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
    key = st.text_input("Enter the key:", "", max_chars = 256)
    

    # Perform encryption or decryption based on the selected mode
    if st.button(mode):
        if input_text and key:
             # Convert key to bytes
            key = key.encode() 
            S = KSA(key)
            keystream = PRGA(S)

           # Encryption
            if mode == "Encryption":
                # Convert plaintext to bytes
                plaintext = input_text.encode()  
                output_text = RC4(plaintext, keystream)
            # Decryption
            else:  
                # Use latin-1 encoding to preserve byte values
                ciphertext = input_text.encode("latin-1")
                output_text = RC4(ciphertext, keystream)

            st.success(mode + " Text: " + output_text)
            st.info("Key Length (bytes): " + str(len(key)))

            
            # Convert keystream bytes to a readable format
            keystream_hex = ''.join(format(b, '02x') for b in  [next(keystream) for _ in range(len(input_text))])
            # Display the keystream
            st.info("Keystream (hex): " + keystream_hex)
        else:
            st.warning("Please enter both input and key.")

if __name__ == "__main__":
    main()