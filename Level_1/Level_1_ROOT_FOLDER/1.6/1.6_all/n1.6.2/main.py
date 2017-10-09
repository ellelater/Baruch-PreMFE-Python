"""
This program demonstrates the use of module imports.
"""


from students.male.profiles.print_profile import print_profile
from students import *


def main():
    print_profile()
    female.profile.print_profile()


if __name__ == '__main__':
    main()
