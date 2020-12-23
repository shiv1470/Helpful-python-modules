def writeInputIntList(l,file):
    file.write(str(len(l)))
    for i in range(len(l)):
        file.write(" "+str(l[i]))
    file.write("\n")
def writeInputStringList(l,file):
    file.write(str(len(l)))
    for i in range(len(l)):
        file.write(" "+l[i])
    file.write("\n")
def writeInputString(s,file):
    file.write(s+"\n")
def writeInputInt(i,file):
    file.write(str(i)+"\n")
def writeInputArrayArrayInt(Mat, file):
    n = len(Mat)
    m = len(Mat[0])
    file.write(str(n)+" "+str(m))
    for i in Mat:
        for x in i:
            file.write(" "+str(x))
    file.write("\n")
def writeInputCharList(l, file):
    file.write(len(l))
    for i in l:
        file.write(" "+i)
    file.write("\n")
def writeOutputInt(i, file):
    file.write(str(i)+"\n")
def writeOutputIntList(l, file):
    for i in l:
        file.write(str(i)+" ")
    file.write("\n")
def writeOutputStringList(l, file):
    for i in l:
        file.write(str(i)+" ")
    file.write("\n")
def writeOutputString(s, file):
    file.write(s+"\n")
def writeOutputCharList(l, file):
    for c in l:
        file.write(c+" ")
    file.write("\n")
def readInputInt(file):
    return int(file.readline())
def readInputIntList(file):
    return list(map(int, file.readline().split()))[1:]
def readInputArrayArrayInt(file):
    l = list(map(int, file.readline().split()))
    n, m = l[0], l[1]
    ans = []
    c=2
    for i in range(n):
        ans.append(l[c:c+m])
        c+=m
    return ans
def readInputString(file):
    return file.readline().trim()
def readInputStringList(file):
    return file.readline().split()[1:]