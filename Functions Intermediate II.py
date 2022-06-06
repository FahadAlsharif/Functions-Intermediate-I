x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15

students[0]['last_name']= 'Bryant'

sports_directory['soccer'][0]='Andres'

z[0]['y']=30

#2-----------------------------------------------------------------------------------------
students2 = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students2):
    p = len(students2)
    for x in range(p):
        print("first_name -",students2[x]['first_name'],", last_name -",students2[x]['last_name'])

#3--------------------------------------------------------------------------------------------------------------

iterateDictionary(students2)

def iterateDictionary(students2):
    p = len(students2)
    for x in range(p):
        print(students2[x]['first_name'])

iterateDictionary(students2)


def iterateDictionary2(students2):
    p = len(students2)
    for x in range(p):
        print(students2[x]['last_name'])

iterateDictionary2(students2)

#4------------------------------------------------------------------------
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(_dict):
    for x in _dict:
        print(len(_dict[x]),x.upper())
        for i in _dict[x]:
            print(i)
        print("")

printInfo(dojo)
