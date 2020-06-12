


def merge_sort(arr): 
    if len(arr) <= 1:
        return arr
    arrA = arr[:(len(arr) // 2) ]
    arrB = arr[(len(arr) //2):]

    return merge(merge_sort(arrA), merge_sort(arrB))


arr = [5, 3, 9 , 8]

merge_sort(arr)

