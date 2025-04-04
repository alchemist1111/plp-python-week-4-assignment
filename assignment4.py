def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()  # Read the entire content of the file

        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Open a new file in write mode to save the modified content
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File has been successfully modified and saved as {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except IOError:
        print(f"Error: Could not read or write the file {input_filename}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input and output filenames
    input_filename = input("Enter the name of the file you want to read: ")
    output_filename = input("Enter the name of the file to save the modified content: ")

    # Call the function to read and modify the file
    read_and_modify_file(input_filename, output_filename)

# Run the program
if __name__ == "__main__":
    main()
