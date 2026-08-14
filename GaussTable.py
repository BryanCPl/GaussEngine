


operation=['x','y','z','=']

def makeTable(table):
    return [separeateRow(table[0]),separeateRow(table[1]),separeateRow(table[2])]

def separeateRow(formula):
    try:
        row=[formula[0:formula.find('x')],
            formula[formula.find('x')+1:formula.find('y')],
            formula[formula.find('y')+1:formula.find('z')],
            formula[formula.find('=')+1:len(formula)]
            ]
        
        print(row)
        gaussRow=[]
        for n in row:
            posOrneg=1
            if len(n)>0 and n[0]=="-":
                posOrneg=-1


            if n=='' or n=="+" or n=='-':
                gaussRow.append(posOrneg*1)
            elif n.isdigit():
                gaussRow.append(int(n))
            elif n[1:len(n)].isdigit():
                gaussRow.append(posOrneg*int(n[1:len(n)]))
        return gaussRow
    except:
        return "La formula no es validad"


