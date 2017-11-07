import datetime


def main():
    date = raw_input("Input date (in format %Y-%m-%d):")
    time = raw_input("Input time (in format %H:%M:%S):")
    t = datetime.datetime.strptime(date + ' ' + time, "%Y-%m-%d %H:%M:%S")
    delta = raw_input("Input delta time: (in format %H:%M:%S:%f)")
    sign = 1
    if delta[0] == '-':
        sign = -1
        delta = delta[1:]
    delta_t = datetime.datetime.strptime(delta, "%H:%M:%S:%f")
    d = datetime.timedelta(hours=delta_t.hour, minutes=delta_t.minute,
                           seconds=delta_t.second, microseconds=delta_t.microsecond)
    if sign > 0:
        res_t = t + d
    else:
        res_t = t - d
    print res_t.strftime("%Y-%m-%d %H:%M:%S:%f")


if __name__ == '__main__':
    main()