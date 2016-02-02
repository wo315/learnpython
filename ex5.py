my_name = 'Wang Yang'
my_age = 35
my_height = 174
my_weight = 77
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %r." % my_name
print "He's %i mm tall." % my_height
print "He's %i kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %i, %i, and %d I get %d." % (my_age, my_height, my_weight, 
my_age + my_height + my_weight)
