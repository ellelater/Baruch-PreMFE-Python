'''
This program is to search the entire computer for all pdf files inside any directory that contains string 'gr' in its name.
'''

import os


def main():
    for root, dirs, files in os.walk('/Users'):
        if 'gr' in root:  # find the directories with string 'gr' in names
            for file in files:
                if file.endswith('.pdf'):
                    print os.path.join(os.path.join(root, *dirs), file)

if __name__ =='__main__':
    main()