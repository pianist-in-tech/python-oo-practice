"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    #create a constructor for the class
    def __init__(self,start):
        self.start = start
        self.next_num = start
    #create a function that generates a number
    def generate(self):
        res = self.next_num
        self.next_num +=1
        return res
    
    #create a reset function
    def reset(self):
        self.next_num = self.start

    
    





