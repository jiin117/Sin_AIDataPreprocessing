import cv2
import SelectSortClass as ss
noise_img = cv2.imread('salt-pepper-noise.jpg')
input_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
print(input_img[0:10, 0:10])
cv2.imshow('input_img', input_img)

filter = ss.MedianFilter(7, input_img) #filterer에 필터 사이즈를 넣으면 됨!
filter_img = filter.median_filter()
print(filter_img[0:10, 0:10])
# cv2.imwrite('filter_image_new1_7.jpg', filter_img)
cv2.imshow('filter_img', filter_img)
cv2.waitKey()