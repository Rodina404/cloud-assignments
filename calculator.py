import sys

def parse_number(prompt):
    s = input(prompt)
    try:
        return float(s) if ('.' in s or 'e' in s.lower()) else int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            print(f"Invalid number: {s}")
            sys.exit(1)

def main():
    a = parse_number("Enter first number: ")
    b = parse_number("Enter second number: ")
    print(f"Addition: {a + b}")
    print(f"Multiplication: {a * b}")

if __name__ == "__main__":
    main()
