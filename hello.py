import os

print('hello')
print('hello')


directory = input("Enter the directory to list: ")
# Vulnerable: An attacker can enter something like "; cat /etc/passwd" to run arbitrary commands
command = f"ls {directory}"
os.system(command)
