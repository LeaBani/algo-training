import codecs

def rot13(text):
    return codecs.encode(text, 'rot_13')

# Example usage:
original_text = "Hello, World!"
encrypted_text = rot13(original_text)
print(f"Original: {original_text}")
print(f"Encrypted: {encrypted_text}")