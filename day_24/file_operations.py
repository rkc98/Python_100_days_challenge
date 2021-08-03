# file=open("day_24/craete_file.txt","a")
# file2=open("readme.md")
# file.write("write some more")
# contents=file.read()
# contents2=file2.read()
# print(contents,contents2)

# file.close()
# file2.close()


with open("day_24/craete_file.txt","w") as file:
    file.write(" write some more code to make yourself more better")
    # print(file)
with open("day_24/craete_file.txt") as files:
    contents=files.read()
    print(contents)

