import pickle
import graphviz
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

from helpers import MakeResultsDir

maxError = 0.01

ResultsDir = MakeResultsDir(__file__)

def FindErrors(yp, y):
    err = 0
    for i in range(len(y)):
        if yp[i] != y[i]:
            err +=1
    return err

x = list()
y = list()
f = open('/home/dennis/Downloads/test_add.dat')
for l in f:
    d=l.split()
    x.append([int(d[0]), int(d[1]), int(d[2]), int(d[3])])
    y.append(int(d[4]))
f.close()

minWeightFractionLeaf = 0.01
err = 10

while err > maxError:
    minWeightFractionLeaf = minWeightFractionLeaf / 2
    clf = DecisionTreeClassifier(min_weight_fraction_leaf=minWeightFractionLeaf)
    clf.fit(x, y)
    yp = clf.predict(x)
    err = FindErrors(yp, y) / len(y)

print("Accuracy %f reached for minimum weight fraction leaf: %f" % (err, minWeightFractionLeaf))

"""
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("dt_mwfl")


s=pickle.dumps(clf)
ff=open("my_ai", "wb")
ff.write(s)
ff.close()
"""