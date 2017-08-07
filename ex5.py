name='Zed A, Shaw'
age = 35 # not a lie
height_inches = 74 # inches
height = 2.54*height_inches
weight_lbs = 180 # lbs
weight = 0.45359237*weight_lbs # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "He's %f inches tall." % height
print "He's %G pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %i, %i, and %d I get %d." % (age, height, weight, age + height + weight)
