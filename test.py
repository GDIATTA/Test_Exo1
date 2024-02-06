# sum.py
def add(x, y):
    return x + y
# test_sum.py
#from sum import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
