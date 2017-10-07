"""
This program demonstrates the use of '**kwargs'
"""


# This is for 1.3.7
def print_profile(name, age, **kwargs):
    lists = [name, age] + [v for k, v in kwargs.items() if k in ['state', 'height', 'weight']]
    for profile in zip(*lists):
        print profile


# This is for 1.3.8
def print_profile2(name, age, **kwargs):
    lists = [name, age] + kwargs.values()
    for profile in zip(*lists):
        print profile


if __name__ == '__main__':
    name = ['Elle', 'Bob']
    age = [18, 80]
    state = ['NJ', 'NY']
    height = [170, 180]
    hobby = ['F1', 'Computer Game']
    print_profile(name, age, state=state, height=height)
    print_profile2(name, age, state=state, hobby=hobby)
