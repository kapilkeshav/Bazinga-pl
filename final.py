#Bazinga programming language compiler

import shlex
#open files and store everything in list
main_f = open("main.baz","r")
lines = main_f.read()
prog = lines.splitlines()
main_f.close()
i=0
loopval=[]  #list of the line number of loop and number of times loop has to execute.

print(prog)
#print(len(prog))
list_func = ["print","input","telldt","convi","convf"]
list_dt = ["int","float","string"]
symbolt = dict()

def dec_var(checker):
    if checker[1] == "int":
        symbolt[checker[2]] = [checker[1],0]
    if checker[1] == "float":
        symbolt[checker[2]] = [checker[1],0]

def inp(checker):
    if checker[2][0] == "#":
        if symbolt[checker[2][1]][0] == "int":
            temp = int(input("input "+checker[2][1]+":"))
            symbolt[checker[2][1]][1] = temp
        if symbolt[checker[2][1]][0] == "float":
            temp = float(input("input "+checker[2][1]+":"))
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
        print(checker[2])

while i<len(prog):
    #print("iter: ",i)
    #print(prog)
    checker = shlex.split(prog[i],posix=False)
    if checker[0] == "keshav":
        if checker[1] == "int" or checker[1] == "float":
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
            _else = prog.index(':')
            _exit = prog.index(';')
            #print(_else,_exit)
            if len(checker[2]) == 3:
                if checker[2][1] == '>':
                    if symbolt[checker[2][0]] > symbolt[checker[2][2]]:
                        i=i+1
                    else:
                        temp = _else-i
                        i=i+temp+1
                        prog[_else]='~'
                        prog[_exit]='~'
                if checker[2][1] == '<':
                    if symbolt[checker[2][0]] < symbolt[checker[2][2]]:
                        i=i+1
                    else:
                        temp = _else-i
                        i=i+temp+1
                        prog[_else]='~'
                        prog[_exit]='~'
            if len(checker[2]) == 4:
                if checker[2][1] == '>':
                    if symbolt[checker[2][0]] >= symbolt[checker[2][3]]:
                        i=i+1
                    else:
                        temp = _else-i
                        i=i+temp+1
                        prog[_else]='~'
                        prog[_exit]='~'
                if checker[2][1] == '<':
                    if symbolt[checker[2][0]] <= symbolt[checker[2][3]]:
                        i=i+1
                    else:
                        temp = _else-i
                        i=i+temp+1
                        prog[_else]='~'
                        prog[_exit]='~'
                if checker[2][1] == '=':
                    if symbolt[checker[2][0]] == symbolt[checker[2][3]]:
                        i=i+1
                    else:
                        temp = _else-i
                        i=i+temp+1
                        prog[_else]='~'
                        prog[_exit]='~'

        if checker[1] == 'loop':
            loopval=[i,int(checker[2])]
            i+=1     

    if checker[0] == 'endloop':
        if loopval[1]==1:
            i+=1
        else:
            i=loopval[0]+1
            loopval[1]=loopval[1]-1

            
    if checker[0] == ':':
        _else = prog.index(':')
        _exit = prog.index(';')
        temp = _exit-i
        i=i+temp+1
        prog[_else]='~'
        prog[_exit]='~'
            
        
        
print(symbolt)
print(prog)
