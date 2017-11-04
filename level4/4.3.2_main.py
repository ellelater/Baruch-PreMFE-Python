'''
This program searches entire computer for all files of extension py using os.walk
'''
import os


def main():
    for root, dirs, files in os.walk('/Users'):
        for file in files:
            if file.endswith('.py'):  # find the files ending with .py
                print (os.path.join(root, file))


if __name__ == '__main__':
    main()