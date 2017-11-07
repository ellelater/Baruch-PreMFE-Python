import datetime


def main():
    # a
    year = input("Year:")
    month = input("Month:")
    day = input("Day:")
    hour = input("Hour:")
    minute = input("Minute:")
    second = input("Second:")
    microsecond = input("Microsecond:")
    # b
    t = datetime.datetime(year, month, day, hour, minute, second, microsecond)
    # c
    print "Year:", t.year
    print "Month:", t.month
    print "Day:", t.day
    print "Hour:", t.hour
    print "Minute:", t.minute
    print "Second:", t.day
    print "Microsecond", t.microsecond
    # d
    print t.strftime("%Y-%m-%d %H:%M:%S:%f")
    # e
    print t.strftime("%Y %B %d %I:%M:%S:%f %p")
    # f
    print datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S:%f")
    print datetime.datetime.today().strftime("%Y %B %d %I:%M:%S:%f %p")
    # g
    print datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S:%f")
    print datetime.datetime.utcnow().strftime("%Y %B %d %I:%M:%S:%f %p")


if __name__ == '__main__':
    main()
