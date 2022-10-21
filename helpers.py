import os

def MakeResultsDir(p=__file__):
    r = str()
    
    r = os.path.splitext(p)[0]
    try:
        os.makedirs(r)
    except FileExistsError:
        pass
    return r