# 🔐 Image Encryption Tool (GUI) v2.0


![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

A professional image encryption/decryption tool using XOR cipher, developed by Ben De Silver

## ✨ Features:

Load Image: Click "Load Image" to select an image file (PNG, JPG, JPEG, BMP, GIF)

Encryption Methods:

Swap: Swaps the red and blue channels of the image

XOR: Applies XOR operation to each pixel with the key

Add: Adds the key value to each pixel (with wrap-around)

Reverse: Reverses the order of pixels in each row

Encryption Key: Enter a value between 0-255 for XOR and Add methods

Encrypt: Click "Encrypt Image" to apply the selected encryption method

Decrypt: Click "Decrypt Image" to reverse the encryption

Save: Click "Save Result" to save the encrypted/decrypted image

 ## 🚀 How to Use the Image Encryption Tool
       
 ## Install Required Libraries:
```
pip install pillow numpy
```

 ## Run the Application:
```
python image_encryption_tool.py
```

## How the Encryption Works:
Pixel Swapping: Swaps the red and blue color channels, creating a color-shifted image

XOR Operation: Applies bitwise XOR to each pixel value with the key

Addition/Subtraction: Adds or subtracts the key value from each pixel (with 0-255 wrap-around)

Pixel Reversal: Reverses the order of pixels in each row horizontally

All operations are reversible, allowing for both encryption and decryption using the same methods.

## 📝Note:

The tool works with RGB images (converts other formats automatically)

For XOR and Add methods, use the same key for encryption and decryption

The "Swap" and "Reverse" methods are symmetric (same operation for encryption and decryption)

Always keep a backup of your original images before encryption

This simple tool demonstrates basic image encryption concepts using pixel manipulation techniques that are reversible for both encryption and decryption.

## 💻Cross-platform:
Works on both Windows, Linux & Mac

