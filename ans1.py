def duplicate(input_list):
    return list(set([x for x in input_list if input_list.count(x) > 1]))
 
if __name__ == '__main__':
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    print(duplicate(input_list))
