#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

new_name_lst = []

with open('./Input/Names/invited_names.txt', 'r') as names:
    name_lst = names.readlines()

for name_index in range(0, len(name_lst)):
    name = name_lst[name_index]
    new_name_lst.append(name.strip('\n'))
    with open('./Input/Letters/starting_letter.txt', 'r') as letter:
        edit_letter = letter.read()
        new_letter = edit_letter.replace('[name]', new_name_lst[name_index])
        with open(f'./Output/ReadyToSend/{new_name_lst[name_index]}.txt', 'w') as ready_letter:
            ready_letter.write(new_letter)



#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp