import random
import string
import time

# a proper format but everytime remain same

# n=random.randint(27,65)
# name=input("Enter your name : ")
# encrypted=[]
# for alphabet in name:
#     encrypted.append(chr(ord(alphabet)-n))
# code=" ".join(encrypted)
# print(f"The encrypted code is {code}")
# time.sleep(5)

# every time different but not a proper format
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
encrypted = []
name = input("Text to be encrypted : ")
for alphabet in name:
    i = chars.index(alphabet)
    encrypted.append(keys[i])
result=" ".join(encrypted)
print("Encrypting the text...")
time.sleep(2)
print(f"The encrypted text : {result}")
