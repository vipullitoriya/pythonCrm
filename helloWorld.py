## FlatList
ls = [[1,2,4,[5,[6,78],[35,[5,[6,78],8]]]]]
lsNew = []

def flatListHere(ls):
    for i in ls:
        if type(i) == list:
            flatListHere(i)
        else:
            lsNew.append(i)
flatListHere(ls)
print(lsNew)
#Manu Litoriya
print("Done")
