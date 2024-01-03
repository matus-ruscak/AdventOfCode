original_list = [{0: '0', 1: '1', 2: '2'},
                 {0: '3', 1: '4', 2: '5'},
                 {0: '6', 1: '7', 2: '8'}]

print('Printing original dict')
for i in original_list:
    for key, value in i.items():
        print(value, end='')
    print('')
print('')

# should be
# 6 3 0
# 7 4 1
# 8 5 2

def transpose_dict_90_degrees(input_dict_list):
    y_range = len(input_dict_list)
    x_range = len(input_dict_list[0])

    transposed_dict_list = []

    for y in range(y_range):
        transposed_dict = {}
        for x in range(x_range):
            transposed_dict[x] = input_dict_list[(x_range-1)-x][y]
        transposed_dict_list.append(transposed_dict)

    print('Printing dict after transposing by 90 degrees')
    for i in transposed_dict_list:
        for key, value in i.items():
            print(value, end='')
        print('')
    print('')

    return transposed_dict_list


transpose_dict_90_degrees(original_list)