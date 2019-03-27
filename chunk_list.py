def split_list(lst, n):
    # Gets the number of elements in each 'chunk'
    size = round(len(lst)/n)
    print(size)
    # List comprehension - if len(list) = 5 and n = 3
    #   loops through to get all but the final chunk
    #   starting at 0 and incrementing i by 3 each time until the 4th element 
    #   gets a slice of the list from i to i+2
    chunk_list = [ lst [i:i+ size] for i in range(0, (n-1)*size, size)]

    # Appends final chunk from final element above to end of list
    chunk_list.append(lst[(n-1)*int(size):])
    return chunk_list   

lst = list(range(1,6))
n = 3
print(split_list(lst,n))

