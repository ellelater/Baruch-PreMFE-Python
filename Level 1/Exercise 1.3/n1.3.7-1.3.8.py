"""
This program demonstrates the use of '**kwargs'
"""


# This is for 1.3.7
def print_profile(name, age, **kwargs):
    print "name", name
    print "age", age
    if 'state' in kwargs:
        print "state", kwargs['state']
    if 'height' in kwargs:
        print "height", kwargs['height']
    if 'weight' in kwargs:
        print "weight", kwargs['weight']


# This is for 1.3.8
def print_profile2(name, age, **kwargs):
    print "name", name
    print "age", age
    for k, v in kwargs.items():
        print k, v


if __name__ == '__main__':
    print_profile('Elle', 18, state='married', height=170)
    print_profile2('Bob', 20, state='single', hobby='Fishing')
