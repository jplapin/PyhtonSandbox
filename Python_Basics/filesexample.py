# creates a new file in the current directory
# the flag w+ indicates that we will write to the file
new_file = open("text.txt", "w+")

text = "This is the content to be written to the text file"

new_file.write(text)
