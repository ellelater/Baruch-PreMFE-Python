'''
This program is to take two inputs from user using raw_input.
'''

def main():
    height = raw_input('Height:')
    base = raw_input('Base:')
    height = float(height)
    base = float(base)

    if height <= 0 or base <= 0:
        print 'Please input positive numbers'
    else:
        print 'The area of the triangle is', 0.5*base*height


############################
if __name__ == '__main__':
        main()