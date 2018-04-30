text = "elite speak"

original = "AEGIOST"
translation = "4361057"

text = text.upper()

new_string = ""
for c in text:
    if c in original:
        new_string = new_string + translation[original.index(c)]
    else:
        new_string = new_string + c

<<<<<<< Updated upstream
print(new_string)
=======

>>>>>>> Stashed changes
