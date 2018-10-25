#opening and writing to a file
    my_list = [i ** 2 for i in range(1, 11)]

    my_file = open("output.txt", "w")

    # Add your code below!
    for l in my_list:
    my_file.write(str(l)+ "\n")
    
    my_file.close()
# reading from a file
    my_file = open("output.txt", "r")
    print my_file.read()
    my_file.close()
# reading line by line
    my_file = open("text.txt", "r")
    print my_file.readline()
    print my_file.readline()
    print my_file.readline()
    my_file.close()
# buffering - you need to clsoe the file as it's sitting in buffer and not fully written
# getting python to open and close the file for you with "with and as"
    with open("text.txt", "w") as textfile:
        textfile.write("Success!")
