#Cy 2026

#Interpreter language to make game programing easyer in python

import pygame as pg
import sys
import time
import math as M
import os
from CybrocksLibrary import *
from colorama import Fore, Back, Style,init
import random as R



def main(programfilepath):
    symbol = r"""
                    ........
        :=====- .-########::...
    ........-:.-.::-----:.=-====-:.......
    :-.=-.--------==...:..++++++++++=+++-:
    :-.--=-:--:-=-----:#*++======%@@%===++-.
    :-.#=.=+.-*:.===#*+==========%..%=====++:.
    --..:*:.*=.-=#*+====+*###+===%%@%======+-.
    :-.#+.=+.:=#+=====+*+....++============+-.
    :-..:+:.=#+=====++#..===-==+*++#%%+==*%%=.
    .:=++*:.=======+==.=.      ..:-#.-@++@..@.
    -=..=-:*======+..-           :@..%:.=..*.
    .=::.-=+======+=:            .*..=   +=
    .-.:.-=+======*=.
    --.:=+======*=.
        -=#+=======*=.
        .-+========+=.
        ..=========+=:.                         ...
        .-+=======++:                         .-.
        .-*+========-:.                    ..:...
        .:-*#*+====++=:.               ..:=#:.
            .-..#+=======.            ..-=##-:.
            -=.+*+====+-:..........-+###=:.
                =..####+++********#####+.-.
                .=....:+++++++++++.....-.
                    :--=:::::::::::.=---.
                        .:::::-:::-
    """

                                                   
    version = 'Beta V1 7/21/2026'
    
    pg.init()
    pg.mixer.init()
    init(autoreset=True)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLACK + Back.BLUE + f'Cobra Programing Language {version} By Cy')
    print(Fore.BLUE + symbol)
    clock = pg.time.Clock()

    #var inits 
    vars = {}
    lists = {}
    sounds = {}
    programlines = []
    DebugInfo = False
    watching = False
    waiting = False
    k=0
    b=False
    d=0
    s=0
    looppos = 0
    FPSEnabled = False
    caption = ''
    watchingvar = []
    


    with open(programfilepath, "r") as program_file: #split lines
        programlines = [line.strip() for line in program_file.readlines()]
        

    
    while k < len(programlines):
        line = programlines[k]
        parts = line.split(" ")
        opcode = parts[0]
        

        if DebugInfo:
            if d >= 60:
                d = 0
                print(Fore.BLUE + str(round(clock.get_fps())) + '       ' + Fore.RED + str(time.strftime('%H:%M:%S')) + '       ' + Fore.GREEN + str(opcode) + '       ' + Fore.CYAN + str(k))
                Fore.RESET
            else:
                d += 1
                
        if watching == True:
            if d >= 60:
                d = 0
                for i in range(len(watchingvar)):
                    print(str(watchingvar[i]) + ': ' + str(vars[watchingvar[i]]))
            else:
                d += 1
                
        if s > 0:
            s-=1
            
        

        if opcode == "" or opcode.startswith("#"):
            k += 1
            continue
        
        elif opcode == "Print": #imitates the classic python print
            text = " ".join(parts[1:])
            if text in vars:
                print(vars[text])
            else:
                print(text)
            
        elif opcode == "Log": # log values in  a txt useful for watching multiple values
            if parts[1] in vars:
                v1 = vars[parts[1]]
            else:
                v1 = parts[1]
                    
            log.write(f"{time.strftime('%H:%M:%S')} {parts[1]} {v1}\n")
                

        elif opcode == "DebugInfo": # really useful (hopefully)
            if parts[1] == 'T':
                log = open("logoutput.txt", "a")
                DebugInfo = True
                watching = False
            else:
                DebugInfo = False

        elif opcode == "Watch": # watch a vars value
            if parts[1] == 'T':
                DebugInfo = False
                watching = True
                watchingvar.append(parts[2])
            else:
                watching = False
                

        elif opcode == "Loop":
            looppos = k+1
            
        elif programlines[k] == 'EndLoop': # have to have ends for loops ifs and control because this language works like reading a list
            loopendpos = k
            k = looppos

            continue
                    
        
        elif opcode == "Break": # to get out of the loop
            k = loopendpos+1
        
        elif opcode == "If": # a classic
            f = False
            if parts[1] == "control": # buttons
                keys = pg.key.get_pressed()

                key = getattr(pg, "K_" + parts[2].lower(), None)

                if key is not None and keys[key]:
                    f = True

                if not f:
                    while k < len(programlines) and programlines[k] != "EndIf":
                        k += 1
                                        #0  1      2      3    4     5     6  7  8  9
            elif parts[1] == "inside": # If inside itemx itemy itemw itemh px py pw ph
                if (float(vars[parts[6]]) < float(parts[2]) + float(parts[4]) and float(vars[parts[6]]) + float(vars[parts[8]]) > float(parts[2]) and float(vars[parts[7]]) < float(parts[3]) + float(parts[5]) and float(vars[parts[7]]) + float(vars[parts[9]]) > float(parts[3])):
                    f = True
                else:
                    while k < len(programlines) and programlines[k] != "EndIf":
                        k += 1
            else:
                left = vars.get(parts[1], parts[1])
                right = vars.get(parts[3], parts[3])
                    

                if parts[2] == ">":
                    f = float(left) > float(right)
                elif parts[2] == "=":
                    f = float(left) == float(right)
                elif parts[2] == "<":
                    f = float(left) < float(right)
                elif parts[2] == "!":
                    f = float(left) != float(right)
                elif parts[2] == ">=":
                    f = float(left) >= float(right)
                elif parts[2] == "<=":
                    f = float(left) <= float(right)


                if not f:
                    while k < len(programlines) and programlines[k] != "EndIf":
                        k += 1
                    

        #4 hours a day is a step closer to the framwork 12 (2 hours is fine too)
                
        elif opcode == "Var": # setting a var would look something like "Var i = 20"
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

                    
            elif parts[2] == "+":                                # math is gud
                vars[parts[1]] = float(vars[parts[1]]) + float(parts[3])
                
            elif parts[2] == "-":
                vars[parts[1]] = float(vars[parts[1]]) - float(parts[3])
                
            elif parts[2] == "*":
                vars[parts[1]] = float(vars[parts[1]]) * float(parts[3])
                
            elif parts[2] == "/":
                vars[parts[1]] = float(vars[parts[1]]) / float(parts[3])
                
            elif parts[2] == "rnd":
                vars[parts[1]] = round(float(vars[parts[1]]))
                
            elif parts[2] == "ceil":
                vars[parts[1]] =  M.ceil(float(vars[parts[1]]))
                
            elif parts[2] == "flr":
                vars[parts[1]] =  M.floor(float(vars[parts[1]]))
                
            elif parts[2] == "sin":
                vars[parts[1]] =  M.sin(float(vars[parts[1]]))
                
            elif parts[2] == "cos":
                vars[parts[1]] =  M.cos(float(vars[parts[1]]))
                
            elif parts[2] == "tan":
                vars[parts[1]] =  M.tan(float(vars[parts[1]]))
                
            elif parts[2] == "sqrt":
                vars[parts[1]] =  M.sqrt(float(vars[parts[1]]))
                
            elif parts[2] == "pow":
                vars[parts[1]] =  M.pow(float(vars[parts[1]]),float(parts[3]))
                
            elif parts[2] == "abs":
                vars[parts[1]] =  abs(float(vars[parts[1]]))
                
            elif parts[2] == "dist":
                vars[parts[1]] =  dist(float(vars[parts[3]]),float(vars[parts[4]]),float(vars[parts[5]]),float(vars[parts[6]]))
                
            elif parts[2] == "vec3":
                vars[parts[1]] =  tuple((float(parts[3]),float(parts[4]),float(parts[5])))
                
            elif parts[2] == "rrng":
                vars[parts[1]] = R.randrange(int(parts[3]), int(parts[4]))
                
            elif parts[2] == "string":
                text = " ".join(parts[3:])
                vars[parts[1]] = str(text)
                

        elif opcode == "Image":
            
            if parts[2] == "set": #image pic set
                vars[parts[1]] = BetterImage(parts[3], (float(parts[4]),float(parts[5])), float(parts[6]),float(parts[7]))
                
            if parts[2] == "draw": #image pic draw
                vars[parts[1]].draw(window)
                
            if parts[2] == "move": #image pic move
                x = float(vars.get(parts[3], parts[3]))
                y = float(vars.get(parts[4], parts[4]))
                vars[parts[1]].move((x,y))
                


        elif opcode == "Button":
            
            if parts[2] == "set": # init the button
                vars[parts[1]] = Button(parts[3], (float(parts[4]),float(parts[5])), float(parts[6]),float(parts[7]))
                
            if parts[2] == "draw": #button pic draw
                vars[parts[1]].draw(window)
                
            if parts[2] == "pressed": #check if the button is being pressed
                b = vars[parts[1]].is_pressed()

                    
                if not b:
                    while k < len(programlines) and programlines[k] != "EndPressed":
                        k += 1
                        

        elif opcode == "Text":
            
            if parts[1] == "init": #text init 20
                font = pg.font.SysFont('Arial', int(parts[2]))
                
            if parts[1] == 'draw': #text draw name string color x y
                parts[2] = font.render(vars[parts[3]],False,vars[parts[4]])
                window.blit(parts[2],(int(parts[5]),int(parts[6])))
                    
                
        #if opcode == "getTimeHMS": #saving this for later
        #    time.strftime('%H:%M:%S:')
        
        
        elif opcode == "Screen":
            if parts[1] == "init": # Screen init w h
                window = pg.display.set_mode((int(parts[2]),int(parts[3])))
                pg.display.set_caption('Cobra Window')
                
            if parts[1] == "caption": # Screen caption string
                pg.display.set_caption(parts[2])
                caption = parts[2]
                
                
            if parts[1] == "pos": # Screen pos x y
                os.environ["SDL_VIDEO_WINDOW_POS"] = f"{parts[2]},{parts[3]}"
                
            if parts[1] == "box":  # Screen box color x y w h
                color = vars.get(parts[2], parts[2])

                x = float(vars.get(parts[3], parts[3]))
                y = float(vars.get(parts[4], parts[4]))
                w = float(vars.get(parts[5], parts[5]))
                h = float(vars.get(parts[6], parts[6]))

                pg.draw.rect(window, color, (x, y, w, h))
        
            if parts[1] == "fill": # Screen fill color
                color = vars.get(parts[2], parts[2])
                window.fill(color)
                
            if parts[1] == "fps": # toggle fps in the caption
                if parts[2] == "T":
                    FPSEnabled = True
                else:
                    FPSEnabled = False

            if parts[1] == "update": # Screen update frames
                if FPSEnabled == True:
                    pg.display.set_caption(caption + '     FPS:' + str(round(clock.get_fps())))
                pg.display.flip()
                clock.tick(int(parts[2]))
                
            if parts[1] == "quitControl": # be able to quit
                events = pg.event.get()

                for event in events:
                    if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                        pg.quit()
                        return
                    
        elif opcode == "Sleep":
            time.sleep(float(parts[1]))
            
        elif opcode == "Wait":
            if parts[1] == "T":
                waiting = True
                s = float(parts[2])
                
            
        elif opcode == "Sound":
            if parts[2] == "load": #Sound name load path
                sounds[parts[1]] = pg.mixer.Sound(parts[3])
            if parts[2] == "play":
                sounds[parts[1]].play()
                
                



        k+=1
    pg.quit()



if __name__ == "__main__":
    programfilepath = sys.argv[1]
    main(programfilepath)
