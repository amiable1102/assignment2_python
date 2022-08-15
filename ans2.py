// iterative long solution
def group(arr,size):
    ans = []
    list1 = []
    i =0
    while i<len(arr):
        if(i%size<size):
            list1.append(arr[i])
            i+=1
        if(i%size == 0):
            ans.append(list1)
            list1 =[]
    if list1:
        ans.append(list1)
    return ans
 
if __name__ == '__main__':
    inlis = [1,2,3,4,5,6,7,8,9]
    print(group(inlis,3))

    
 def group(l, size):
    return [l[i:i+size] for i in range(0, len(l), size)]
 
 
if __name__ == '__main__':
    input_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9]
    print(group(input_list,3))

