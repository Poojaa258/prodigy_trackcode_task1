from PIL import Image

def encrypt_image(image_path, key):
    with Image.open(image_path, 'r') as img:
        pixels = img.load()
        width, height = img.size

        for py in range(height):
            for px in range(width):
                r, g, b = pixels[px, py]
                pixels[px, py] = (r ^ key, g ^ key, b ^ key)

    img.save("encrypted_image.png")
    print("Image encrypted successfully.")

def decrypt_image(image_path, key):
    with Image.open(image_path, 'r') as img:
        pixels = img.load()
        width, height = img.size

        for py in range(height):
            for px in range(width):
                r, g, b = pixels[px, py]
                pixels[px, py] = (r ^ key, g ^ key, b ^ key)

    img.save("decrypted_image.png")
    print("Image decrypted successfully.")

if __name__ == "__main__":
    image_path = input("Enter the path of the image: ")
    key = int(input("Enter the encryption/decryption key: "))

    # Encrypt the image
    encrypt_image(image_path, key)

    # Decrypt the image
    decrypt_image("encrypted_image.png", key)
