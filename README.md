# Image Security by Triple DES

Encryption and decryption of images using the Triple DES (3DES) algorithm — a symmetric-key block cipher that applies the DES cipher three times to each data block.

## Author

**Rajgopal Pandilwar**

## Based On Original Work By

This project is based on original work by **Vatshayan** — [Original Repository](https://github.com/Vatshayan/Image-Security-by-Triple-DES-Final-Year-Project)

## What is Triple DES?

In cryptography, Triple DES (officially the Triple Data Encryption Algorithm) applies the DES cipher algorithm three times to each data block for enhanced security.

- **Block size:** 64 bits
- **Key sizes:** 168, 112, or 56 bits

### Why Triple DES?

Standard DES uses a 56-bit key which is vulnerable to modern brute-force attacks. Triple DES applies encryption three times with different keys (or the same key), making it significantly more secure than single DES.

### Encryption Process

```
Encrypt with Key 1 → Decrypt with Key 2 → Encrypt with Key 3
```

### Decryption Process

```
Decrypt with Key 3 → Encrypt with Key 2 → Decrypt with Key 1
```

## Files

| File | Description |
|------|-------------|
| `image_enryption_using_3_des.py` | Python implementation of Triple DES image encryption |
| `IMAGE_ENRYPTION_USING_3_DES.ipynb` | Jupyter Notebook with step-by-step walkthrough |
| `IMAGE SECURITY 3 DES PROJECT CODE.pdf` | Full project code in PDF format |
| `IMAGE SECURITY BY 3 DES.pdf` | Project presentation/report |

## Dependencies

```bash
pip install pyDes matplotlib
```

## How to Use

1. Install dependencies
2. Run the Python script or open the notebook
3. Provide an image path and encryption key
4. The encrypted/decrypted image will be saved to the specified output path
