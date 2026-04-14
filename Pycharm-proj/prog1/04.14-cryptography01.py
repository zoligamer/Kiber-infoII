import random
import string

text=''+string.ascii_letters+string.digits+string.punctuation
text = list(text)
key = text.copy()
random.shuffle(key)

text_input = input("szöveg: ")
encrypted_text=''

for i in text_input:
    index=text.index(i)
    encrypted_text+=key[index]

#decrypt:

decrypted_text=''
for i in encrypted_text:
    index=key.index(i)
    encrypted_text+=text[index]

print(encrypted_text)
print('\n')
print(decrypted_text)