import fileinput

file_path = 'keypairs1.txt'  # Replace 'file.txt' with the actual file path

# Delete the first line of the file
with fileinput.input(file_path, inplace=True) as file:
    first_line = True
    for line in file:
        if not first_line:
            print(line, end='')
        first_line = False