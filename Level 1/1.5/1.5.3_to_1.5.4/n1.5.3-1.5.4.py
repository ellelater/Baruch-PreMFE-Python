def main():
    # 1.5.3
    mortgages = [150, 23, 23, 160]
    unique_mortgages = list(set(mortgages))

    # 1.5.4
    mortgages = {10, 15, 30}
    # 1.5.4 a
    mortgages.add(5)
    # 1.5.4 b
    mortgages.remove(15)
    # 1.5.4 c
    # mortgages.remove(45)  # KeyError
    # To prevent the KeyError from happening:
    mortgages.discard(45)


if __name__ == '__main__':
    main()
