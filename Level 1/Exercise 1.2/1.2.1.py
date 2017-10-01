'''
This program is to ask for numbers and display the average of the numbers.
'''

def main():
    print 'Average Calculator\n'

    count = 0.0
    ttl = 0
    while(True):
        n = raw_input('Please enter a number (s to exit):')
        if n == 's':
            print 'Program Complete'
            break
        else:
            n = float(n)
            ttl += n
            count += 1.0
    print 'Average is', ttl/count


######################
if __name__ == '__main__':
    main()

