import random, string

alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits

password_length = int(input("Enter the password length: "))
password = ''

for i in range(password_length):
    choice = random.choice(alphabet)
    password += choice

print(password)