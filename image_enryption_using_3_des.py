# -*- coding: utf-8 -*-
"""
IMAGE_ENCRYPTION USING TRIPLE DES (3DES)
=========================================
Encrypts and decrypts image files using the Triple DES symmetric-key block cipher.
Triple DES applies the DES cipher three times (encrypt-decrypt-encrypt) for enhanced security.

Author: Rajgopal Pandilwar
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pyDes import triple_des, ECB, PAD_PKCS5
import os

# --- Configuration ---
# Triple DES requires a 24-byte key (192 bits) for 3-key mode
KEY = b"YOUR_24_BYTE_KEY_HERE!!"  # Replace with a secure 24-byte key
BLOCK_SIZE = 8  # DES operates on 64-bit (8-byte) blocks


def display_image(path):
    """
    Display an image from the given file path.

    Args:
        path (str): Absolute or relative path to the image file.
    """
    img = mpimg.imread(path)
    plt.imshow(img)
    plt.axis("off")
    plt.show()


def pad_data(data):
    """
    Pad data to be a multiple of the DES block size (8 bytes) using PKCS#5 padding.

    Args:
        data (bytes): Raw binary data to pad.

    Returns:
        bytes: Padded data, length is a multiple of 8.
    """
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)


def unpad_data(data):
    """
    Remove PKCS#5 padding from decrypted data.

    Args:
        data (bytes): Padded data to strip.

    Returns:
        bytes: Original data with padding removed.
    """
    pad_len = data[-1]
    return data[:-pad_len]


def encrypt_image(image_path, output_path="encrypted.bin", key=KEY):
    """
    Encrypt an image file using Triple DES encryption.

    Args:
        image_path (str): Path to the source image file.
        output_path (str): Path where the encrypted file will be saved.
        key (bytes): 24-byte encryption key.

    Returns:
        str: Path to the encrypted output file.
    """
    # Read the image file as raw bytes
    with open(image_path, "rb") as f:
        raw_data = f.read()

    print(f"Original image size: {len(raw_data)} bytes")

    # Pad data to align with 8-byte DES block boundary
    padded_data = pad_data(raw_data)

    # Initialize Triple DES cipher in ECB mode
    cipher = triple_des(key, ECB, pad=None, mode=ECB)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)
    print(f"Encrypted data size: {len(encrypted_data)} bytes")

    # Write encrypted bytes to output file
    with open(output_path, "wb") as f:
        f.write(encrypted_data)

    print(f"Image encrypted successfully! Saved to {output_path}")
    return output_path


def decrypt_image(encrypted_path, output_path="decrypted.png", key=KEY):
    """
    Decrypt a Triple DES encrypted file back to an image.

    Args:
        encrypted_path (str): Path to the encrypted file.
        output_path (str): Path where the decrypted image will be saved.
        key (bytes): 24-byte decryption key (must match the encryption key).

    Returns:
        str: Path to the decrypted output file.
    """
    # Read the encrypted file
    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    # Initialize Triple DES cipher with the same key
    cipher = triple_des(key, ECB, pad=None, mode=ECB)

    # Decrypt the data
    decrypted_padded = cipher.decrypt(encrypted_data)

    # Remove PKCS#5 padding to recover original bytes
    decrypted_data = unpad_data(decrypted_padded)

    # Write decrypted bytes to output image file
    with open(output_path, "wb") as f:
        f.write(decrypted_data)

    print(f"Image decrypted successfully! Saved to {output_path}")
    return output_path


# === Main Execution ===
if __name__ == "__main__":
    # Example: Encrypt then decrypt an image
    # Step 1: Encrypt
    # encrypt_image("input_image.png", "encrypted.bin")

    # Step 2: Decrypt
    # decrypt_image("encrypted.bin", "output_image.png")

    # Display the result
    # display_image("output_image.png")

    print("Triple DES Image Encryption tool ready.")
    print("Set your 24-byte KEY and uncomment the example usage above.")
