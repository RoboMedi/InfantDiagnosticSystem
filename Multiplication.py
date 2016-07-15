import string

class Multiplication:
    def __init__(self):
        self.result = 1
        self.isNumber = True

    #if you don't put 'self' as a parameter , 'self'-instance info goes into arg.
    def do(self, *arg):
        for x in arg:
            if type(x) is str:
                print "Cannot caluate character type"
                self.isNumber = False
                break
        if self.isNumber:
         if 0 in arg:
              print 0
         else:
            for x in arg:
                self.result *= x
            print self.result


cal = Multiplication()

cal.do(1,2,3,6)

