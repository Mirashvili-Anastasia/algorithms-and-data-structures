def generate_parentheses(n):
    result = []

    def build(current, opened, closed):
        if len(current) == 2 * n:
            result.append(current)
            return

        if opened < n:
            build(current + '(', opened + 1, closed)

        if closed < opened:
            build(current + ')', opened, closed + 1)

    build('', 0, 0)

    return result


def main():
    n = int(input())

    for sequence in generate_parentheses(n):
        print(sequence)

if __name__ == "__main__":
    main()