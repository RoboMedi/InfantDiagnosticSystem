import subtraction
import division

class calculator:

    def __init__(self):

        # Initialize classes
        sub = subtraction.substraction()
        div = division.division()

        # Substraction
        print "Substraction : %.1f" % sub.execute(1, 2)

        # Division
        print "Division : %.1f" % div.execute(1, 2)

# Run calculator class
calculator()
