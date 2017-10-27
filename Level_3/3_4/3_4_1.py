def main():
    with open("test.txt", 'w') as w:
        w.write('asdf')
    print w.closed


if __name__ == '__main__':
    main()
