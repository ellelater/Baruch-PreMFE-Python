'''
This program demonstrates how to extract filename and add folder in a Windows file-path.
'''


def main():
    f = 'C:\\Users\\Me\\Desktop\\MyTable.csv'
    # 4.1.2 a Extract the filename with extension from the path.
    print f.split('\\')[-1]

    # 4.1.2 b Extract the file extension only.
    print f[f.rfind('.'):]

    # 4.1.2 c Add another folder between 'Desktop' and the filename.
    l = f.split('\\')
    l.insert(4, 'Course')
    f = '\\'.join(l)
    print f


if __name__ == '__main__':
    main()
