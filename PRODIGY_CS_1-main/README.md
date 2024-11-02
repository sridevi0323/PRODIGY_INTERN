Caesar Cipher Python Implementation

Project Description

This project implements a Caesar Cipher, one of the simplest and most widely known encryption techniques. In this cipher, each letter in the plaintext is shifted by a certain number of positions in the alphabet. This Python program allows users to both encrypt and decrypt text using a specified shift value.
Features

Encrypts text using the Caesar Cipher algorithm.
Decrypts the encrypted text back to its original form.
Supports both uppercase and lowercase letters.
Preserves non-alphabetic characters such as spaces and punctuation.
How It Works

Encryption: Shifts each letter in the input message by a given number of positions in the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.
Decryption: Reverses the shift, transforming the encrypted text back to the original message.
***
Function to encrypt or decrypt text using the Caesar Cipher algorithm.
Parameters:
    text (str): The message to be encrypted or decrypted.
    shift (int): The shift value for the cipher.
    mode (str): Either 'encrypt' or 'decrypt' to specify the operation. Default is 'encrypt'.
Returns:
    str: The resulting encrypted or decrypted message.
***
