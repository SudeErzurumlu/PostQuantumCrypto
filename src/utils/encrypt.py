"""
Encrypt Module - Encryption Operations
This module provides functions for encrypting data using RSA
or post-quantum cryptographic algorithms. The encrypted data
can be saved to a file for further use or transmission.
"""

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os


def encrypt_data(input_file, output_file, public_key_path):
    """
    Encrypts the content of an input file using RSA public key encryption.
    The encrypted data is saved to the specified output file.
    
    :param input_file: Path to the input file to be encrypted.
    :param output_file: Path where the encrypted data will be saved.
    :param public_key_path: Path to the public key (PEM format).
    """

    # Load the public key
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(), backend=default_backend()
        )

    # Read the input file data
    with open(input_file, "rb") as file:
        data = file.read()

    # Encrypt the data using the public key
    encrypted_data = public_key.encrypt(
        data,
        padding.OAEP(
            algorithm=hashes.SHA256(),
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            label=None
        )
    )

    # Save the encrypted data to the output file
    with open(output_file, "wb") as enc_file:
        enc_file.write(encrypted_data)

    print(f"[INFO] Data successfully encrypted and saved to {output_file}")


def encrypt_string(data, public_key_path):
    """
    Encrypts a string of data using RSA public key encryption.
    
    :param data: The data (string) to be encrypted.
    :param public_key_path: Path to the public key (PEM format).
    :return: Encrypted data (bytes).
    """
    
    # Load the public key
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(), backend=default_backend()
        )

    # Encrypt the data (string to bytes)
    encrypted_data = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            algorithm=hashes.SHA256(),
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            label=None
        )
    )

    print("[INFO] Data successfully encrypted.")
    return encrypted_data


