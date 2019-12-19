sample_tuple = ("manik", "mary", "sheeri", "tennant")

def tuple_contains(tuple, element):
    return element in tuple

if __name__ == '__main__':
    print(sample_tuple)
    print(tuple_contains(sample_tuple, "manik"))