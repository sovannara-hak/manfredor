
class Rules(object):
    def __init__(self, rules_file_path=None):
        self.rules = {}
        self.path = rules_file_path

    def loadRules(self, rules_file_path):
        f = open(rules_file_path, 'r')
        for linestr in f:
            tok = linestr.split(" = ")
            if len(tok) == 2:
                self.rules[tok[0]] = float(tok[1])

    def dumpRules(self, rules_file_path):
        f = open(rules_file_path, 'w')
        for key in self.rules:
            linestr = key+" = "+str(self.rules[key])
            f.write(linestr+"\n")

    def addRule(self, tag, score):
        if tag in self.rules: 
            print "Rewriting rule "+tag+" = "+str(self.rules[tag])+" to "
            print tag+" = "+str(score)
        self.rules[tag] = score

