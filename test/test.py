import manfredor
import IPython

rules = manfredor.Rules()
rules.loadRules("../src/data/rules.txt")

a0 = manfredor.ManfObject()
a0.url = "bla0"
a0.tags = ["t1", "t2"]

a1 = manfredor.ManfObject()
a1.url = "bla1"
a1.tags = ["t1", "t4", "t2"]

a2 = manfredor.ManfObject()
a2.url = "bla2"
a2.tags = ["t1", "t2"]

a3 = manfredor.ManfObject()
a3.url = "bla3"
a3.tags = ["t1", "t2", "t3", "t4"]

a4 = manfredor.ManfObject()
a4.url = "bla4"
a4.tags = ["t5", "t4"]

list_obj = [a0, a1, a2, a3, a4]

for obj in list_obj:
  print "URL: "+obj.url, " Score: ", obj.computeScore(rules)

print ""
print "Classification: "
print manfredor.manfredor(list_obj, rules, 3)

IPython.embed()
