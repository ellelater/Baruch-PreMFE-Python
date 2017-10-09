'''
This program is to demonstrate taking input from the user.
'''

def main():
    #1.1.4 Here is my code
    var = input('Input:')

    #1.1.5 Here is my code
    print 'The type of your input is ', type(var)

    #1.1.6 Here is my code
    if type(var) == float or type(var) == int:
        print 'The inputted value is a number'
        if var>65:
            print 'The inputted number is greater than 65'
        elif 64<=var<=65:
            print 'The inputted number is between 64 and 65'
        else:
            print 'The inputted number is less than 64'
    elif type(var) == str:
        print 'The inputted value is a string'
    else:
        print 'The inputted value is neither a number nor a string'






#######################
if __name__ == '__main__':
    main()