"""
PostQuantumCrypto - Main Execution File
This is the entry point for running encryption, decryption, and key generation
operations using the PostQuantumCrypto package.
"""

import argparse
from src.utils.keygen import generate_key
from src.utils.encrypt import encrypt_data
from src.utils.decrypt import decrypt_data
from src.utils.test import run_tests


def main():
    """
    Main function to handle command-line arguments and execute the desired operation.
    """
    # Create argument parser
    parser = argparse.ArgumentParser(
        description="Post-Quantum Cryptography CLI Tool for encryption, decryption, and key management."
    )
    
    # Add arguments
    parser.add_argument(
        "--operation",
        type=str,
        choices=["keygen", "encrypt", "decrypt", "test"],
        required=True,
        help="The operation to perform: keygen (generate keys), encrypt, decrypt, or test."
    )
    parser.add_argument(
        "--input",
        type=str,
        help="Input file or data for encryption/decryption. Not required for keygen or test."
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file to save the results. Not required for keygen or test."
    )
    parser.add_argument(
        "--key",
        type=str,
        help="Path to the key file for encryption/decryption. Required for encrypt and decrypt."
    )

    # Parse arguments
    args = parser.parse_args()

    # Handle operations
    if args.operation == "keygen":
        print("[INFO] Generating a new key pair...")
        generate_key()
        print("[INFO] Key pair generated successfully!")

    elif args.operation == "encrypt":
        if not args.input or not args.output or not args.key:
            print("[ERROR] --input, --output, and --key are required for encryption.")
        else:
            print(f"[INFO] Encrypting data from {args.input}...")
            encrypt_data(args.input, args.output, args.key)
            print(f"[INFO] Data encrypted successfully and saved to {args.output}.")

    elif args.operation == "decrypt":
        if not args.input or not args.output or not args.key:
            print("[ERROR] --input, --output, and --key are required for decryption.")
        else:
            print(f"[INFO] Decrypting data from {args.input}...")
            decrypt_data(args.input, args.output, args.key)
            print(f"[INFO] Data decrypted successfully and saved to {args.output}.")

    elif args.operation == "test":
        print("[INFO] Running performance and security tests...")
        run_tests()
        print("[INFO] Tests completed successfully!")

    else:
        print("[ERROR] Unknown operation.")

if __name__ == "__main__":
    main()
