dict1 = {"name":"maniksheeri", "company":"draftkings"}
dict2 = dict(name="manik", company="draftkings")
dict3 = dict(dict2, wife="mary", wifelastname="tennant")
dict4 = dict([('company','draftkings'),('location', 'boston')])
dict5 = dict([('company','draftkings'),('location', 'boston')], name="maniksheeri")
dict6 = dict.fromkeys(['surname', 'wifelastname'], 'sheeri')

if __name__ == '__main__':
    print(dict1)
    print(dict2)
    print(dict3)
    print(dict4)
    print(dict5)
    print(dict6)

    # Iterator
    for k in iter(dict6):
        print(k, dict6[k])
    
    # Keys View
    for k in dict5.keys():
        print(k)
    
    # Values View
    for v in dict5.values():
        print(v)
