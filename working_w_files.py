#This assumes that the file is in the same folder as the main .py script
file_path = "some_filename.txt"

file_content = []

with open(file_path) as file:
    for line in file:
        file_content.append(line)

print(file_content)

no_of_lines = int(input("How many lines to read? :  "))
with open(file_path) as file:
    lines = file.readlines()
    num_lines = len(lines)

    if num_lines < no_of_lines:
        print(f"Please enter a values. The file has {num_lines} lines.")
    else:
        for i in range(no_of_lines):
            #If you wanted to read the last lines of the text then:

            #for i in range(-no_of_lines,0):
            #would have to be used.
            #The strip function removes the next line character,
            #this prevents a blank line from being inserted.
            print(lines[i].strip("\n"))

longest_word = ""

with open(file_path) as file:
    for word in file:
        if len(word) > len(longest_word):
            longest_word = word

print(longest_word)

#Assumes that the dictionary has 1 word per line
freq_dict = {}
with open(file_path) as file:
    for word in file:
        word = word.strip("\n")
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1

print(freq_dict)

#Writing to a file
write_path = "file_written.txt"
my_list = [1, 5, 8, 9, 4, 6]
with open(write_path, "w") as file:
    for element in my_list:
        file.write(str(element))
# This  willl write all element to 1 line
#
#This one below will write to a new line
#        file.write(str(element)+"\n")

#Copy a file
file_path = "some_filename.txt"
copy_path = "copied_filename.txt"

with open(file_path) as file, open(copy_path, "w") as copy:
    #To split the above line into 2 we introduce a \
    # with open(file_path) as file, \
    #           open(copy_path, "w") as copy:
    for line in file:
        copy.write(line)

#To check if file exists
import os.path

my_file = "some_file_path.txt"

if os.path.isfile(my_file):
    print(f"The file {my_file} exists.")
else:
    print(f"The file {my_file} does NOT exist.")


