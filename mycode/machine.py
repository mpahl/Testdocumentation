from random import randint
""" Das ist ein Text """

class Machine():
    """ Diese Klasse beinhaltet eine Maschine mit mehreren Eigenschaften """
    
    def __init__(self):
        self.seele = None
    
    def calculator(self, zahl1, zahl2, operator):
    	""" Es werden zwei gegebene Zahlen addiert """
        if operator == "+":
            x = zahl1 + zahl2
            return str(zahl1) + " + " + str(zahl2) + " = " + str(x)
        else:
            return "unknown operator"
            
    def speak(self, string):
    	""" Auch sprechen ist keine Schwierigkeit mehr """
        return "Ich sage: " + string
        
    def randomnumber(self):
    	""" Denke dir eine Zahl zwischen 0 und 100 aus """
        return randint(0, 100)
