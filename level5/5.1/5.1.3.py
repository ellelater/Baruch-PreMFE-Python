import datetime


def main():
    # a
    time = raw_input("Input time (in format %Y %B %d %I:%M:%S:%f %p):")
    # b
    t = datetime.datetime.strptime(time, "%Y %B %d %I:%M:%S:%f %p")
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
