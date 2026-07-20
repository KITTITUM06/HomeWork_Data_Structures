text = input()

while "()" in text or "{}" in text or "[]" in text:
    text = text.replace("()", "").replace("{}", "").replace("[]", "")

result = text == "" # เปรียบเทียบ
print(result)