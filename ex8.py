formatter = "%r %r %r %r"
print "wangyang is %s." % "a good man"
print "wangyang is %r." % "a good man"
#1 2 3 4
print formatter % (1, 2, 3, 4)

#one two three four
print formatter % ("one", "two", "three", "four")

#True False False True
print formatter % (True, False, False, True)

#"%r %r %r %r"
print formatter % (formatter, formatter, formatter, formatter)


print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)