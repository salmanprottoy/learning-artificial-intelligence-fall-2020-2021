#mean, mode, median

List = [1, 4, 9, 16, 25, 36, 49, 64, 81, 16, 16]

#finding mean for the given list
def mean(List):
    s = 0
    for i in List:
        s += i
    meanValue = s / len(List)
    return meanValue

#finding mode for the given list
def mode(List):
    modeValue = max(List, key = List.count)
    return modeValue

#finding median for the given list
def median(List):
    List.sort()
    if len(List) % 2 == 0:
        median1 = List[int(len(List) / 2)]
        median2 = List[int(len(List) / 2 - 1)]
        medianValue = (median1 + median2) / 2
    else:
        medianValue = List[len(List) // 2]
    return medianValue

print(mean(List))
print(mode(List))
print(median(List))

# def modeMethod1(List):
#     keys = list(set(List))
#     modeDict = {i:0 for i in keys}
#     for i in range(len(List)):
#         if List[i] in keys:
#             modeDict[List[i]] = modeDict[List[i]] + 1

# def mode(List):
#     mode = None
#     for i in List:
#         mode = List.count(i)
#         if mode[i] > mode[i-1]
#             modeValue = mode[i]
#      #modeValue = max(mode)
#      return modeValue

# def median(List):
#     List.sort()
#     if (len(List) % 2 == 0):
#         mid = int(len(List)/2)
#     else:
#         mid = int(len(List)+1/2)
#     return mid
