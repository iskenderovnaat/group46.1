def binary_search(list, num):
    first = 0
    last = len(list) - 1
    result_ok = False
    pos = -1

    while first <= last and not result_ok:
      middle = (first + last) // 2
      if list[middle] == num:
        result_ok = True
        pos = middle
      elif list[middle] < num:
        first = middle + 1
      else:
        last = middle - 1

    if result_ok:
      print("Элемент:",num, "Hайдено в индексе:", pos)
    else:
      print("Элемент не найден")
    return pos

list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
num = 13
binary_search(list, num)

