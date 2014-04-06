import manfredor
import IPython

manf = manfredor.Manfredor()
manf.loadRules("../src/data/rules.txt")

a0 = manfredor.ManfObject("bla0", ["t1", "t2"])
a1 = manfredor.ManfObject("bla1", ["t1", "t4", "t2"])
a2 = manfredor.ManfObject("bla2", ["t1", "t2"])
a3 = manfredor.ManfObject("bla3", ["t1", "t2", "t3", "t4"])
a4 = manfredor.ManfObject("bla4", ["t5", "t4"])

list_obj = [a0, a1, a2, a3, a4]
manf.list_obj = list_obj

print ""
print "Classification: "
manf.cluster_init(3)
print manf.clustered_obj

a5 = manfredor.ManfObject("bla5", ["t3", "t4", "t1"])
manf.list_obj.append(a5)
manf.cluster()
print manf.clustered_obj
manf.printScore()

IPython.embed()
