"""
Decrypt Module - Decryption Operations
This module provides functions for decrypting data using RSA
or post-quantum cryptographic algorithms. The decrypted data
can be saved to a file or returned as a string for further use.
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def decrypt_data(input_file, output_file, private_key_path):
    """
    Decrypts the content of an encrypted file using RSA private key decryption.
    The decrypted data is saved to the specified output file.
    
    :param input_file: Path to the encrypted input file.
    :param output_file: Path where the decrypted data will be saved.
    :param private_key_path: Path to the private key (PEM format).
    """

    # Load the private key
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=None, backend=default_backend()
        )

    # Read the encrypted input file
    with open(input_file, "rb") as enc_file:
        encrypted_data = enc_file.read()

    # Decrypt the data using the private key
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            algorithm=hashes.SHA256(),
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            label=None
        )
    )

    # Save the decrypted data to the output file
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted_data)

    print(f"[INFO] Data successfully decrypted and saved to {output_file}")


def decrypt_string(encrypted_data, private_key_path):
    """
    Decrypts a string of encrypted data using RSA private key decryption.
    
    :param encrypted_data: The encrypted data (bytes) to be decrypted.
    :param private_key_path: Path to the private key (PEM format).
    :return: Decrypted data (string).
    """
    
    # Load the private key
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(), password=None, backend=default_backend()
        )

    # Decrypt the data (bytes to string)
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            algorithm=hashes.SHA256(),
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            label=None
        )
    )

    decrypted_string = decrypted_data.decode()

    print("[INFO] Data successfully decrypted.")
    return decrypted_string
