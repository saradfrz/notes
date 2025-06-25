# main.py

import re
from parameters import INPUT_FILE_PATH, OUTPUT_FILE_PATH, REGEX_PATTERNS

def read_input_file(file_path: str) -> str:
    """Reads the entire content of the input file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found at: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading file {file_path}: {e}")

def find_matches(text: str, pattern: str) -> list[str]:
    """Finds all non-overlapping matches using the given regex pattern."""
    return re.findall(pattern, text)

def write_output_file(file_path: str, matches: list[str]) -> None:
    """Writes matches to an output file, one per line."""
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for match in matches:
                file.write(f"{match}\n")
    except Exception as e:
        raise RuntimeError(f"Error writing file {file_path}: {e}")

def run_regex_extraction(input_path: str, output_path: str, pattern: str) -> None:
    """Pipeline to extract regex matches from a file and save the output."""
    print(f"Reading from {input_path}")
    text = read_input_file(input_path)

    print(f"Finding matches with pattern: {pattern}")
    matches = find_matches(text, pattern)

    print(f"Writing {len(matches)} matches to {output_path}")
    write_output_file(output_path, matches)

if __name__ == "__main__":
    run_regex_extraction(INPUT_FILE_PATH, OUTPUT_FILE_PATH, REGEX_PATTERNS['chapter'])
