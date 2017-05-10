str = "It's thanksgiving day. it's my birthday,too!"
my_list = ["It's", 'thanksgiving', 'day', "it's", 'my', 'birthday', 'too!']
print my_list[2]
string = "It's thanksgiving month. it's my birthday,too!"


x = [2,54,-2,7,12,98]
print x
print max(x)
print min(x)

x = ['hello',2,54,-2,7,12,98,"world"]
print x[0],x[7]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[0:len(x/2)]
sec_list = x[len(x)/2:len(x)]
print "first_list", first_list
print "sec_list", sec_list
sec_list.insert(0,first_list)
print sec_list
