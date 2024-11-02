from PIL import Image

def encrypt_image(image_path, key, output_path):
   
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure the image is in RGB mode
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Loop over each pixel and modify the values
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Encrypt each RGB value by adding the key
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Save the encrypted image
    img.save(output_path)
    print(f"Encrypted image saved as {output_path}")


def decrypt_image(image_path, key, output_path):
   
    # Open the image
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Loop over each pixel and reverse the encryption
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            # Decrypt each RGB value by subtracting the key
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save the decrypted image
    img.save(output_path)
    print(f"Decrypted image saved as {output_path}")


if __name__ == "__main__":
    # User input for image path, encryption key, and operation
    image_path = input("Enter the path of the image: ")
    key = int(input("Enter the encryption/decryption key (a number): "))
    choice = input("Do you want to 'encrypt' or 'decrypt' the image? ").lower()

    if choice == 'encrypt':
        output_path = "encrypted_image.png"
        encrypt_image(image_path, key, output_path)
    elif choice == 'decrypt':
        output_path = "decrypted_image.png"
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
