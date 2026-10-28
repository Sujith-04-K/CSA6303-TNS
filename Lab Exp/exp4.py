def xor_cipher(data, key):
    return bytes(byte ^ key[i % len(key)] for i, byte in enumerate(data))

message = input("Enter message: ").encode("utf-8")
key = input("Enter shared key: ").encode("utf-8")

if not key:
    raise ValueError("Key cannot be empty.")

encrypted = xor_cipher(message, key)
print("Intercepted ciphertext (hex):", encrypted.hex())

decrypted = xor_cipher(encrypted, key)
print("Decrypted message:", decrypted.decode("utf-8"))

wrong_key = b"wrong"
wrong_decryption = xor_cipher(encrypted, wrong_key)
print("Wrong-key output (hex):", wrong_decryption.hex())
print("Educational demonstration only: repeating-key XOR is not secure VPN encryption.")
