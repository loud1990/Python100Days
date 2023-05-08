#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# create a list with all the names in it
with open("./Input/Names/invited_names.txt") as names_file:
    all_names = names_file.readlines()

# Open the file starting letter
with open("./Input/Letters/starting_letter.txt") as file:
    contents = file.read()
    for name in all_names:
        stripped_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
            print(new_letter)

# replace the [name] with each name in the invitednames file

# create a text file and copy each to readytosend folder

