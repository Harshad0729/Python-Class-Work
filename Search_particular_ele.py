# WAP to search particular element in list

l = [89, 74, 34, 23, 11]
search_element = 34

for i in l:
    if i == search_element:
        print("Element found is", i)
        break
    else:
        print("Element not found")