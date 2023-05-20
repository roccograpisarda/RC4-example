# RC4-example
This Python project is an educational streamlit application that simulates the RC4 algorithm encryption.
The RC4 algorithm is a widely used symmetric stream cipher that efficiently encrypts and decrypts data.

## Features 
- Encryption and Decryption: The simulator allows users to input their text or message and encrypt it using the RC4 algorithm. It also provides a decryption option to retrieve the original message from the encrypted data.
- Encryption Strength Analysis: The application provides insights into the strength of the encryption by displaying the key length.


## Project Structure
   ```bash
.
├── LICENSE
├── README.md
└── src
    ├── main.py
    └── RC4.py
```

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/your-username/rc4-encryption-simulator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd rc4-encryption-simulator
    ```
3. Install the required dependency:
    ```bash
    pip install streamlit
    ```

## Usage
Run the streamlit application:
```bash
streamlit run app.py
``` 
   
Open your web browser and navigate to http://localhost:8501 to access the RC4 encryption simulator.

Follow the instructions on the web interface to encrypt or decrypt your messages using the RC4 algorithm.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request to the GitHub repository.

## License
This project is licensed under the GPL-3.0 License. You can find more information in the [LICENSE](LICENSE) file.


## Credits

This project was developed by Rocco Rapisarda. Special thanks to Streamlit for providing the interactive web framework for the application.

## Acknowledgments
The RC4 algorithm was originally developed by Ron Rivest.
