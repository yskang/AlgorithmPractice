import sys

filename = ''
if len(sys.argv) > 1:
    filename = sys.argv[1]

if filename == '':
    filename = 'set1.in'

testInput = open(filename, 'r')
testOutput = open(filename.replace('in', 'out'), 'w')

numOfTest = int(testInput.readline().replace('\n', '').replace('\r', '').strip())

def getDistance(man, sts, energy):
    dists = []
    for st in sts:
        dist = abs(man[0] - st[0]) + abs(man[1] - st[1])
        if dist <= energy:
            dists.append(st)
    return dists


def didAllManLive(mans, sts, stCaps, energy):
    status = {}
    stMan = {}
    escMan = {}

    for st in sts:
        status[st] = []

    for man in mans:
        dists = []
        dists = getDistance(man, sts, energy)
        stMan[man] = dists

    safeMans = []
    count = 1
    while True:
        for man in mans:
            if len(stMan[man]) == count:
                for st in stMan[man]:
                    if stCaps[st] > 0:
                        stCaps[st] = stCaps[st] - 1
                        status[st].append(man)
                        safeMans.append(man)
                        break

        for man in safeMans:
            mans.remove(man)
        safeMans[:] = []

        haveRoom = False
        for cap in stCaps.values():
            if cap != 0:
                haveRoom = True

        if not haveRoom:
            if len(mans) == 0:
                return(1)
            else:
                return(0)
        count = count + 1
        if count > 100:
            if len(man) > 0:
                return(0)

 
for i in range(numOfTest):
    line = testInput.readline().replace('\n', '').replace('\r', '').strip()
    ins = line.split(' ')
    numOfMan = int(ins[0])
    numOfSt = int(ins[1])
    
    mans = []
    sts = []
    stCaps = {}
    energy = 0

    for j in range(numOfMan):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        point = (int(ins[0]), int(ins[1]))
        mans.append(point)
    
    for j in range(numOfSt):
        line = testInput.readline().replace('\n', '').replace('\r', '').strip()
        ins = line.split(' ')
        point = (int(ins[0]), int(ins[1]))
        sts.append(point)

    line = testInput.readline().replace('\n', '').replace('\r', '').strip()
    ins = line.split(' ')
    for i in range(numOfSt):
        stCaps[sts[i]] = int(ins[i])

    line = testInput.readline().replace('\n', '').replace('\r', '').strip()
    energy = int(line)

    if len(sys.argv) > 1:
        testOutput.write(str("%d\n" %didAllManLive(mans, sts, stCaps, energy)))
    else:
        print("%d" %didAllManLive(mans, sts, stCaps, energy))
