Pixel Manipulation for Image Encryption


Python-based image encryption tool using pixel manipulation, where you can apply basic operations like swapping pixel values or performing mathematical operations (e.g., adding or subtracting values) to encrypt and decrypt an image.
This solution uses the Pillow library, which is commonly used for image processing in Python.

Steps:
Encrypt the image by modifying pixel values using a basic mathematical operation.
Decrypt the image by reversing the operation to retrieve the original image.

Requirement :

*pip install pillow*

How the Program Works:
encrypt_image:
Opens the input image, loops through each pixel, and adjusts the red, green, and blue (RGB) values by adding a user-specified encryption key.
The new pixel values are wrapped around (using % 256) to stay within the valid range for RGB values (0-255).
The encrypted image is saved to a specified path.
decrypt_image:
Reverses the encryption by subtracting the same key from each pixel's RGB values.
The original image is restored and saved as a new file.
User Input: The program prompts the user for the path of the image file, a key (an integer), and whether they want to encrypt or decrypt the image.


 """
    Encrypts an image by manipulating its pixel values using a given key.

   Parameters:
    - image_path: str, the path of the image to encrypt.
    - key: int, the encryption key (a value used to modify the pixels).
    - output_path: str, the path to save the encrypted image.
"""

 """
    Decrypts an image by reversing the pixel manipulation using the given key.

   Parameters:
    - image_path: str, the path of the encrypted image.
    - key: int, the decryption key (same as the encryption key).
    - output_path: str, the path to save the decrypted image.
    """

