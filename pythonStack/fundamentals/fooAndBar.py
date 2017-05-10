def fooBar():
    for i in range (1,101):
        print i
        if Prime(i):
            print 'Foo'
        # elif Square(i):
        #     print 'Bar'
        # else:
        #     print 'FooBar'

def Prime(x):
    for i in range(2, x):
        if x%i == 0:
            return False
        return True

# def Square(x):
#     for i in range(2, (x/2)+1):
#         if i * i == x:
#             return True
#         return False
fooBar()
