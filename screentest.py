#Screen Testing
#import getch
import readchar
import os
import random
from time import sleep

buffer = 0
posv = 500
posh = 500
character = 'X'
pos_save = ' ' #save previous value first!
#
lookva = 7
lookvb = 17
#
lookha = 35
lookhb = 45
#
lkdist = 11



#Single Screen output Good for stuff like App/CPU
#Easy to Reference
#screen_buff = [' ' for x in range(1920)]

### World Creator!
# Creates actual 2D array!
# Array Parameters
scr_vert = 1000
scr_horz = 1000
# Create the Array
screen_buff = [[' '] * scr_horz for i in range(scr_vert)]
####

def envi_gen(): #Creates Ground Clutter
    count = 10000
    h = 0
    v = 0
    while count > 0:
        h = random.randint(0,scr_vert-1)
        v = random.randint(0,scr_horz-1)
        screen_buff[h][v] = '.' #Ground Clutter Character
        count = count - 1

def blit_screen():
    print('Location: '+str(posv)+' '+str(posh) + ' ' + str(buffer)+' '+'LookVa:Vb'+'-'+ str(lookva) + ' ' + str(lookvb)+' '+'LookHa:Hb'+'-'+ str(lookha) + ' ' + str(lookhb))
# Testing

#########
    for row in screen_buff[lookva:lookvb]: #vert
#        print(''.join([str(elem) for elem in row]))
        print(''.join(str(elem) for elem in row[lookha:lookhb])) #horiz


envi_gen()
#blit_screen()

while 1: #Works, outputs the list cleanly! Woo!
    buffer = screen_buff[posv][posh]
    screen_buff[posv][posh] = 'X'
    sleep(0.01)
    blit_screen()
    char = readchar.readkey()
#    char = getch.getch() #remove e for no echo
## Insert stuff to now interact with things
## 3D array for items in area?
### Dictionary in secondary array?
    if char == 'd':
        posh = posh + 1
        lookha = posh - lkdist
        lookhb = posh + lkdist
        screen_buff[posv][posh-1] = buffer
        if posh > (scr_horz - 1):
            posh = posh - 1

    if char == 'a':
        posh = posh - 1
        lookha = posh - lkdist
        lookhb = posh + lkdist
        screen_buff[posv][posh+1] = buffer
        if posh < 0:
            posh = posh + 1

    if char == 'w':
        posv = posv - 1
        lookva = posv - lkdist
        lookvb = posv + lkdist
        screen_buff[posv+1][posh] = buffer
        if posv < 0:
            posv = posv + 1

    if char == 's':
        posv = posv + 1
        lookva = posv - lkdist
        lookvb = posv + lkdist
        screen_buff[posv-1][posh] = buffer
        if posv > (scr_vert - 1):
            posv = posv - 1

    if char == 'q': #Exit
        exit()
    else:
        posv = posv
        posh = posh
        continue
'''
 To Do:
Rate Limit Input!
'''
