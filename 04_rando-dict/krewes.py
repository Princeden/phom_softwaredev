"""
Princeden Hom
Sizzle
SoftDev
K04 -- Python dictionairies and random selection
2024-09-15
time spent: .1
"""
import random
krewes = {
           4: [ 
		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
		],
           5: [ 
                'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
                'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
                'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
                'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN' 
              ]
         }
devo_period = random.randint(4, 5)
print(krewes[devo_period][random.randint(0, len(krewes[devo_period]) - 1)])
print(1 / (len(krewes[4]) + len(krewes[5])))
## runs the code n times then returns the frequency of each name as a percentage
def validate(n):
    devo_p = {}
    for n in range (0, n):
        devo_period = random.randint(4, 5)
        devo = krewes[devo_period][random.randint(0, len(krewes[devo_period]) - 1)]
        if devo in devo_p.keys():
            devo_p[devo] += 1
        else:
            devo_p[devo] = 0
    for devo in devo_p.keys():
        devo_p[devo] = devo_p[devo] / n
        print(str(devo) + ": " + str(devo_p[devo]))
validate(1000000)