import bcrypt

# Step 1: User creates a password
user_password = input("12345678: ")

# Convert to bytes (bcrypt needs bytes)
password_bytes = user_password.encode()

# Step 2: Hash the password
hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print("\nStored Hashed Password:")
print(hashed_password)

# Step 3: Ask user to type password again to verify
typed_password = input("\nType your password to verify: ")
typed_password_bytes = typed_password.encode()

# Step 4: Compare typed password with stored hash
is_correct = bcrypt.checkpw(typed_password_bytes, hashed_password)

# Step 5: Print result
if is_correct:
    print("\n Correct password")
else:
    print("\n Wrong password")
