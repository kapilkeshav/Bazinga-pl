#Bazinga programming language compiler
import math as m
import shlex
#open files and store everything in list
main_f = open("test.baz","r")
lines = main_f.read()
prog = lines.splitlines()
main_f.close()
i=0
loopval=[]  #list of the line number of loop and number of times loop has to execute.
if_ctr = 0
prog = [i for i in prog if i != '']
#print(len(prog))
list_func = ["print","input","telldt","convi","convf"]
list_dt = ["int","float","string"]
symbolt = dict()

def dec_var(checker):
    if checker[1] == "int":
        symbolt[checker[2]] = [checker[1],0]
    if checker[1] == "float":
        symbolt[checker[2]] = [checker[1],0]
    if checker[1] == "string":
        symbolt[checker[2]] = [checker[1],0]
    

def inp(checker):
    if checker[2][0] == "#":
        if symbolt[checker[2][1]][0] == "int":
            temp = int(input("input "+checker[2][1]+":"))
            symbolt[checker[2][1]][1] = temp
        if symbolt[checker[2][1]][0] == "float":
            temp = float(input("input "+checker[2][1]+":"))
            symbolt[checker[2][1]][1] = temp
        if symbolt[checker[2][1]][0] == "string":
            temp = input("input "+checker[2][1]+":")
            symbolt[checker[2][1]][1] = temp

def tell_dt(checker):
    if checker[2][0]=='#':
        dt = symbolt[checker[2][1]][0]
        print("Data type is: "+dt)
    else:
        print("Data type is: string")

def prnt(checker):
    if checker[2][0] == "#":
        print(symbolt[checker[2][1]][1])
    else:
        checker[2] = checker[2].replace('"','')
        print(checker[2])

def cond_check(cond) -> bool:
    if len(cond) == 3:
        if checker[2][1] == '>':
            if symbolt[checker[2][0]][1] > symbolt[checker[2][2]][1]:
                return True
            else:
                return False
        if checker[2][1] == '<':
            if symbolt[checker[2][0]][1] < symbolt[checker[2][2]][1]:
                return True
            else:
                return False
    if len(checker[2]) == 4:
        if checker[2][1] == '>':
            if symbolt[checker[2][0]][1] < symbolt[checker[2][2]][1]:
                return True
            else:
                return False
        if checker[2][1] == '<':
            if symbolt[checker[2][0]][1] < symbolt[checker[2][2]][1]:
                return True
            else:
                return False
        if checker[2][1] == '=':
            if symbolt[checker[2][0]][1] < symbolt[checker[2][2]][1]:
                return True
            else:
                return False
            
def sine(checker):
    x=m.radians(float(checker[2]))
    result = 0
    sign = 1
    for i in range(1,50,2):
        term = (sign)*(x**i)/m.factorial(i)
        result+=term
        sign*=-1
    return result

def cosine(checker):
    x=m.radians(float(checker[2]))
    result = 0.0
    sign = 1.0
    for n in range(20):
        term = sign * (x**(2*n)) / m.factorial(2*n)
        result += term
        sign *= -1.0
    return result

def arcsin(checker):
    x = m.radians(float(checker[2]))
    if x > 1 or x < -1:
        return None
    else:
        sum_ = x
        term = x
        n = 1
        while n <= 100:
            term *= ((2*n-1)**2 * x**2) / ((2*n)*(2*n+1))
            sum_ += term
            n += 1
        return sum_

while i<len(prog):
    checker = shlex.split(prog[i],posix=False)
    if checker[0] == "keshav":
        if checker[1] == "int" or checker[1] == "float" or checker[1] == "string":
            dec_var(checker)
            i+=1
        if checker[1] == "input":
            inp(checker)
            i+=1
        if checker[1] == "print":
            prnt(checker)
            i+=1
        if checker[1] == "telldt":
            tell_dt(checker)
            i+=1
        if checker[1] == 'if':                        
            sol = cond_check(checker[2])
            if sol == True:
                i=i+1
            else:
                temp = prog.index('endif')
                if 'else' in prog[i:temp]:
                    temp = prog.index('else')
                    i=temp+1
                    prog[temp] = '`'

        if checker[1] == 'loop':
            loopval=[i,int(checker[2])]
            i+=1

        if checker[1] == 'sine':
            res = sine(checker)
            if len(checker) == 3:
                print(res)
            else:
                if  checker[3][0]=='#':
                    if symbolt[checker[3][1]][0] == "int":
                        symbolt[checker[3][1]][1] = int(res)
                    if symbolt[checker[3][1]][0] == "float":
                        symbolt[checker[3][1]][1] = float(res)
            i+=1
        
        if checker[1] == 'cosine':
            res = cosine(checker)
            if len(checker) == 3:
                print(res)
            else:
                if  checker[3][0]=='#':
                    if symbolt[checker[3][1]][0] == "int":
                        symbolt[checker[3][1]][1] = int(res)
                    if symbolt[checker[3][1]][0] == "float":
                        symbolt[checker[3][1]][1] = float(res)
            i+=1

        if checker[1] == 'tan':
            num = sine(checker)
            den = cosine(checker)
            if len(checker) == 3:
                print(num/den)
            else:
                if  checker[3][0]=='#':
                    if symbolt[checker[3][1]][0] == "int":
                        symbolt[checker[3][1]][1] = int(num/den)
                    if symbolt[checker[3][1]][0] == "float":
                        symbolt[checker[3][1]][1] = float(num/den)
            i+=1

        if checker[1] == 'cosec':
            res = 1/(sine(checker))
            if len(checker) == 3:
                print(res)
            else:
                if  checker[3][0]=='#':
                    if symbolt[checker[3][1]][0] == "int":
                        symbolt[checker[3][1]][1] = int(res)
                    if symbolt[checker[3][1]][0] == "float":
                        symbolt[checker[3][1]][1] = float(res)
            i+=1
        
        if checker[1] == 'sec':
            res = 1/(cosine(checker))
            if len(checker) == 3:
                print(res)
            else:
                if  checker[3][0]=='#':
                    if symbolt[checker[3][1]][0] == "int":
                        symbolt[checker[3][1]][1] = int(res)
                    if symbolt[checker[3][1]][0] == "float":
                        symbolt[checker[3][1]][1] = float(res)
            i+=1
        
        if checker[1] == 'cot':
            num = sine(checker)
            den = cosine(checker)
            if len(checker) == 3:
                print(1/(num/den))
            else:
                if  checker[3][0]=='#':
                    if symbolt[checker[3][1]][0] == "int":
                        symbolt[checker[3][1]][1] = int(1/(num/den))
                    if symbolt[checker[3][1]][0] == "float":
                        symbolt[checker[3][1]][1] = float(1/(num/den))
            i+=1
        if checker[1] == 'arcsin':
            res = arcsin(checker)
            if len(checker) == 3:
                if res is not None:
                    print(res)
                else:
                    print("Not in range")
            else:
                if res is not None:
                    if checker[3][0]=='#':
                        if symbolt[checker[3][1]][0] == "int":
                            symbolt[checker[3][1]][1] = int(res)
                        if symbolt[checker[3][1]][0] == "float":
                            symbolt[checker[3][1]][1] = float(res)
                else:
                    print("out of range")
            i+=1

                 
    if checker[0] == 'endloop':
        if loopval[1]==1:
            i+=1
        else:
            i=loopval[0]+1
            loopval[1]=loopval[1]-1
    if checker[0] == 'endif':
        prog[i] = '~'
        i+=1
        
    if checker[0] == 'else':
        temp = prog.index('endif')
        prog[i] = '`'
        i = temp

    
    #Expression check
    if "=" in checker[0]:
        var = prog[i][0]
        keys = list(symbolt.keys())
        temp_stack = []
        op = ""
        for j in range(1,len(prog[i])):
            if prog[i][j] in keys:
                temp = prog[i][j]
                temp_stack.append(symbolt[temp][1])
            else:
                op = prog[i][j]
        if op == "+":
            fin = temp_stack[0]+temp_stack[1]
            symbolt[var][1]=fin
            i+=1
        if op == "-":
            fin = temp_stack[0]-temp_stack[1]
            symbolt[var][1]=fin
            i+=1
        if op == "/":
            fin = temp_stack[0]/temp_stack[1]
            symbolt[var][1]=fin
            i+=1
        if op == "*":
            fin = temp_stack[0]*temp_stack[1]
            symbolt[var][1]=fin
            i+=1