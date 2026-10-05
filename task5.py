text = input()
text = text.lower()
new_text = ""
for char in text:
    if char.isalnum():
        new_text += char

if new_text == new_text[::-1]:
    print("True")
else:
    print("False")