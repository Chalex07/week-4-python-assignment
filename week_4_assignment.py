def read_and_write_file():
    try:
        # Inputting the file name
        input_file = input("Enter the name of the file to read: ")
        
        # Opening and reading the file
        with open(input_file, 'r') as file:
            content = file.readlines()
        
        # Modify the content (example: add line numbers)
        modified_content = [f"{i+1}: {line}" for i, line in enumerate(content)]
        
        # Ask for the name of the output file
        output_file = input("Enter the name of the file to save the modified content: ")
        
        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)
        
        print(f"Modified content written successfully to '{output_file}'!")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_write_file()
