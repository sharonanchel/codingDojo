def table(x):
    for row in range(1, x+1):
        if row == 1:
            string = 'x  '
            for column in range(row, (row*x)+1,row):
                string += str(column)+ '  '
            print string

        string = str(row) + '  '

        for column in range(row, (row*x)+1,row):
            string += str(column) + '  '
        print string
table(10)
