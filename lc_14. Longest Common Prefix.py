lists = ["abrdfe", "abcd", "abcf"]
lslen = len(lists)
onelen = len(lists[0])
sortedwords = sorted(lists, key=len)
sortlen = len(sortedwords[0])

print('sort : ', sortedwords[0], sortlen)

oc = []
for s in range(lslen):
    os = list(lists[s])
    oc.append(os)
print(oc)

# for i in range(len(oc)):
#     for j in range(len(oc[i])):
#         print(oc[i][j], end=' ')
#     print()


oclen = len(oc)
alloc = []
for i in range(len(oc)):
    for j in range(sortlen):
        if (oc[i][j] == oc[i + 1][j] == oc[i + 2][j]):
            print('ok', oc[i][j], oc[i + 1][j], oc[i + 2][j])
            alloc.append(oc[i][j])
        else:
            break

    #         elif (oc[i][0] != oc[i+1][0] != oc[i+2][0]):
    #             break

    print(alloc)
    print(''.join(alloc))
