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
<note any discoveries you made here... no matter how small!>

QCC:
0. Java creating classes
1. file directories, and html pages
2. to the terminal?
3. location in memory?
4. unsure, but likely not since it just returns
5. java methods
 ...

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



