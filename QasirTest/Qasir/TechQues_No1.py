objA = {'a': 10, 'b': 20, 'c': 30}
objB = {'a': 3, 'c': 6, 'd': 3}
objC = {'a': 1, 'b': 2, 'e': 3}
objD = {'c': 2, 'e': 2, 'f': 5}
objE = {'e': 1, 'f': 1}
newObj = {}
def combineData(objA, objB, *args):
    print('raw data = ', objA )
    print('raw data = ', objB)
    lenArgs = args.__len__()
    for key in list(objA.keys()):
        if key in list(objB.keys()):
            save = key
            total = objB[key] + objA[key]
            newObj[save] = total
        elif key not in list(objB.keys()) :
            save = key
            total = objA[save]
            newObj[save] = total
    for key in list(objB.keys()):
        if key not in list(objA.keys()):
            save = key
            total = objB[save]
            newObj[save] = total

    newObj[save] = total

    if lenArgs != 0:
        for a in range(lenArgs):
            print('raw data = ', args[a])
            for key in list(newObj.keys()):
                if key in list(args[a].keys()):
                    save = key
                    total = args[a][key] + newObj[key]
                    newObj[save] = total
                elif key not in list(args[a].keys()):
                    save = key
                    total = newObj[save]
                    newObj[save] = total
            for key in list(args[a].keys()):
                if key not in list(newObj.keys()):
                    save = key
                    total = args[a][save]
                    newObj[save] = total

    newObj[save] = total
    print('================================================')
    print('Combined Data = ', newObj)

combineData(objA, objB, objC, objD, objE)

