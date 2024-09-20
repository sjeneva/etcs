import os
import re

def find_missing_numbers(directory, pattern):
    files = os.listdir(directory)
    numbers = []

    # Extract numbers from filenames based on the given pattern
    for filename in files:
        match = re.search(pattern, filename)
        if match:
            numbers.append(int(match.group(1)))

    # Check if no numbers were found
    if not numbers:
        print("No numbers found in filenames. Please check the pattern or the directory.")
        return []

    # Find missing numbers in the sequence
    numbers = sorted(numbers)
    missing_numbers = [num for num in range(numbers[0], numbers[-1] + 1) if num not in numbers]

    return missing_numbers

# Directory containing the files
directory = "C:\\Users\\1234\\OneDrive - 인하대학교\\바탕 화면\\ESGL_Korean\\LDA_English_Korean\\Extracted_Articles\\"

# Pattern to extract numbers from filenames (assuming filenames like "GoogleNews_article_001_...txt", "GoogleNews_article_002_...txt", etc.)
pattern = r'GoogleNews_article_(\d+)_'

missing_numbers = find_missing_numbers(directory, pattern)

if missing_numbers:
    print("Missing numbers in the sequence:")
    for num in missing_numbers:
        print(num)
else:
    print("No missing numbers found or no valid files to process.")
