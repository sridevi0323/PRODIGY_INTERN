# Caesar Cipher Implementation
def caesar_cipher(text, shift, mode='encrypt'):
  
    result = ''
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    return result

if __name__ == "__main__":
    message = input("Enter the message: ")
    shift_value = int(input("Enter the shift value: "))
    
    encrypted_message = caesar_cipher(message, shift_value, mode='encrypt')
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = caesar_cipher(encrypted_message, shift_value, mode='decrypt')
    print(f"Decrypted Message: {decrypted_message}")
