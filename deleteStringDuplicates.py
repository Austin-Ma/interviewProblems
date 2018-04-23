test = "The quick brown fox jumped over the three lazy dogs"
#PRESERVE ORDER

def preserveOrderDuplicates(input):
    seen = set()



#DO NOT PRESERVE ORDER
def noOrderDuplicates(input):
    #Standardize upper and lower to prevent duplicates
    input = input.lower
    store = ""

    for i in set(input):
        store += i
    temp = list(store)
    temp.sort()
    return "".join(temp)

print(noOrderDuplicates(test))
