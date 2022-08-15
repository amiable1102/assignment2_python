def lensort(lis):
    sorted_list = list(sorted(lis,key=len))
    return sorted_list
if __name__ == '__main__':
    lis = ['a','abc','sdfgre','ad']
    print(lensort(lis))
