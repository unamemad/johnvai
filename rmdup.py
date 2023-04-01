input_file = "output.txt"
output_file = "output_no_duplicates.txt"

# Read lines from the input file
with open(input_file, 'r') as file:
    lines = file.readlines()

# Remove duplicates by converting the list of lines to a set and then back to a list
unique_lines = list(set(lines))

# Write the unique lines to the output file
with open(output_file, 'a') as file:
    file.writelines(unique_lines)
