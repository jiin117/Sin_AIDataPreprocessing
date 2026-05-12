def select_sort(in_data):
    arr = in_data.copy()
    for row in range(3):
        for col in range(3):
            for row1 in range(3):
                for col1 in range(3):
                    if row1==row and col1>col and arr[row, col]>arr[row1, col1]:
                        temp = arr[row, col]
                        arr[row, col] = arr[row1, col1]
                        arr[row1, col1] = temp
                    elif row1>row and arr[row, col]>arr[row1, col1]:
                        temp = arr[row, col]
                        arr[row, col] = arr[row1, col1]
                        arr[row1, col1] = temp
    # print(arr)
    # value = arr[1,1]
    # print("-"*30)
    return arr[1, 1]

def median_filter(input_img):
    for row in range(input_img.shape[0]-2):
        for col in range(input_img.shape[1]-2):
            # value_2 = select_sort(input_img[row:(row+3), col:(col+3)])
            # input_img[row+1, col+1] = value_2
            input_img[row + 1, col + 1] = select_sort(input_img[row:(row + 3), col:(col + 3)])
            # print(input_img[0:4, 0:4])
            # print("="*30)
    return input_img

import cv2
noise_img = cv2.imread('../Data/salt-pepper-noise.jpg')
input_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
print(input_img[0:10, 0:10])
cv2.imshow('input_img', input_img)
cv2.imwrite('../input_image.jpg', input_img)
# print()
# print(input_img[1, 1])
# print(select_sort(input_img[0:3, 0:3]))

filter_img = median_filter(input_img)
# print(filter_img.shape)
# print(filter_img[0:10, 0:10])
# print(filter_img[1, 1])

# print(filter_img[0:3, 0:3])
cv2.imshow('filter_img', filter_img)
cv2.imwrite('../filter_image.jpg', filter_img)
cv2.waitKey()
