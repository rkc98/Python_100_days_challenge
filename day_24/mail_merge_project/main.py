#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("day_24/mail_merge_project/Input/letters/starting_letter.txt") as start_letter:
    letter_content=start_letter.read()
# print(letter_content)
# new_content=letter_content.replace("[name]","anuj")
# print(new_content)
with open("day_24/mail_merge_project/Input/Names/invited_names.txt") as names:
    names_list=names.readlines()
new_names_list=[]
for name in names_list:
    name_strip=name.strip('\n')
    new_names_list.append(name_strip)

print(new_names_list)

for name in new_names_list:
    with open(f"day_24/mail_merge_project/Output/Ready_to_send/{name}.txt","w") as write_letters:
        print(letter_content)
        new_content=letter_content.replace("[name]",name)
        write_letters.write(new_content)

    



