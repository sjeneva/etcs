def extract_and_save_from_marker(source_file_path, result_file_path, start_marker):
    """
    Extracts text from a file starting from a line containing the start marker until the end of the file.

    Args:
    source_file_path: The path to the source text file.
    result_file_path: The path where the extracted text should be saved.
    start_marker: The marker indicating where to start extracting text.
    """
    # Flag to start capturing lines. Initially False and set to True once the start marker is found.
    start_capturing = False
    extracted_lines = []

    with open(source_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if start_marker in line:
                start_capturing = True
            if start_capturing:
                extracted_lines.append(line)

    # Write the extracted lines to the result file
    with open(result_file_path, 'w', encoding='utf-8') as result_file:
        result_file.writelines(extracted_lines)

    print(f"Extracted text saved to {result_file_path}")

# Example usage
source_file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\지배구조.txt'  # Update this to your source file path
result_file_path = r'C:\Users\1234\OneDrive - 인하대학교\바탕 화면\ESG_Logistics\지배구조_2.txt'  # Update this to your desired result file path
start_marker = '###'
extract_and_save_from_marker(source_file_path, result_file_path, start_marker)
