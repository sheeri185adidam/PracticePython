def insertion_sort(input_array):
    size = len(input_array)

    for index in range(1, size):
        for j in range(index, 0, -1):
            if(input_array[j] >= input_array[j-1]):
                break
            else:
                tmp = input_array[j]
                input_array[j] = input_array[j-1]
                input_array[j-1] = tmp

def bubble_sort(input_array):
    size = len(input_array)
    sorted = False

    while not(sorted):
        sorted = True

        for i in range(1, size):
            if(input_array[i]<input_array[i-1]):
                tmp = input_array[i]
                input_array[i] = input_array[i-1]
                input_array[i-1] = tmp
                sorted = False

if __name__ == '__main__':
    input = [5,6,1,2,4,3,0]
    insertion_sort(input)
    print(input)           