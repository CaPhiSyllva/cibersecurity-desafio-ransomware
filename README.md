### `README.md`

# Educational File Encryption and Decryption Project

This project demonstrates file encryption and decryption using the `pyaes` module in Python. **Note: This project was developed exclusively for educational purposes. Hacking practices are illegal and unethical when conducted outside of a controlled environment and without proper consent.**

## Project Structure

- `encrypter.py`: Script to encrypt a file.
- `decrypter.py`: Script to decrypt an encrypted file.
- `README.md`: This documentation file.

## Requirements

- Python 3.6 or higher
- `pyaes` module

## Installation

1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Install the `pyaes` module using pip:

```sh
pip install pyaes
```

## Usage

### Encryption

1. Make sure you have a file named `test.txt` or change the file name in the `encrypter.py` script.
2. Run the encryption script:

```sh
python encrypter.py
```

3. The `test.txt` file will be encrypted, and a new file named `test.txt.ransomwaretroll` will be created.

### Decryption

1. Ensure that the `test.txt.ransomwaretroll` file is present in the directory.
2. Run the decryption script:

```sh
python decrypter.py
```

3. The `test.txt.ransomwaretroll` file will be decrypted, and a new file named `test.txt` will be created.

## Important Note

This project was created exclusively for educational and awareness purposes. The creation, use, and distribution of ransomware or any other type of malware is illegal and unethical. Use the knowledge gained to improve system security and protect data. Always obtain permission before testing or executing any security techniques on systems that are not your property.
