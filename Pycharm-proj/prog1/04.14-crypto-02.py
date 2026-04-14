import string
abc=string.ascii_letters
input_txt=input('szöveg: ')
shift=int(input("eltolás: "))
txt_len=len(input_txt)
enc_txt=''

for i in range(txt_len):
    letters=input_txt[i]
    location=abc.find(letters)
    new_location=(location+shift)%26
    enc_txt+=abc[new_location]
print(enc_txt)
