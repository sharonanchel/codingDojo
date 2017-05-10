l = ['magical unicorns',19,'hello',98.98,'world']
# output mixed
# "magical unicorns hello world"
# sum
m = [2,3,1,7,4,12]
# output integer
# sum
n = ['magical','unicorns']
# out put string
# concat

# loop through each value
# find out data type
# add if int
# concat if string
temp = ""
num = 0
for i in n:
    if isinstance(i, int) or isinstance(i, float):
        num += i
    elif isinstance(i, str):
        temp += i + " "
if not n:
    print "Array is empty"
elif not temp:
    print "The array contains ints, floats, or both"
    print num
elif not num:
    print "The array contains strings"
    print temp
else:
    print "The array is of mixed type"
    print temp
    print num
