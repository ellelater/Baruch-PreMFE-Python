'''
This program is to display certain operations.
'''

def main():
    lst = [1, 0.5, 34, 65.6, 93, 43.5, 55, 34.666, 9, 32.54]
    # a. Display the first two numbers from the list.
    print lst[0:2]
    # b. Display the last two numbers.
    print lst[-2:]
    # c. Display all the numbers besides the last number, using a single print statement.
    print lst[:-1]
    # d. Display all the numbers besides the first number, using a single print statement.
    print lst[1:]
    # e. Display all the numbers besides the first two and last three numbers, using a single print.
    print lst[2:7]
    # f. Append one number to the end of the list.
    lst.append(4)
    # g. Append five numbers to the end of the list, using a single operation.
    lst2 = [3, 56, 32.3, 4, 10]
    lst.extend(lst2)
    # h. Insert one number right after the third number in the list.
    lst.insert(3, 12)
    # i. Modify the fourth-to-last number in the list.
    lst[3:]=[2, 334.4, 23, 34.4, 423, 86.44, 32, 121, 32.3, 4, 45, 5, 5]
    # j. Display the list backwards, using splicing.
    print lst[::-1]
    # k. Display every second item in the list.
    print lst[1::2]
    # l. Display every second item in the list, backwards.
    print lst[::-2]











####################
if __name__ == '__main__':
    main()