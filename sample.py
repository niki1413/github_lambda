import one

def generate_and_save_output(file_name):
    # Generate some sample output
    output_data = one.generate_output()

    try:
        # Open the file for writing
        with open(file_name, 'w') as file:
            # Write the output to the file
            file.write(output_data)

        print(f"Output has been saved to {file_name}")

        # Return the generated output
        return output_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Specify the desired file name where you want to save the output
file_name = 'output.txt'

# Call the function to generate and save the output
output = generate_and_save_output(file_name)

# You can use 'output' as needed in your code
print("Generated output:")
print(output)
