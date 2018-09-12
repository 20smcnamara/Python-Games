lists = [[5,8,3,2,4,6,9,0,1,7],[8,2,3,4,5,7,1,6,4,0],[4,5,6,7,1,3,2,9,8,0],[6,7,3,4,1,9,0,2,5,8]]
indexes = [1,2,0,3]

def gen(num):
    global lists, indexes
    sum = -1
    var = 0
    while sum < 0 or num < sum:
        if var == 10:
            var = 0
        one = lists[0][var]
        two = lists[3][one]
        three = lists[2][two]
        four = lists[1][three]
        value = four
        if sum < 0:
            sum += value
        if num < sum:
            sum -= value
        lists = [lists[1], lists[3], lists[0], lists[2]]
        indexes = [indexes[2],indexes[1],indexes[0],indexes[3]]
        for l in lists:
            temp = l[0]
            for i in range(len(l)-1):
                l[i] = l[i+1]
            l[len(l)-1] = temp
        temp = lists[0]
        for l in range(len(lists)-1):
            lists[l] = lists[l+1]
        lists[len(lists)-1] = temp
        var += 1
    return sum


for x in range(100):
    print(gen(9))
