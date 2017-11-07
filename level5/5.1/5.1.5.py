import datetime


def main():
    date1 = raw_input("Input date 1 (in format %Y-%m-%d %H:%M:%S):")
    date2 = raw_input("Input date 2 (in format %Y-%m-%d %H:%M:%S):")
    date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    delta = date2 - date1
    # 1-6 displays
    print delta.days + delta.seconds / 86400.
    print delta.days * 24 + delta.seconds / 3600.
    print delta.days * 24 * 60 + delta.seconds / 60.
    print delta.seconds
    print delta.microseconds
    print "The difference is {} days, {} hours, {} minutes, {} seconds, and {} microseconds.".format(
        delta.days, delta.seconds / 3600, (delta.seconds % 3600)/60, delta.seconds % 60, delta.microseconds
    )


if __name__ == '__main__':
    main()
