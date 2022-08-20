with open("test.txt",'r', encoding= 'utf-8') as f:
   for line in reversed(list(f)):
       print(line.rstrip())
f.close()
