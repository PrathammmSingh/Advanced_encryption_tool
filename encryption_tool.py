from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved as 'encryption_key.key'.")

def load_key():
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path + ".enc", "wb") as enc_file:
        enc_file.write(encrypted_data)
    print(f"[+] Encrypted file saved as '{file_path}.enc'.")

def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as enc_file:
        encrypted_data = enc_file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    original_path = file_path.replace(".enc", "")
    with open(original_path, "wb") as dec_file:
        dec_file.write(decrypted_data)
    print(f"[+] Decrypted file saved as '{original_path}'.")

def main():
    print("Advanced Encryption Tool")
    print("========================")
    print("1. Generate Encryption Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        generate_key()
    elif choice == "2":
        file_path = input("Enter the file path to encrypt: ")
        encrypt_file(file_path)
    elif choice == "3":
        file_path = input("Enter the file path to decrypt: ")
        decrypt_file(file_path)
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
