dict = {'micro':1.7,'act':2.0, 'total':2.16}
print(dict['micro'])

# To Manipulate assigned value
print(dict['micro'] - 0.2)

# To assign multiple values to one key value
multi = {'sem1':['systems','BandE','TPP'], 'sem2':['act','micro']}
print(multi['sem1'][0])

# To assign nested keya and value
multi = {'sem1':{'systems':2.7,'BandE':3.0,'TPP':2.0}, 'sem2':{'act':2.0,'micro':1.7}}
print(multi['sem1']['systems'])

# To pass values in a empty dictionary 
empty = {}
empty['first'] = 'given_name'
empty['second'] = 'sir_name'
print(empty['first'])

# To check keys, values, and items
print(empty.keys())
print(empty.values())
print(empty.items())


# Sets

# To avoid repetition and maintain uniqueness, we use sets
set = sorted(set([1,5,4,3,5,34,3,2,5]))
print(set)


