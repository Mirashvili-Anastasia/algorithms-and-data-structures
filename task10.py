def generate_combinations(digits, current="", index=0, result=None):
    if result is None:
        result = []

    if index == len(digits):
        result.append(current)
        return result

    letters = phone_map[digits[index]]

    for letter in letters:
        generate_combinations(digits, current + letter, index + 1, result)

    return result

phone_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

digits = input().strip()

combinations = generate_combinations(digits)

combinations.sort()
print(' '.join(combinations))