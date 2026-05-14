def select_sort_list(in_data):
    arr = in_data.copy()
    arr_list = []
    for row in range(3):
        for col in range(3):
            value = arr[row, col]
            arr_list.append(value)
    print(arr_list)
    for j in range(8):
        temp = 255
        for i in range(j+1, 9):
            if arr_list[i] < temp:
                temp = arr_list[i]
        index = arr_list.index(temp)
        if arr_list[j] > temp:
            arr_list[index] = arr_list[j]
            arr_list[j] = temp
        print(index)
        print(arr_list)
        print("++++++++++++++++++++++++++++++")
    return arr_list

import cv2
img = cv2.imread('../input_image.jpg')
input_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(input_img[0:3, 0:3])
print(select_sort_list(input_img[0:3, 0:3]))
