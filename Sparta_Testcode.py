#F-string

#mixture = [1,2,3,"one","two","three"]

#for i in range(len(mixture)-1 , 3, -1):
#    print(mixture[i])


#for item in mixture[::-1]:
#    print(item)

#for item in mixture[1::2]:
#    print(item)
#print(f"[{mixture[1]}],[{mixture[2]}]")

def count_vowels(password):
    """
    Counts the number of vowels in a given password.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in password if char in vowels)

# Step 1: Ask the user to input 3 passwords
passwords = []


for i in range(3):
    password = input(f"Enter password {i + 1}: ")
    passwords.append(password)

# Step 2: Method to check how many vowels are in each password
for idx, password in enumerate(passwords, start=1):
    vowel_count = count_vowels(password)
    print(f"Password {idx} ('{password}') contains {vowel_count} vowel(s).")
