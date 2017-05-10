students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def printNames(arr):
#     for i in range(0,len(arr)):
#         print arr[i]['first_name'], arr[i]['last_name']
#
# printNames(students)

# def printAll(users):
#     for x in users:
#         print x
#         for i in range(0, len(users[x])):
#             print i+1,'-',users[x][i]['first_name'].upper(), users[x][i]['last_name'].upper(),'-',len(users[x][i]['first_name']+users[x][i]['last_name'])
#
# printAll(users)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# def printStudents(arr):
#     for i in students:
#         print i['first_name'], i['last_name']

def printAll(users):
    for cohort in users:
        counter = 0
        print cohort
        for person in users[cohort]:
            counter += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(person['first_name']) + len(person['last_name'])
            print "{} - {} {} - {}".format(counter, person['first_name'], person['last_name'], length)

# printStudents(students)
printAll(users)
