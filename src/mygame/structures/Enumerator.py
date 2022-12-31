class Enumerator :
    __counter = 0
    __label = None


    def __init__( self, number: int, data=None, label=None ) :
        self.number = number
        self.data = data
        self.label = label
        


    def __str__( self ) :
        return "[EnumObject(label:{}) : ( <number:{}> , <data:{}> ) ]".format(self.label,
            self.number, self.data)


    @staticmethod
    def reset( label: str = None ) :
        Enumerator.__label = label
        Enumerator.__counter += 1


    @staticmethod
    def next( data=None ) :
        Enumerator.__counter += 1
        return Enumerator(Enumerator.__counter, data, Enumerator.__label)
