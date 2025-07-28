people = [
    {"name": "Ali", "age": 10, "score": 17},
    {"name": "Sara", "age": 15, "score": 8},
    {"name": "Reza", "age": 20, "score": 13},
    {"name": "Mina", "age": 30, "score": 19},
    {"name": "Omid", "age": 7, "score": 11}
]


newpeople=[{ 
    
 'name':p['name'],
 'age':p['age'],
 'score':p['score'],
 'group':'child'   if p['age']<12 else'teen ' if p['age']>12 and p['age']<18 else 'adult',
 'result':'قبول' if p['score']>9  else 'مردود'
 
                   
}for p in people ]





for item in newpeople:
    print(item)
    
