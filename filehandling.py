def modify_content(content):
    return content.upper()

def read_and_write_file():
    try:
        
        input_filename = input("Enter the name of the file to read: ")

       
        with open(input_filename, 'r') as infile:
            content = infile.read()

       
        modified_content = modify_content(content)

      
        output_filename = input("Enter the name of the new file to save modified content: ")

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f" File '{output_filename}' created successfully with modified content!")

    except FileNotFoundError:
        print("Error: The file you entered does not exist.")
    except IOError as e:
        print(f" IOError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_write_file()
