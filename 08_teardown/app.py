"""
Princeden Hom
PD - Princeden Hom and Danny Huang (5)
SoftDev
K08 -- Tear Down!
2024-09-20
time spent: .1
"""
'''
DISCO:
- running the program creates a website on a local serveer
- we were wrong and no hablo queso appears on that website


QCC:
0. I believe I have seen similar syntax in java, when we assign function values to variables. Name would be a parameter.
1. I have seen it used in the terminal for file directories.
2. This would print in the shell below.
3. It may print the value of the variable name.
4. It may appear in the terminal/shell, as this is usually where returned values would go.
5. We have seen this be used in Java, specifically for inheritance. When the methods of one file are not in the main file, you must call "file name"."function name"

INVESTIGATIVE APPROACH:
- we tried to use our previous knowledge of java, and how return/ print functions worked when printing objects
as well as trying to figure out what app.route exactly did

'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



