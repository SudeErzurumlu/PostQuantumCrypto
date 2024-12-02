"""
PostQuantumCrypto Package Initialization
This file initializes the package and provides access to key functions
and modules for encryption, decryption, key generation, and testing.
"""

# Import essential modules
from .utils.keygen import generate_key
from .utils.encrypt import encrypt_data
from .utils.decrypt import decrypt_data
from .utils.test import run_tests

__all__ = ["generate_key", "encrypt_data", "decrypt_data", "run_tests"]

# Package metadata
__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"
__description__ = "A post-quantum cryptography package for secure and efficient data encryption."
