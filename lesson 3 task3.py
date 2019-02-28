# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.min_num=0
max_num=0
for i in range(SIZE):
    if array[i] <array [min_num]:
        min_num =i
    elif array[i] >max_num:
        max_num = i
        print((max_num),":",array[max_num], (min_num),":",array[min_num])
        new_array=array
        new_array[min_num],new_array[max_num]=new_array[max_num],new_array[min_num]
        print(new_array)