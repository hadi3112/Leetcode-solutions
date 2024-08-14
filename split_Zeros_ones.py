
def split_zeros_ones(arr):
    zeros =[]
    ones = []
    new_arr = []

    for elem in arr:
        if elem==0:
            zeros.append(elem)
        if elem==1:
            ones.append(elem)

    x= [new_arr.append(elem) for elem in zeros]
    y = [new_arr.append(elem) for elem in ones]
    return new_arr

arr  = [0,1,1,1,0,1]
print(split_zeros_ones(arr))  

