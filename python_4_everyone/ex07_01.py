# Write a program to read a file and print the contents of the file (line by line) all in upper case

file_handle=open('mbox.txt')

for line_x in file_handle:
    line_y = line_x.rstrip()
    print(line_y.upper())