'''
This program demonstrates how to join the list to create a pathname.
'''


def main():
    lst = ['C:', 'Users', 'Me', 'Desktop', 'MyTable.csv']
    # 4.1.3 a Join the list together to create a valid pathname.
    f = '\\'.join(lst)
    print f

    # 4.1.3 b Insert another folder into the list and join the resulting list to create a valid pathname.
    lst.insert(4, 'Course')
    print '\\'.join(lst)


if __name__ == '__main__':
    main()