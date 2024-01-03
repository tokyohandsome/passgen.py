import string
import secrets
import sys

num = 12
if len(sys.argv) >= 2:
    num = int(sys.argv[1])

punctuation = string.punctuation
letters = string.ascii_letters
digits = string.digits

password = ''.join(secrets.choice(punctuation + letters + digits) for i in range(num))

print(password)
