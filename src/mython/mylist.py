class mylist(list):
    def __init__(self,container=None):
        if container is None:
            super(mylist, self).__init__()
            return

        super(mylist, self).__init__(container)

    def copycat( self ):
        copycat = mylist(super(mylist, self).copy())
        return copycat


    def replace( self,index_:int,object_ ):
        self[index_] = object_

        return self

    def get_replaced( self,index_:int,object_ ):
        return self.copycat().replace(index_,object_)
