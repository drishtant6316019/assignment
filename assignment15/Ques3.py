''' Ques 3. Split the following irregular sentence into words
sentence = "A, most most lucky person; irregular_sentence"
desired_output = "A most most lucky person irregular sentence".'''


import re
irregular_sentence="A,most most lucky person;irregular_sentence"


p = re.compile(r"[^A-Za-z0-9]")
result=p.sub(" ",irregular_sentence)
print(result)