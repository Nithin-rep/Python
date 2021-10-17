# Formating using data type
print("entered value is %s and %s" % ("a stringer", "an arrow"))
print("My grades in 10th is %1.2f and in 12th is %1.2f" %(88.9645,90.3333))

# Formating using a comand of .format (Better way of formating)
value ="a string"
print("entered value is {}".format(value))

# formating and index positioning
tenth,twelve, be = 88.96,90.33,78.88
print("My grades in 10th, 12th and BE is {},{},{}".format(tenth,twelve,be))
print("My grades in 10th, 12th and BE is {2},{1},{0}".format(be,twelve,tenth))

# To reuse
print("My grades in 10th, 12th and BE is {score},{score},{score}".format(score = tenth))

# To get foramt using f
print(f"Entered value is {value!r}")