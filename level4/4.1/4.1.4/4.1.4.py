def a():
    name = raw_input("Name:")
    age = input("Age:")
    country = raw_input("Country of Residence:")
    print name, 'is', age, 'years old and lives in', country


def b():
    name = raw_input("Name:")
    age = float(raw_input("Age:"))
    country = raw_input("Country of Residence:")
    print "{} is {:.1f} years old and lives in {}".format(name, age, country)


def new_a():
    name = raw_input("Name:")
    age = input("Age:")
    country = raw_input("Country of Residence:")
    print "{0} is {1} years old and lives in {2}".format(name, age, country)


def new_b():
    name = raw_input("Name:")
    age = float(raw_input("Age:"))
    country = raw_input("Country of Residence:")
    print "{name} is {age:.1f} years old and lives in {country}".format(name=name, age=age, country=country)


if __name__ == '__main__':
    new_b()
