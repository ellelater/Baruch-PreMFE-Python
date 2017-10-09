'''
This program is to take two inputs from user using input.
'''

def main():
    height = input('Height:')
    base = input('Base:')
    if type(height) != int and type(height) != float and type(base) != int and type(base) != float:
        print 'Please input numbers'
    elif height <= 0 or base <= 0:
        print 'Please input positive numbers'
    else:
        print 'The area of the triangle is:', 0.5*base*height




############################
if __name__ == '__main__':
        main()