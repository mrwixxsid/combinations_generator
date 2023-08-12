import itertools
import argparse

def generate_combinations(input_str):
    input_str = input_str.replace(" ", "")  # Remove spaces
    combinations = set()
    for combo in itertools.permutations(input_str, len(input_str)):
        combinations.add(''.join(combo))
    return combinations

def save_to_file(combinations, filename):
    with open(filename, 'w') as file:
        for combo in combinations:
            file.write(combo + '\n')

def main():
    parser = argparse.ArgumentParser(description="Generate and save combinations of input text.")
    parser.add_argument("input", type=str, help="Input text (letters, numbers, symbols)")
    parser.add_argument("-o", "--output", type=str, help="Output filename", default="password.txt")
    args = parser.parse_args()

    input_text = args.input
    output_filename = args.output

    if not input_text:
        print("Input text must not be empty.")
        return

    if not any(c.isalpha() for c in input_text):
        print("Input text must contain at least one letter.")
        return

    combinations = generate_combinations(input_text)
    save_to_file(combinations, output_filename)

    print(f"Combinations with input text '{input_text}' saved to {output_filename}")

if __name__ == "__main__":
    main()

