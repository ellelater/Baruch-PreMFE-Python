def main():
    usnames = {"JAMES", "JOHN", "ROBERT", "MICHAEL", "WILLIAM", "DAVID", "RICHARD",
               "CHARLES", "JOSEPH", "THOMAS", "CHRISTOPHER", "DANIEL", "PAUL",
               "MARK", "DONALD", "GEORGE", "KENNETH", "STEVEN", "EDWARD", "BRIA"}

    uknames = {"WILLIAM", "JOHN", "GEORGE", "THOMAS", "ARTHUR", "JAMES", "CHARLES",
               "FREDERICK", "ALBERT", "ERNEST", "ALFRED", "EDWARD", "JOSEPH",
               "HAROLD", "ROBERT", "FRANK", "HENRY", "HARRY", "WALTER", "REGINAL"}

    # 1.5.2 a
    for name in usnames.intersection(uknames):
        print name,
    print ""

    # 1.5.2 b
    for name in usnames - uknames:
        print name,
    print ""

    # 1.5.2 c
    for name in uknames - usnames:
        print name,


if __name__ == '__main__':
    main()
