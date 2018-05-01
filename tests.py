from leetspeak import translate, substitute

input = "s"
ouput = "5"
assert substitute(input) == ouput, "character should have been substituted"

input = "elite speak"
ouput = "3L173 5P34K"
assert translate(input) == ouput, "phrase should have been translated"
