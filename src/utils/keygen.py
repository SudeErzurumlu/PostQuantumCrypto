"""
Keygen Module - Key Generation Algorithms
This module contains functions to generate cryptographic key pairs
for encryption and decryption using post-quantum cryptography methods.
"""

import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

def generate_key():
    """
    Generates a RSA key pair (public and private).
    Save the keys in PEM format for further use.
    """
    print("[INFO] Generating RSA key pair...")

    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate the public key
    public_key = private_key.public_key()

    # Serialize and save private key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Serialize and save public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Save the private key to a file
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_pem)
    print("[INFO] Private key saved as 'private_key.pem'.")

    # Save the public key to a file
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_pem)
    print("[INFO] Public key saved as 'public_key.pem'.")

    print("[INFO] Key generation complete.")


def load_private_key(path):
    """
    Loads a private key from a PEM file.
    :param path: Path to the PEM file containing the private key.
    :return: Private key object.
    """
    with open(path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )
    return private_key


def load_public_key(path):
    """
    Loads a public key from a PEM file.
    :param path: Path to the PEM file containing the public key.
    :return: Public key object.
    """
    with open(path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    return public_key

