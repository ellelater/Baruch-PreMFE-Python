'''
This program is to create a list and print all numbers in the list.
'''

def main():
    #1.2.3 here is my code
    l = [i for i in range(1, 1001) if i % 2 == 0 ]
    for i in l[:-1]:
        print str(i) + ',',
    print l[-1]


    #1.2.4 here is my code
    l2 = [n for n in range(1000) if n % 2 == 1]
    for n in l2[:-1]:
        print str(n) + ',',
    print l2[-1]


    #1.2.5 here is my code
    lst = l + l2
    for i in lst[:-1]:
        print str(i) + ',',
    print lst[-1]


    #1.2.6 here is my code
    lst.reverse()
    for i in lst[:-1]:
        print str(i) + ',',
    print lst[-1]







###############
if __name__ == '__main__':
    main()