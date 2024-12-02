"""
Utils Module Initialization
This module contains utility functions for key generation, encryption, decryption,
performance profiling, and testing within the PostQuantumCrypto package.
"""

# Import core utility functions
from .keygen import generate_key
from .encrypt import encrypt_data
from .decrypt import decrypt_data
from .test import run_tests
from .profiler import profile_performance

__all__ = [
    "generate_key",
    "encrypt_data",
    "decrypt_data",
    "run_tests",
    "profile_performance",
]

# Package metadata specific to utils
__utils_version__ = "1.0.0"
__utils_author__ = "Your Name"
__utils_description__ = "Utility functions for cryptographic operations and testing."
