class MedianFilter:
    def __init__(self, filterer, input_img):
        self.filterer = filterer
        self.input_img = input_img
        self.outline = self.filterer - 1
        self.medianValue = int((self.filterer - 1) / 2)

    def select_sort_list(self, in_data):
        arr = in_data.copy()
        arr_list = []
        for row in range(self.filterer):
            for col in range(self.filterer):
                value = arr[row, col]
                arr_list.append(value)
        # print(arr_list)
        for i in range((self.filterer**2)-1):
            temp = arr_list[i]
            index = arr_list.index(temp)
            for j in range(i+1, (self.filterer**2)):
                if arr_list[j]<temp:
                    temp = arr_list[j]
                    index = j
            arr_list[index] = arr_list[i]
            arr_list[i] = temp
            # print(f"{i+1}번째: {arr_list}")
        value = arr_list[int((self.filterer**2)/2)]
        # print(arr_list)
        # print("===============================")
        return value

    def median_filter(self):
        filter_img = self.input_img.copy()
        for row in range(filter_img.shape[0] - self.outline):
            for col in range(filter_img.shape[1] - self.outline):
                filter_img[row + self.medianValue, col + self.medianValue] = (
                    self.select_sort_list(filter_img[row:(row + self.filterer), col:(col + self.filterer)]))
        return filter_img

