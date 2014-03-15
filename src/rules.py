
class Rules(object):
    def __init__(self, rules_file_path=None):
        self.rules = {}
        self.path = rules_file_path

    def loadRules(self, rules_file_path):
        pass

    def dumpRules(self, rules_file_path):
        pass

    def addRule(self, tag, score):
        if tag in self.rules: 
            print "Rewriting rule "+tag+" = "+str(self.rules[tag])+" to "
            print tag+" = "+str(score)
        self.rules[tag] = score

