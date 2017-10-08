def main():
    dct = {'China': 1403500365, 'India': 1324171354, 'United States': 322179605,
           'Indonesia': 261115456, 'Brazil': 207652865, 'Pakistan': 193203476,
           'Nigeria	Africa': 185989640, 'Bangladesh': 162951560, 'Russia': 143964513,
           'Mexico': 127540423, 'Japan': 127748513, 'Ethiopia': 102403196}

    # 1.5.5 a
    while True:
        country = raw_input("Please type a country's name(0 for exit):")
        if country != '0':
            if country not in dct:
                print "Population for this country is not recorded."
                population = int(raw_input("Please insert its population:"))
                dct[country] = population
            else:
                print "The population for this country is:", dct[country]
            print ""  # to make console look better
        else:
            break

    # 1.5.5 b
    print "\n\n********** 1.5.5 b **********"
    print "The final population list is:"
    for country, population in dct.items():
        print country, "has population", population

    # 1.5.5 c1
    print "\n\n********** 1.5.5 c1 **********"
    print "The final population list sorted by country name is:"
    for country, population in sorted(dct.items()):
        print country, "has population", population

    # 1.5.5 c2
    print "\n\n********** 1.5.5 c2 **********"
    print "The final population list sorted by country population is:"
    temp_lst = sorted([(-v, k) for k, v in dct.items()])
    for population, country in temp_lst:
        print country, "has population", -population


if __name__ == '__main__':
    main()
