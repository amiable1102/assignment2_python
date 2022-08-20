with open("test.txt",'r', encoding = 'utf-8') as f1:
   for line in f1:
       s = ''
       l = len(line)
       while(l>=1):
           s = s + line[l-1]
           l = l-1
       print(s)
f1.close()
