

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#  % puts a variable in this string
y = "Those who know %s and those who %s."  % (binary, do_not)

print x
print y

# string is put inside a string
print "I said: %r." % x
# string is put inside a string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?!  %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

