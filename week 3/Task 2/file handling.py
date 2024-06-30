# File: Library Management System/file_handling.py

def read_file(file_path):
    # """
    # Read and print the contents of a file. Also, count and print the number of words in the file.

    # :param file_path: str: Path to the file to be read.
    # """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Contents:")
            print(content)
            word_count = len(content.split())
            print(f"Number of words: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")


def write_to_file(file_path, content):
    # """
    # Write the user input to a file.

    # :param file_path: str: Path to the file to be written.
    # :param content: str: The content to be written to the file.
    # """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content written to '{file_path}' successfully.")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")


if __name__ == "__main__":
    # Reading from 'data.txt'
    read_file("data.txt")

    # Writing user input to 'output.txt'
    user_input = input("Enter some text to write to the file 'output.txt': ")
    write_to_file("output.txt", user_input)
