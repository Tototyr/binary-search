
def binarysearch(list, search, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if search == list[mid]:
            return mid
        elif search > list[mid]:
            return binarysearch(list, search, mid + 1, stop)
        else: search < list[mid]
        return binarysearch(list, search, start, mid -1)







list = [1, 3, 4, 5, 6, 7, 8, 9, 10]
search = 11
start = 0
stop = len(list)

x = binarysearch(list, search, start, stop)

if x == False:
    print("Number not found")
elif x > list:
    print("Number not found")
else:
    print("This number", search, "index", x)