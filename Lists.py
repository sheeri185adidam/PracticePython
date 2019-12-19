def list_verify_index(list, index):
    if(index < 0 or index >= len(list)):
        return False
    return True

def list_print_element(list, index):
    if(not(list_verify_index(list, index))):
        raise IndexError('Invalid index')
    return list[index]

def list_slice(list,begin,end):
    if(not(list_verify_index(list, begin)) or not(list_verify_index(list, end))):
        raise IndexError('Invalid index')
    return list[begin:end]

def list_contains(list, element):
    return element in list

def list_append(list, new_element):
    list.append(new_element)

def list_extend(list, new_element):
    list.extend(new_element)

def list_pop(list, index=-1):
    list.pop(index)

def list_remove(list, element):
    list.remove(element)

if __name__ == '__main__':
    sample_list = ['manik','mary','james','gabe','ty']
    print(sample_list)
    print(list_print_element(sample_list, 3))
    print(list_slice(sample_list, 0, 3))
    print(list_contains(sample_list, "mary"))

    # Appending to a list
    list_append(sample_list, "sheeri")
    list_append(sample_list, ["jammu", "india"])
    print(sample_list)

    # Extending a list
    list_extend(sample_list, "tennant")
    list_extend(sample_list, ["wooster", "ohio"])
    print(sample_list)

    # Popping elements from a list
    list_pop(sample_list, -1)
    list_pop(sample_list, 0)
    print(sample_list)

    # Removing elements from a list
    list_remove(sample_list, "sheeri")
    print(sample_list)

