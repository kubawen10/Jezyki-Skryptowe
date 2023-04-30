def mypred(x):
    return x>2

def forall(pred, iterable):
    return all([pred(element) for element in iterable])
print("\nforall tests:")
print(forall(mypred, [2,3,4,5,6,7,8]))
print(forall(mypred, [3,4,5,6,7,8]))


def exists(pred, iterable):
    return any([pred(element) for element in iterable])
print("\nexists tests:")
print(exists(mypred, [1,2,1,2,0,1]))
print(exists(mypred, [1,2,3,2,0,1]))

def atleast(n, pred, iterable):
    if n <= 0:
        return True
    
    if len(iterable) == 0:
        return False
    head, *tail = iterable
    return atleast(n-1, pred, tail) if pred(head) else atleast(n,pred, tail)
print("\natleast tests:")
print(atleast(0, mypred, [1,2,3,4]))
print(atleast(3, mypred, []))
print(atleast(3, mypred, [0,1,2,3,4,2]))
print(atleast(3, mypred, [0,1,2,3,4,5]))

def atmost(n, pred, iterable):
    if n < 0:
        return False
    
    if len(iterable) == 0 and n >= 0:
        return True
    
    head, *tail = iterable
    return atmost(n-1, pred, tail) if pred(head) else atmost(n,pred, tail)
print("\natmost tests:")
print(atmost(-1, mypred, [1,2,3]))
print(atmost(0, mypred, [1,2,1,2,1]))
print(atmost(3, mypred, [1,3,2,3,3]))
print(atmost(3, mypred, [1,3,3,3,3]))

