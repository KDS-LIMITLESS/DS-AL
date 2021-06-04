def compareTriplets(a, b):
    
    result = []
    aliceScore =0
    bobScore = 0
    
    for Alice, Bob in zip(a, b):
        if Alice > Bob:
            aliceScore +=1
            continue
        if Bob > Alice:
            bobScore +=1
            continue
        if Alice == Bob:
            continue
    result.append(aliceScore)
    result.append(bobScore)
    return result

if __name__ == '__main__':
    a = list(map(int, input('::: ').strip().split()))
    b = list(map(int, input('::: ').strip().split()))
    print(compareTriplets(a, b))