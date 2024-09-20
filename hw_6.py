def bubble_sort(lists):
    for i in range(len(lists)):
        for j in range(len(lists) - 1):
            if lists[j+1] < lists[j]:
                lists[j], lists[j+1] = lists[j+1], lists[j]

    return lists
print(bubble_sort([34,22,69,255,90,0,3]))
