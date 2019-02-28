# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.

min_num = array[0]
for i in range(SIZE):
        if array[i] <min_num:
            min_num = array[i]

print (min_num)