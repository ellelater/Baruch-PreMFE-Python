'''
This program demonstrate how to read and append to a file.
'''


def main():
    os.mkdir('/Users/x.huang13/Desktop/Python')
    with open('Users/x.huang13/Desktop/Python/1.xlsx', 'w') as f:
        f.write('asdf')

    with open ('/Users/x.huang13/Desktop/Python/1.xlsx') as fp:  # read the file and display
        for line in fp:
            print line

    with open ('/Users/x.huang13/Desktop/Python/1.xlsx', 'a') as myfile:  # append to the file
        myfile.write('23, 300000, 0.015, 180')


if __name__ == '__main__':
    main()