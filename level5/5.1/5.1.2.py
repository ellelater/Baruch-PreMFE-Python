import datetime


def main():
    # a
    time = raw_input("Input time (in format %Y-%m-%d %H:%M:%S:%f):")
    # b
    t = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S:%f")
    # c
    print "Year:", t.year
    print "Month:", t.month
    print "Day:", t.day
    print "Hour:", t.hour
    print "Minute:", t.minute
    print "Second:", t.day
    print "Microsecond", t.microsecond


if __name__ == '__main__':
    main()
