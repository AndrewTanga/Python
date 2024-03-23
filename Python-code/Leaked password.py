leaked_passwords = ['password123', 'admin', '123456', '@dmin123']
common_passwords = ['password', 'admin', '123456', 'admin123']

def crack_passwords():
  cracked_passwords = []

  for leaked_password in leaked_passwords:
      if leaked_password in common_passwords:
          cracked_passwords.append(leaked_password)

  return cracked_passwords

cracked_passwords_list = crack_passwords()

print("Cracked Passwords:", cracked_passwords_list)