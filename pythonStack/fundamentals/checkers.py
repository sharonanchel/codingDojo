# make 8x8x8 board consisting of 8 stars and spaces.
# loop 8 times to build board.
num = 20
for x in range(0,num):
    if x % 2 == 0:      #even num
        temp = ""
    else:
        temp = " "
    for y in range(1,num):
        if y % 2 == 0:  #odd num
            temp += "*"
        else:
            temp += " "
    print temp
