'''
This program demonstrates how to write to a new file.
'''
def main():
    with open('/Users/zhipengyan/Desktop/GOOGL.xlsx', 'a') as fp:
        fp.write('\n 2, 20000, 0.025, 180'
                 '\n 2, 130000, 0.015, 120')


if __name__ == '__main__':
    main()