def extsort(lis):
    i =0
    while i<len(lis):
        lis[i] = lis[i].split('.')
        i+=1
    lis.sort(key =lambda lis: lis[1])
    i=0
    while i<len(lis):
        lis[i] = ".".join(lis[i])
        i+=1
        
    return lis
if __name__ == '__main__':
    print (extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
