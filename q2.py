def remove_duplicates_from_file(inputFile, outputFile):

    with open(inputFile, 'r') as input:
        file_content = input.readlines()
        unique_content = list(set(file_content))

    with open(outputFile, 'w') as output:
        output.write(' '.join(unique_content))

inputFile = "a5.txt"
outputFile = "a5output.txt"

print("input file before duplication")
with open(inputFile, 'r') as input_file:
    print(input_file.read())

print("Output file before duplication")
with open(outputFile, 'r') as output_file:
    print(output_file.read())

remove_duplicates_from_file(inputFile, outputFile)

print("input file after duplication")
with open(inputFile, 'r') as input_file:
    print(input_file.read())

print("Output file after duplication")
with open(outputFile, 'r') as output_file:
    print(output_file.read())