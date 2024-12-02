
"""
Profiler Module - Performance Analysis
This module provides functions for profiling the performance of encryption,
decryption, and other cryptographic operations. It can be used to measure
execution time, memory usage, and analyze the overall performance of the system.
"""

import time
import psutil
import os
from memory_profiler import memory_usage
from utils.encrypt import encrypt_data, encrypt_string
from utils.decrypt import decrypt_data, decrypt_string


def measure_time(func, *args, **kwargs):
    """
    Measures the execution time of a function.
    
    :param func: The function to be profiled.
    :param args: Arguments to be passed to the function.
    :param kwargs: Keyword arguments to be passed to the function.
    :return: Execution time in seconds.
    """
    
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    return elapsed_time


def profile_memory(func, *args, **kwargs):
    """
    Profiles the memory usage of a function during its execution.
    
    :param func: The function to be profiled.
    :param args: Arguments to be passed to the function.
    :param kwargs: Keyword arguments to be passed to the function.
    :return: Memory usage in megabytes (MB).
    """
    
    mem_usage = memory_usage((func, args, kwargs))
    max_mem_usage = max(mem_usage)
    
    return max_mem_usage


def test_encryption_performance(input_file, output_file, public_key_path):
    """
    Profiles the encryption operation's time and memory usage on a file.
    
    :param input_file: Path to the input file to be encrypted.
    :param output_file: Path where the encrypted file will be saved.
    :param public_key_path: Path to the public key (PEM format).
    """
    
    # Measure time
    time_taken = measure_time(encrypt_data, input_file, output_file, public_key_path)
    print(f"[INFO] File encryption took {time_taken:.4f} seconds.")
    
    # Measure memory usage
    mem_usage = profile_memory(encrypt_data, input_file, output_file, public_key_path)
    print(f"[INFO] Memory usage during encryption: {mem_usage:.2f} MB")
    
    # Test performance thresholds
    assert time_taken < 3, f"Performance test failed! Encryption took {time_taken:.4f} seconds."
    assert mem_usage < 50, f"Memory usage is too high: {mem_usage:.2f} MB"


def test_decryption_performance(output_file, decrypted_output_file, private_key_path):
    """
    Profiles the decryption operation's time and memory usage on a file.
    
    :param output_file: Path to the encrypted input file.
    :param decrypted_output_file: Path where the decrypted file will be saved.
    :param private_key_path: Path to the private key (PEM format).
    """
    
    # Measure time
    time_taken = measure_time(decrypt_data, output_file, decrypted_output_file, private_key_path)
    print(f"[INFO] File decryption took {time_taken:.4f} seconds.")
    
    # Measure memory usage
    mem_usage = profile_memory(decrypt_data, output_file, decrypted_output_file, private_key_path)
    print(f"[INFO] Memory usage during decryption: {mem_usage:.2f} MB")
    
    # Test performance thresholds
    assert time_taken < 3, f"Performance test failed! Decryption took {time_taken:.4f} seconds."
    assert mem_usage < 50, f"Memory usage is too high: {mem_usage:.2f} MB"


def test_string_encryption_performance(data, public_key_path):
    """
    Profiles the performance of string encryption.
    
    :param data: The string data to be encrypted.
    :param public_key_path: Path to the public key (PEM format).
    """
    
    # Measure time
    time_taken = measure_time(encrypt_string, data, public_key_path)
    print(f"[INFO] String encryption took {time_taken:.4f} seconds.")
    
    # Measure memory usage
    mem_usage = profile_memory(encrypt_string, data, public_key_path)
    print(f"[INFO] Memory usage during string encryption: {mem_usage:.2f} MB")
    
    # Test performance thresholds
    assert time_taken < 1, f"Performance test failed! Encryption took {time_taken:.4f} seconds."
    assert mem_usage < 30, f"Memory usage is too high: {mem_usage:.2f} MB"


def test_string_decryption_performance(encrypted_data, private_key_path):
    """
    Profiles the performance of string decryption.
    
    :param encrypted_data: The encrypted data (bytes) to be decrypted.
    :param private_key_path: Path to the private key (PEM format).
    """
    
    # Measure time
    time_taken = measure_time(decrypt_string, encrypted_data, private_key_path)
    print(f"[INFO] String decryption took {time_taken:.4f} seconds.")
    
    # Measure memory usage
    mem_usage = profile_memory(decrypt_string, encrypted_data, private_key_path)
    print(f"[INFO] Memory usage during string decryption: {mem_usage:.2f} MB")
    
    # Test performance thresholds
    assert time_taken < 1, f"Performance test failed! Decryption took {time_taken:.4f} seconds."
    assert mem_usage < 30, f"Memory usage is too high: {mem_usage:.2f} MB"


def get_system_info():
    """
    Get system information such as CPU and memory usage.
    Useful for profiling the overall system performance during testing.
    """
    
    # CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"[INFO] CPU usage: {cpu_percent}%")
    
    # Memory usage
    memory_info = psutil.virtual_memory()
    print(f"[INFO] Memory usage: {memory_info.percent}% used, {memory_info.available / (1024 ** 2):.2f} MB available.")
    
    # Disk usage
    disk_info = psutil.disk_usage('/')
    print(f"[INFO] Disk usage: {disk_info.percent}% used, {disk_info.free / (1024 ** 2):.2f} MB free.")


if __name__ == "__main__":
    get_system_info()
    # Example usage for file encryption performance
    test_encryption_performance("input_file.txt", "encrypted_file.enc", "public_key.pem")
    test_decryption_performance("encrypted_file.enc", "decrypted_file.txt", "private_key.pem")
    # Example usage for string encryption performance
    test_string_encryption_performance("This is a test message.", "public_key.pem")
    test_string_decryption_performance(b"encrypted_test_data", "private_key.pem")
