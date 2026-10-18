def is_correct_bracket_seq(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return s == ""
s = input()
print(is_correct_bracket_seq(s))