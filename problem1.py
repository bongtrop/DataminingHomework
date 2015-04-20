import ann.net as net
import ann.bp as bp

def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]

# Read Dataset from file
fp = open('dataset.txt', 'r')
lines = fp.readlines();
lines = [[float(j) for j in i.split(',')] for i in lines]

# 3 flod cross validations
folds = chunks(lines, len(lines)/3)
valids = [[0,1,2],[1,2,0],[2,0,1]]

m = 0.0

for valid in valids:
    print "Fold ( "+str(valid[0]+1)+" )"
    tests = folds[valid[0]]
    trains = folds[valid[1]] + folds[valid[2]]

    # init mlp model and bp parameter
    nn = net.randNet([16,3,1])
    b = bp.bp(nn, 0.08, 0.08)

    # Train mlp model 200 epoch
    for i in range(0, 100):
        print "\tTrain "+str(i+1)+"/100 epoch"
        error = 0.0
        for t in trains:
            target = [t[0]]
            inp = t[1:]
            error = error + b.backPropagate(inp, target)

    # Test
    n = len(tests)
    c = 0.0
    for t in tests:
        target = t[0]
        inp = t[1:]
        nn.process(inp)
        # print str(target)+" <> "+str(round(nn.getNode(2,0)))
        if target==round(nn.getNode(2,0)):
            c+=1

    print "Correct Rate is "+str(c/n)
    if c/n>m:
        m = c/n
        gnn = nn

print "Save Best mlp model in file (eiei.ann)"
gnn.save('eiei.ann')
