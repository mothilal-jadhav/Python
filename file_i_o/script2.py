# previously on script.py we opned and closed the file but we can just open the file without closing it as well

with open('text.txt') as file:
    texxt = file.read()
    print(texxt)

'''
output :
Hi, my name is mothilal jadhav

long ago there was a king who was irresponsible and careless
'''

# i can read and write as well 

# with open('text.txt', mode = 'w') as my_file:
#     texxt = my_file.write('hi, my name is Virat Kohli')
#     print(texxt)

'''
output :
Hi, my name is mothilal jadhav

long ago there was a king who was irresponsible and careless
26
'''
# but this changes the text file as 'hi, my name is Virat Kohli'

'''
after commenting out write function part and reading the line we get the output as :
hi, my name is Virat Kohli
26

because of the change in text file
'''

# lets do read and write, mode = 'r+'

# with open('text.txt', mode='r+') as new_file:
#     texxt = new_file.write('bye')
#     print(texxt)

# with open('text.txt') as file:
#     texxt = file.read()
#     print(texxt)

'''
output is :
hi, my name is Virat Kohli
3
bye my name is Virat Kohli

hence it is not completely changing the matter of text instead overwrting from the start of the string, hi, is replaced with bye
'''


# lets append

with open('text.txt', mode='a') as new_file:
    texxt = new_file.write(' hey, i am not leaving ')
    print(texxt)

with open('text.txt') as file:
    texxt = file.read()
    print(texxt)

'''
output is :
bye my name is Virat Kohli
23
bye my name is Virat Kohli hey, i am not leaving 
'''

# i can even create a new txt file and write the content in it

with open('new_text.txt', mode = 'w') as new_file:
    print(new_file.write('welcome to new_file'))

with open('new_text.txt') as file:
    texxt = file.read()
    print(texxt)

'''
output: 

ye my name is Virat Kohli hey, i am not leaving 
23
bye my name is Virat Kohli hey, i am not leaving  hey, i am not leaving 
19
welcome to new_file
'''