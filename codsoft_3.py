import string
import random

spChar = '@_*&$#'
# pw of 8 char

pw = []

for i in range(2):
    pw.append(random.choice(string.ascii_uppercase))
    pw.append(random.choice(string.ascii_lowercase))
    pw.append(str(random.randint(0, 10)))
    pw.append(random.choice(spChar))

b = ''
for n in range(len(pw)):
    b += random.choice(pw)
print("password:",b,'length:',len(b))
