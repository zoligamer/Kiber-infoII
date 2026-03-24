"""import itertools
import string

def password_generator(max_len=3):
    chars=string.ascii_lowercase
    for i in range(1,max_len+1):
        for x in itertools.product(chars,repeat=i):
            yield ''.join(x)

for x in password_generator(max_len=5):
    print(x)

"""

def read(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            print(f"[read]{line.strip()}")
            yield line.strip()

def find(line):
    for x in line:
        if "FAILED LOGIN" in x:
            yield x

logs=read("auth.log")
error=find(logs)
for i in error:
    print(i)