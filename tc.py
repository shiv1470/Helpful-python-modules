from random import randint, shuffle, choices
def generateRandomTree(numOfNodes, Dense = False, Sparse = False): #generate a random tree of N-1 edges on Nodes from 1 to N.
    if Dense and Sparse:
        raise SyntaxError # "Tree cannot be Dense and Sparse."
    n = numOfNodes
    par = [None, None]
    for i in range(2,n+1):
        if Dense:
            par.append(randint(1, int(i**0.5)))
        elif Sparse:
            par.append(randint(i - int(i**0.5), i-1))
        else:
            par.append(randint(1,i-1))
    mp = [i+1 for i in range(n)]
    shuffle(mp)
    mp = [None] + mp
    edges = []
    for i in range(2,n+1):
        edges.append((mp[i], mp[par[i]]))
    shuffle(edges)
    return edges
def generateRandomString(length, alphabets):
    return "".join(choices(alphabets, k=length))
def generateRandomArray(length, lower, upper):
    return [randint(lower, upper) for i in range(length)]
def generateRandomMatrix(maxRows, maxCols, lower, upper, square = False):
    n=randint(1,maxRows)
    m=randint(1,maxCols)
    if square:
        maxn = min(maxRows, maxCols)
        n = randint(1,maxn)
        m = n
    ans = []
    for i in range(n):
        ans.append([randint(lower, upper) for i in range(m)])
    return ans
        
