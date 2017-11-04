'''
This program is to demonstrate string functions.
'''

s = '  The Python course is the best course that I have ever taken.   '

# 4.1.1 a Display the length of the string.
print 'The length of the string is {0}'.format(len(s))

# 4.1.1 b Find the index of the first 'o' in the string.
print "The index of the first 'o' in the string is {0}".format(s.find('o'))

# 4.1.1 c Trim off the leading spaces only.
print "To trim off the leading spaces only: {0}".format(s.lstrip())

# 4.1.1 d Trim off the trailing spaces only.
print "To trim off the trailing spaces only: {0}".format(s.rstrip())

# 4.1.1 e Trim off both the leading and trailing spaces.
ss = s.strip()

# 4.1.1 f Fully capitalize the string.
print "Fully capitalize the string: {0}".format(ss.upper())

# 4.1.1 g Fully lowercase the string.
print "Fully lowercase the string: {0}".format(ss.lower())

# 4.1.1 h Display the number of occurrence of the letter 'd' and of the work 'the'.
d = ss.find('d')
the = ss.find('the')
print "The number of occurrence of the letter 'd' is {0} and of the work 'the' is {1}".format(d, the)

# 4.1.1 i Display the first 15 characters of the string.
print "The first 15 characters of the string are {0}".format(ss[:15])

# 4.1.1 j Display the last 10 characters of the string.
print "The last 10 characters of the string are {0}".format(ss[-10:])

# 4.1.1 k Display characters 5-23 of the string.
print "Characters 5-23 of the string are {0}". format(ss[4:24])

# 4.1.1 l Find the index of the first occurrence of the word 'course'.
print "The index of the first occurrence of the word 'course' is {0}".format(ss.find('course'))

# 4.1.1 m Find the index of the second occurrence of the word 'course'.
first_course = ss.find('course')
print "The index of the second occurrence of the word 'course' is {0}".format(ss.find('course', first_course+1))

# 4.1.1 n Find the index of the second to last occurrence of the letter 't',
# between the 7th and 33rd characters in the string.
occ = []
for i in xrange(6, 33):  # find the 7th to 33rd characters
    if ss[i] == 't':  # use a loop to find the occurrence of 't'
        occ.append(i)
print "The indexes of the second to last occurrence of the letter 't' " \
      "between 7th and 33rd characters are {0}".format(occ[1:])

# 4.1.1 o Replace the period (.) with an exclamation point (!).
print ss.replace('.', '!')

# 4.1.1 p Replace all occurrences of the word 'course' with 'class'.
print ss.replace('course', 'class')


