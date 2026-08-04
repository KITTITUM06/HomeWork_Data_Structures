text = input()
list_chars = []

for chars in text:
    lower_chars = chars.lower() 
    if lower_chars not in list_chars:
        list_chars.append(lower_chars)
        
    data = "".join(sorted(list_chars))
    
print(data)