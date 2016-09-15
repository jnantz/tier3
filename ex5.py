# -*- coding: utf-8 -*-


name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %r centimeters tall." % (height * 2.54)
print "He's %r kilograms heavy." % (weight /2.2)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)













# inches = 19
# centimeters = inches * 2.54
# print "%r inches equals %r centimeters." % (inches, centimeters)
#
#
# pounds = 180
# kilos = pounds /2.2
# print "%r pounds equals %r kilos." % (pounds, kilos)