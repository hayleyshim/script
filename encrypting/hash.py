from hashlib import sha256

text = input("please enter the text: ")
hash_of_text = sha256(text.encode())
print(hash_of_text.hexdigest())
