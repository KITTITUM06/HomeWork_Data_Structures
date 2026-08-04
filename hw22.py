user_input = input()
passwords = user_input.split(",")
valid_passwords = []
for p in passwords:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    
    if len(p) >= 6 and len(p) <= 12:
        
        for char in p:
            if char.islower():    
                has_lower = True
            elif char.isdigit():  
                has_digit = True
            elif char.isupper():  
                has_upper = True
            elif char in "$#@":   
                has_special = True
                
        if has_lower and has_digit and has_upper and has_special:
            valid_passwords.append(p)

print(",".join(valid_passwords))