from edit_distance import edit_distance
from recover_operations import recover_operations
import sys


def main():
    try:
        X = input("Enter string X: ")
        Y = input("Enter string Y: ")
        m, n = len(X), len(Y)
        distance = edit_distance(X, Y, m, n)
        operations = recover_operations(X, Y, m, n, None)
        print(f"Minimum edit distance between '{X}' and '{Y}' is: {distance}")
        print("Operations:")
        for op in operations:
            print("- " + op)
    except (ValueError, TypeError) as e:
        print("Error:", e)
        print("Please enter valid strings.")
        sys.exit(1)
    except Exception as e:
        print("Unexpected error occurred:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
