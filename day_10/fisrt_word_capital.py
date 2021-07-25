

first_name=input("what is your first name ?\n")
last_name=input("what is your last name ?\n")

def format_name(first,last):
    if first=='' and last=='':
        return "check your inputs"
    f_name=first.title()
    l_name=last.title()
    return f_name+" "+l_name
fullname=format_name(first=first_name,last=last_name)
print(fullname)
    


