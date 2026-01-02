import os
import csv

def save_text_to_csv(file_path, text_content):
    """
    Saves the given text content to a CSV file.

    Each line in the text will become a row in the CSV file.
    """
    # Ensure the file path ends with .csv
    if not file_path.lower().endswith(".csv"):
        file_path += ".csv"

    # Split text into lines
    lines = text_content.splitlines()

    try:
        with open(file_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            # Write each line as a separate row
            for line in lines:
                # Each line as a single column
                writer.writerow([line])

        print(f"Saved CSV successfully: {os.path.abspath(file_path)}")
        return True
    except Exception as e:
        print(f"Error saving CSV: {e}")
        return False
