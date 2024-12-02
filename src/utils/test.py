"""
Test Module - Performance and Security Tests
This module provides functions for testing the encryption
and decryption operations for both security and performance.
Tests include correctness of operations, execution time,
and potential vulnerabilities.
"""

import time
import os
import random
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from utils.encrypt import encrypt_data, encrypt_string
from utils.decrypt import decrypt_data, decrypt_string
import pytest


# Performance Test for File Encryption
def test_encryption_performance(input_file, output_file, public_key_path):
    """
    Tests the performance of the encryption operation on a file.
    It measures the time taken to encrypt the input file.
    
    :param input_file: Path to the input file to be encrypted.
    :param output_file: Path where the encrypted file will be saved.
    :param public_key_path: Path to the public key (PEM format).
    """
    
    start_time = time.time()
    encrypt_data(input_file, output_file, public_key_path)
    elapsed_time = time.time() - start_time
    print(f"[INFO] File encryption completed in {elapsed_time:.4f} seconds.")
    
    # Assert that the file encryption time is below a threshold
    assert elapsed_time < 2, f"Performance test failed! Encryption took {elapsed_time:.4f} seconds."


# Performance Test for String Encryption
def test_string_encryption_performance(data, public_key_path):
    """
    Tests the performance of the string encryption operation.
    It measures the time taken to encrypt a string of data.
    
    :param data: The string data to be encrypted.
    :param public_key_path: Path to the public key (PEM format).
    """
    
    start_time = time.time()
    encrypted_data = encrypt_string(data, public_key_path)
    elapsed_time = time.time() - start_time
    print(f"[INFO] String encryption completed in {elapsed_time:.4f} seconds.")
    
    # Assert that the string encryption time is below a threshold
    assert elapsed_time < 1, f"Performance test failed! Encryption took {elapsed_time:.4f} seconds."


# Correctness Test for Encryption and Decryption
def test_encryption_decryption_correctness(input_file, output_file, private_key_path, public_key_path):
    """
    Tests the correctness of the encryption and decryption operations.
    It encrypts data and then decrypts it, checking if the result matches
    the original input.
    
    :param input_file: Path to the input file to be encrypted and decrypted.
    :param output_file: Path where the encrypted file will be saved.
    :param private_key_path: Path to the private key (PEM format).
    :param public_key_path: Path to the public key (PEM format).
    """
    
    # Encrypt the file
    encrypt_data(input_file, output_file, public_key_path)
    
    # Decrypt the file
    decrypt_data(output_file, "decrypted_file.txt", private_key_path)
    
    # Compare the original and decrypted files
    with open(input_file, "rb") as original_file, open("decrypted_file.txt", "rb") as decrypted_file:
        original_data = original_file.read()
        decrypted_data = decrypted_file.read()
        assert original_data == decrypted_data, "Decrypted data does not match the original!"


# Security Test for Private Key Protection
def test_private_key_protection(private_key_path):
    """
    Tests if the private key is protected with a password.
    A password-protected private key is more secure and should be
    tested to ensure it cannot be loaded without the password.
    
    :param private_key_path: Path to the private key (PEM format).
    """
    
    try:
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(), password=None  # No password provided for the test
            )
        assert False, "Security test failed! Private key was loaded without a password."
    except ValueError as e:
        print(f"[INFO] Private key is protected: {str(e)}")


# Security Test for Key Size
def test_key_size():
    """
    Tests if the RSA key pair has an adequate size for security (e.g., 2048 bits).
    This ensures that the key is secure enough for modern cryptography.
    """
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,  # Use at least 2048 bits for strong security
        backend=default_backend()
    )
    
    public_key = private_key.public_key()
    assert private_key.key_size >= 2048, f"Security test failed! Key size is too small: {private_key.key_size} bits."
    print(f"[INFO] Key size is sufficient: {private_key.key_size} bits.")


# Randomness Test for Key Generation
def test_key_generation_randomness():
    """
    Tests the randomness of the key generation process. It ensures that the keys are not
    predictable by comparing multiple key generations.
    """
    
    key1 = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    key2 = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # Assert that the generated keys are different
    assert key1.private_numbers() != key2.private_numbers(), "Security test failed! Keys are not unique."


# Run all tests with pytest
if __name__ == "__main__":
    pytest.main()
