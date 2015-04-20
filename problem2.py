import ann.net as net

TH = 0.5
nn = net.load('eiei.ann')

ys = []

fp = open('dataset.txt', 'r')
lines = fp.readlines();
lines = [[float(j) for j in i.split(',')] for i in lines]

for line in lines:
    inp = line[1:]
    nn.process(inp)
    ys.append(round(nn.getNode(2,0)))

clusters = []
centers = []

for y in ys:
    if len(centers)==0:
        clusters.append([y])
        centers.append(y)

    c = False
    i = 0
    for center in centers:
        if abs(center-y)<TH:
            c = True
            clusters[i].append(y)
            s = 0.0
            n = 0.0
            for node in clusters[i]:
                s+=node
                n+=1

            centers[i] = s/n
            break

        i+=1

    if not c:
        clusters.append([y])
        centers.append(y)

print centers
