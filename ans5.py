f = open(r'C:\Users\Aditi Jain\Desktop\test.txt')
print(f.read()) #prints the read data from the file

print(f.tell()) #tells current file position
f.close()
# writing in file
with open("test2.txt",'w',encoding = 'utf-8') as f2:
   f2.write("this is my first python file\n")
   f2.write("I am learning to write in a text file through python\n")
   f2.write("this is fun!\n")
f2.close()

# reading the whole file at once
f3 = open("test2.txt","r")
print(f3.read())
f3.close()

# using for loop to read each line seperately
with open("test2.txt", 'r', encoding = 'utf-8') as f4:
   for line in f4:
       print(line, end='')
f4.close()

# using readline to read each line
with open("test.txt", 'w', encoding = 'utf-8') as f5:
   f5.write("heya this is Aditi Jain!\n")
   f5.write("how are you?\n")
f5.close()
with open("test.txt", 'r', encoding='utf-8') as f6:
   print("\n")
   print(f6.readlines())
f6.close()

# using writelines to write in the text file

with open("test1.txt", 'w', encoding = 'utf-8') as f8:
   f8.writelines(["sky is blue\n", "I love pegions"])
f8.close()

with open("test1.txt", 'r', encoding = 'utf-8') as f9:
   print(f9.readlines())
f9.close()
