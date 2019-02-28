# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
num=array[0]
max_repetition = 1
for i in range(SIZE-1):
    repetition = 1
    for j in range(i+1,SIZE):
        if array[i] == array[j]:
            repetition += 1
    if repetition > max_repetition:
        max_repetition = repetition
        num=array[i]
if max_repetition > 1:
    print(max_repetition, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
