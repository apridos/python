arr = [11, 3, 4, 33 ,12, 1, 9, 5]

def quickSort(arr):
    while len(arr) > 1:
        ptr_idx = -1
        pvt_idx = len(arr) - 1
        for i in range(0, pvt_idx):
            if arr[i] < arr[pvt_idx]:
                ptr_idx += 1
                swap(arr, i, ptr_idx)
                
        # Move pivot into correct position
        ptr_idx += 1
        swap(arr, pvt_idx, ptr_idx)
        return quickSort(arr[0:ptr_idx]) + [arr[ptr_idx]] + quickSort(arr[ptr_idx+1:])
    return arr

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

print(quickSort(arr))
