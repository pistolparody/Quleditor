from forbiddenfruit import curse

def get_modified(self,index_,object_):
    self[index_] = object_
    return self

def ActivateCurse():
    curse(list,'get_modified',value=get_modified)









