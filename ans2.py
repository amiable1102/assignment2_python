def group(l, size):
    return [l[i:i+size] for i in range(0, len(l), size)]
 
 
if __name__ == '__main__':
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9]
    print(group(input_list,3))
