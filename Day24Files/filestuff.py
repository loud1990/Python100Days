# mode "a" for append "w" for write, if you open a file that doesn't exist in write mode, it will create it

'''with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
'''

with open("my_file.txt", mode="") as file:
    file.write("New text")
