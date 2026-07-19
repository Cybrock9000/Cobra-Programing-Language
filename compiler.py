#Cy 2026

#Interpreter language to make game programing easyer in python

import pygame as pg
import sys
import time
import math as M
import os



def main(programfilepath):
    
    pg.init()
    clock = pg.time.Clock()

    #var inits 
    vars = {}
    defs = {}
    looplines = []    
    programlines = []
    k=0
    j=0
    defline=0
    looppos = 0


    with open(programfilepath, "r") as program_file: #split lines
        programlines = [line.strip() for line in program_file.readlines()]
        
    while k < len(programlines): #load defs

        parts = programlines[k].split()

        if parts and parts[0] == "Def":
            name = parts[1]

            body = []

            k += 1

            while k < len(programlines):
                if programlines[k] == f"EndDef {name}":
                    break

                body.append(programlines[k])
                k += 1

            defs[name] = body

        k += 1
    k = 0
    
    while k < len(programlines):
        line = programlines[k]
        parts = line.split(" ")
        opcode = parts[0]
        
        
        

        if opcode == "" or opcode.startswith("#"):
            k += 1
            continue
        
        if opcode == "print": #imitates the classic python print
            text = " ".join(parts[1:])
            if text in vars:
                print(vars[text])
            else:
                print(text)
            
        if opcode == "log":
            with open('logoutput.txt', "a") as log: # log values in  a txt useful for watching multiple values
                if parts[1] in vars:
                    v1 = vars[parts[1]]
                else:
                    v1 = parts[1]
                    
                log.write(time.strftime('%H:%M:%S:') + ' ' + parts[1] + ' ' + v1)
                

        if opcode == "loop":
            looppos = k+1
            
        if programlines[k] == 'Endloop':
            loopendpos = k
            k = looppos

            continue
                    
        
        if opcode == "Break":
            k = loopendpos+1
        
        if opcode == "If":
            f = False
            if parts[1] == 'control':
                if event.type == pg.KEYDOWN:
                    if pg.key.name(event.key) == parts[2]:
                        f=True
                if not f:
                    while k < len(programlines) and programlines[k] != "EndIf":
                        k += 1
            else:
                left = vars.get(parts[1], parts[1])
                right = vars.get(parts[3], parts[3])

                
                
                    
                if parts[2] == ">":
                    f = float(left) > float(right)
                elif parts[2] == "=":
                    f = left == right
                elif parts[2] == "<":
                    f = float(left) < float(right)

                if not f:
                    while k < len(programlines) and programlines[k] != "EndIf":
                        k += 1
                    


                
        if opcode == "Var": # setting a var would look something like "Var i = 20"
            if parts[2] == "=":
                if parts[3] == "getTimeHMS":
                    v1 = time.strftime('%H:%M:%S')
                    
                elif parts[3] == "getTimeDHMS":
                    v1 = time.strftime('%d:%H:%M:%S')
                    
                elif parts[3] == "getTimeDHM":
                    v1 = time.strftime('%d:%H:%M')
                    
                elif parts[3] == "getTimeDH":
                    v1 = time.strftime('%d:%H')
                    
                elif parts[3] == "getTimeD": #D is for date aparently and d is day
                    v1 = time.strftime('%d')
                    
                elif parts[3] == "getTimeHM":
                    v1 = time.strftime('%H:%M')
                    
                elif parts[3] == "getTimeH":
                    v1 = time.strftime('%H')
                    
                elif parts[3] == "getTimeMS":
                    v1 = time.strftime('%M:%S')
                    
                elif parts[3] == "getTimeM":
                    v1 = time.strftime('%M')
                    
                elif parts[3] == "getTimeS":
                    v1 = time.strftime('%S')
                    
                else:
                    v1 = parts[3]
                    
                if parts[1] in vars:
                    vars[parts[1]] = v1
                else:
                    vars[str(parts[1])] = v1

                    
            elif parts[2] == "+":
                vars[parts[1]] = float(vars[parts[1]]) + float(parts[3])
                
            elif parts[2] == "-":
                vars[parts[1]] = float(vars[parts[1]]) - float(parts[3])
                
            elif parts[2] == "*":
                vars[parts[1]] = float(vars[parts[1]]) * float(parts[3])
                
            elif parts[2] == "/":
                vars[parts[1]] = float(vars[parts[1]]) / float(parts[3])
                
            elif parts[2] == "rnd":
                vars[parts[1]] = round(vars[parts[1]])
                
            elif parts[2] == "ceil":
                vars[parts[1]] =  M.ceil(vars[parts[1]])
                
            elif parts[2] == "flr":
                vars[parts[1]] =  M.floor(vars[parts[1]])
                
            elif parts[2] == "color":
                vars[parts[1]] =  tuple((int(parts[3]),int(parts[4]),int(parts[5])))
                
                
        #if opcode == "getTimeHMS":
        #    time.strftime('%H:%M:%S:')
        
        if opcode == "Def":
            pass
        if opcode == "EndDef":
            pass
        
        if opcode == "Screen":
            if parts[1] == "init": # Screen init w h
                window = pg.display.set_mode((int(parts[2]),int(parts[3])))
                
            if parts[1] == "caption": # Screen caption string
                pg.display.set_caption(parts[2])
                
            if parts[1] == "pos": # Screen pos x y
                os.environ['SDL_VIDEO_WINDOW_POS'] = (int(parts[2]),int(parts[3]))
                
            if parts[1] == "box": # Screen box color x y w h
                color = vars.get(parts[2], parts[2])
                pg.draw.rect(window, color, [parts[3], parts[4], parts[5], parts[6]], 0)
        
            if parts[1] == "fill": # Screen fill color
                color = vars.get(parts[2], parts[2])
                window.fill(color)

            if parts[1] == "update": # Screen update frames
                pg.display.flip()
                clock.tick(int(parts[2]))
                
            if parts[1] == "quitControl":
                events = pg.event.get()

                for event in events:
                    if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                        pg.quit()
                        return

                    #if event.type == pg.KEYDOWN and event.key == pg.K_a: #<<<save this for later
                    #    testS.play()
                    







                    
        
        if opcode == "DoDef":

            if parts[1] in defs:

                for defline in defs[parts[1]]:

                    parts = defline.split()
                    opcode = parts[0]
                    print('do this part')








        k+=1
    pg.quit()



if __name__ == "__main__":
    programfilepath = sys.argv[1]
    main(programfilepath)
