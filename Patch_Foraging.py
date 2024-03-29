#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on April 19, 2022, at 00:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

import os
from psychopy import visual, event, core, data
from pathlib import Path
import random
import os
from psychopy import visual, event, core
import random



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.2'
expName = 'Patch_Foraging_19_12_30am'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\bhuva\\Desktop\\BSE662_Project\\Projects\\Patch_Foraging\\Patch_Foraging.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Welcometext = visual.TextStim(win=win, name='Welcometext',
    text='Welcome\nPlease press Spacebar to start',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[1.0000, 1.0000, 1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
exp_start = keyboard.Keyboard()

# Initialize components for Routine "ViewPatch"
ViewPatchClock = core.Clock()
competitors = [[1,4],[5,1],[2,5]]
#competitors = [[1,4]]

state_c = random.randint(0,2)
#state_c = 0
state_t = random.randint(0,1)
#state_t = 1
state_r = random.randint(1,5)

l_c = competitors[state_c][0]
r_c = competitors[state_c][1]

rect_l = []
rect_r = []
img_tree = []
img_ltree = []
img_rtree = []

# Initialize components for Routine "Patch_Selection"
Patch_SelectionClock = core.Clock()
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Foraging"
ForagingClock = core.Clock()
reward_value = 10;
cap_time =-1;
reward_captured = 0
reward_nc = 0
captured_index = []
shock = 0
reward_treepos = [[500,40],[580,40],[660,40],[500,-40],[580,-40],[660,-40]]


def motion(p_pos): #motion function
    k = event.getKeys()
    if k: # if there was an actual key pressed:
        if k[0] == 'left':
            p_pos[0] += LEFT
        elif k[0] == 'right':
            p_pos[0] += RIGHT
        elif k[0] == 'up':
            p_pos[1] += RIGHT
        elif k[0] == 'down':
            p_pos[1] += LEFT
        elif k[0] == 'q':
            core.quit()
#            
    if p_pos[0] > (200-15):
        p_pos[0] = (200-15)
    elif p_pos[0]<-(200-15):
        p_pos[0] = -(200-15)
    if p_pos[1]> (300-15):
        p_pos[1] = (300-15)
    elif p_pos[1]<-(300-15):
        p_pos[1] = -(300-15)
    return p_pos
    

# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='This is the end of current trial, now next trial will begin.\nThank you',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
exp_start.keys = []
exp_start.rt = []
_exp_start_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Welcometext, exp_start]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcometext* updates
    if Welcometext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcometext.frameNStart = frameN  # exact frame index
        Welcometext.tStart = t  # local t and not account for scr refresh
        Welcometext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcometext, 'tStartRefresh')  # time at next scr refresh
        Welcometext.setAutoDraw(True)
    
    # *exp_start* updates
    waitOnFlip = False
    if exp_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exp_start.frameNStart = frameN  # exact frame index
        exp_start.tStart = t  # local t and not account for scr refresh
        exp_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exp_start, 'tStartRefresh')  # time at next scr refresh
        exp_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(exp_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(exp_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if exp_start.status == STARTED and not waitOnFlip:
        theseKeys = exp_start.getKeys(keyList=['space'], waitRelease=False)
        _exp_start_allKeys.extend(theseKeys)
        if len(_exp_start_allKeys):
            exp_start.keys = _exp_start_allKeys[-1].name  # just the last key pressed
            exp_start.rt = _exp_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ViewPatch"-------
continueRoutine = True
# update component parameters for each repeat
clock = core.Clock()

c1 = -250
c2 = 250

box_t = visual.Rect(
    win=win,
    units="pix",
    width=1000,
    height=700,
    fillColor= 'red',
    lineColor=[-1, -1, 1]
)

box1 = visual.Rect(
    win=win,
    units="pix",
    width=400,
    height=600,
    fillColor= 'black',
    lineColor=[-1, -1, 1]
)
box1.pos = [c1,0]

box2 = visual.Rect(
    win=win,
    units="pix",
    width=400,
    height=600,
    fillColor= 'black',
    lineColor=[-1, -1, 1]
)
box2.pos = [c2,0]


for i in range(l_c):
    rect_x = visual.Rect(win, units="pix",
        width=30,
        height=30,
        fillColor= 'yellow')
    rect_l.append(rect_x)

for i in range(l_c):
    x = random.uniform(-1, 1)
    y = random.uniform(-1,1)
    x = x*185
    y = y*285
    rect_l[i].pos = [c1+x,y]

for i in range(r_c):
    rect_x = visual.Rect(win, units="pix",
        width=30,
        height=30,
        fillColor= 'yellow')
    rect_r.append(rect_x)

for i in range(r_c):
    x = random.uniform(-1, 1)
    y = random.uniform(-1,1)
    x = x*185
    y = y*285
    rect_r[i].pos = [c2+x,y]


for i in range(state_r):
    img = visual.ImageStim(
        win=win,
        image="tree.png",
        units="pix"
    )
    size_x = img.size[0]
    size_y = img.size[1]
    img.size = [size_x * 0.15, size_y * 0.15]
#    print(img.size)
    img_tree.append(img)

for i in range(state_r):
    img = visual.ImageStim(
        win=win,
        image="tree.png",
        units="pix"
    )
    size_x = img.size[0]
    size_y = img.size[1]
    img.size = [size_x * 0.15, size_y * 0.15]
    img_ltree.append(img)
    
for i in range(state_r):
    img = visual.ImageStim(
        win=win,
        image="tree.png",
        units="pix"
    )
    size_x = img.size[0]
    size_y = img.size[1]
    img.size = [size_x * 0.15, size_y * 0.15]
    img_rtree.append(img)
    
#print(len(img_ltree))
#print(len(img_rtree))

for i in range(len(img_tree)):
    x = random.uniform(-1, 1)
    y = random.uniform(-1,1)
    size_x = img_tree[0].size[0]
    size_y = img_tree[0].size[1]
    
    x = x*(200-size_x)
    y = y*(300-size_y)
#    print(x,y)
    img_tree[i].pos = [x,y]

for i in range(len(img_tree)):
    pos = img_tree[i].pos
    x_l = pos[0] + c1
    y_l = pos[1]
    x_r = pos[0] + c2
    y_r = pos[1]
    print(pos)
    print(x_l,y_l)
    print(x_r,y_r)
    img_ltree[i].pos = [x_l,y_l]
    img_rtree[i].pos = [x_r,y_r]
    

#for i in range(len(img_rtree)):
#    posr = img_tree[i].pos
#    x = posr[0] + c2
#    y = posr[1]
#    print(x,y)
#    img_rtree[i].pos = [x,y]

clock.reset()
while clock.getTime() < 5: # draw moving stimulus
    if state_t:
        box_t.draw()
    box1.draw()
    box2.draw()
    
    for i in range(state_r):
#        img_ltree[i].draw()
        img_rtree[i].draw()
        img_ltree[i].draw()

    for i in range(l_c):
        rect_l[i].draw()
    for i in range(r_c):
        rect_r[i].draw()
    
    win.flip() # make the drawn things visible

# keep track of which components have finished
ViewPatchComponents = []
for thisComponent in ViewPatchComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ViewPatchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ViewPatch"-------
while continueRoutine:
    # get current time
    t = ViewPatchClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ViewPatchClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ViewPatchComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ViewPatch"-------
for thisComponent in ViewPatchComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('left_competitors', l_c)
thisExp.addData('right_competitors', r_c)
thisExp.addData('threat', state_t)
thisExp.addData('no_rewards', state_r)
# the Routine "ViewPatch" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Patch_Selection"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Patch_SelectionComponents = [key_resp]
for thisComponent in Patch_SelectionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Patch_SelectionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Patch_Selection"-------
while continueRoutine:
    # get current time
    t = Patch_SelectionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Patch_SelectionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Patch_SelectionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Patch_Selection"-------
for thisComponent in Patch_SelectionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
#thisExp.nextEntry()
# the Routine "Patch_Selection" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Foraging"-------
continueRoutine = True
# update component parameters for each repeat
box = visual.Rect(
    win=win,
    units="pix",
    width=400,
    height=600,
    fillColor= 'black',
    lineColor=[-1, -1, 1]
)
end_img = visual.ImageStim(
        win=win,
        image="attacked.png",
        units="pix"
)

cap_txt = visual.TextBox2(
    win,
    "Forage",
    font='Open Sans',
    units="pix",
    color=(1, 0, 0), 
    colorSpace='rgb',
    letterHeight = 40
)

reward_txt = visual.TextBox2( # text showed when reward is caputures
    win,
    "Rewards Gained",
    units="pix",
    color= (1, 0, 0), 
    colorSpace='rgb',
    letterHeight = 40
)

reward_txt.pos = [880,160]
reward_box = visual.Rect( # box for the selected patch
    win=win,
    units="pix",
    width=240,
    height=160,
    fillColor= 'black',
    lineColor= 'green'
)
reward_box.pos = [580,0]


cap_txt.pos= [box.pos[0]+ 150,325]
cap_txt.draw()
box.draw()
print("Trial started");
data = thisExp.getAllEntries()
key = data[0]['key_resp.keys']




if key == 'left':
    for i in range(len(rect_l)):
        position = rect_l[i].pos
        position[0] -= -250
        rect_l[i].pos = position
    #        
    n = len(rect_l)
    p = random.randint(0,n-1)
   # print(key)
    clock = core.Clock()

    LEFT = -10
    RIGHT = 10
    rect = visual.Rect(
        win=win,
        units="pix",
        width=400,
        height=600,
        fillColor= 'black',
        lineColor=[-1, -1, 1]
    )

    clock.reset()
    
    p_pos = rect_l[p].pos
    depriciated_reward =[];
    
    reward_list = list(range(state_r));
    rect_list = list(range(l_c))
    #print("state_r",l_c);
    if l_c==1:
        dep_rate = 10
    else:
        dep_rate = 7 - l_c;
    reward_ctr = dep_rate;
    attack_time = 2;
    flag=0;
    while clock.getTime()<10: # draw moving stimulus
        if(clock.getTime() > reward_ctr):
            reward_ctr= reward_ctr + dep_rate; 
            if(len(reward_list)>=1):
                rnd = random.randint(0,len(reward_list)-1)
                del reward_list[rnd]
        if state_t == 1:
            pred_x = random.randint(-150, 150)
            pred_y = random.randint(-250, 250)
#            pred_x = pred_x - 250
            if clock.getTime() > attack_time:
                attack_time = attack_time + 2
                dist = []
                del_comp = 0;
                print("number of comp is ",len(rect_l))
                for i in rect_list:
                    dist.append([pow(abs(rect_l[i].pos[0]-pred_x),2) + pow(abs(rect_l[i].pos[1]-pred_y),2),i])
                dist.sort()
                print(dist)
                if(dist[0][0] < 500000):
                    del_comp = dist[0][1];
#                    print(i)
#                    del rect_l[del_comp];
#                    print(rect_list)
#                    print(del_comp)
                    if del_comp==p:
                        shock = -100
                        cap_txt.text= "Attacked by Predator";
                        print("Attacked by Predator")
                        flag=1;
                    for i1 in range(len(rect_list)):
#                        print(i1)
                        if rect_list[i1]==del_comp:
                            del rect_list[i1]
                            break

        if(flag):
            while(clock.getTime()<10):
                end_img.draw()
                win.flip()
#            core.wait(10-clock.getTime())
        else:
            p_pos = motion(p_pos) #captures the motion
            rect_l[p].pos = p_pos # directly update both x *and* y
            box.draw()
            for i,j in enumerate(reward_list):
                ind_tree = img_tree[j];
                tree_pos_x = ind_tree.pos[0];
                tree_pos_y= ind_tree.pos[1];
            
                if(abs(p_pos[0]-tree_pos_x)< 20 and  abs(p_pos[1]-tree_pos_y)< 20):
                    cap_txt.text= "Reward Captured";
                    captured_index.append(j)
                    del reward_list[i]
                    img_tree[j].pos = reward_treepos[reward_nc]
                    reward_captured += 100
                    cap_time = clock.getTime();
                    reward_nc +=1
                # print("capture Time",cap_time);

            if(cap_time < clock.getTime()- 0.7 ):
                cap_txt.text= "Forage";
            reward_box.draw()
            reward_txt.draw()
            for i in rect_list:
                rect_l[i].draw()
            for i in reward_list:
                img_tree[i].draw()
            for i in captured_index:
                img_tree[i].draw()
            cap_txt.draw();
            win.flip() # make the drawn things visible
else:
    for i in range(len(rect_r)):
        position = rect_r[i].pos
        position[0] -= 250
        rect_r[i].pos = position
    #        
    n = len(rect_r)
    p = random.randint(0,n-1)
#    print(key)
    clock = core.Clock()

    LEFT = -10
    RIGHT = 10
    rect = visual.Rect(
        win=win,
        units="pix",
        width=400,
        height=600,
        fillColor= 'black',
        lineColor=[-1, -1, 1]
    )

    clock.reset()
    p_pos = rect_r[p].pos
    reward_list = list(range(state_r));
    rect_list = list(range(r_c))
    if r_c==1:
        dep_rate = 10
    else:
        dep_rate = 7 - r_c;
    reward_ctr = dep_rate;
    attack_time = 2;
    flag=0;
    while clock.getTime()<10: # draw moving stimulus
        if(clock.getTime() > reward_ctr):
            reward_ctr= reward_ctr + dep_rate; 
            if(len(reward_list)>=1):
                rnd = random.randint(0,len(reward_list)-1)
                del reward_list[rnd]
        if state_t == 1:
            pred_x = random.randint(-150, 150)
            pred_y = random.randint(-250, 250)
#            pred_x = pred_x - 250
            if clock.getTime() > attack_time:
                attack_time = attack_time + 2
                dist = []
                del_comp = 0;
                print("number of comp is ",len(rect_r))
                for i in rect_list:
                    dist.append([pow(abs(rect_r[i].pos[0]-pred_x),2) + pow(abs(rect_r[i].pos[1]-pred_y),2),i])
                dist.sort()
                print(dist)
                if(dist[0][0] < 500000):
                    del_comp = dist[0][1];
#                    print(i)
#                    del rect_r[del_comp];
                    if del_comp==p:
                        shock = -100
                        cap_txt.text= "Attacked by Predator";
                        print("Attacked by Predator")
                        flag=1;
                    for i1 in range(len(rect_list)):
                        if rect_list[i1]==del_comp:
                            del rect_list[i1]
                            break
        if(flag):
            while(clock.getTime()<10):
                end_img.draw()
                win.flip()
        else:
            p_pos = motion(p_pos) #captures the motion
            rect_r[p].pos = p_pos # directly update both x *and* y
            box.draw()
            for i,j in enumerate(reward_list):
                ind_tree = img_tree[j];
                tree_pos_x = ind_tree.pos[0];
                tree_pos_y= ind_tree.pos[1];
            
                if(abs(p_pos[0]-tree_pos_x)< 20 and  abs(p_pos[1]-tree_pos_y)< 20):
                    cap_txt.text= "Reward Captured";
                    captured_index.append(j)
                    del reward_list[i]
                    img_tree[j].pos = reward_treepos[reward_nc]
                    reward_captured += 100
                    cap_time = clock.getTime();
                    reward_nc +=1
                # print("capture Time",cap_time);

            if(cap_time < clock.getTime()- 0.7 ):
                cap_txt.text= "Forage";
            reward_box.draw()
            reward_txt.draw()
            for i in rect_list:
                rect_r[i].draw()
            for i in reward_list:
                img_tree[i].draw()
            for i in captured_index:
                img_tree[i].draw()
            cap_txt.draw();
            win.flip() # make the drawn things visible
# keep track of which components have finished
ForagingComponents = []
for thisComponent in ForagingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ForagingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Foraging"-------
while continueRoutine:
    # get current time
    t = ForagingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ForagingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ForagingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Foraging"-------
for thisComponent in ForagingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rewards_captured', reward_captured)
thisExp.addData('shock', shock)
# the Routine "Foraging" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [text]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
state_c = random.randint(0,2)
#state_c = 0
#state_t = random.randint(0,1)
state_t = 1
state_r = random.randint(1,5)

l_c = competitors[state_c][0]
r_c = competitors[state_c][1]

rect_l = []
rect_r = []
img_tree = []
img_ltree = []
img_rtree = []
reward_value = 10;
cap_time =-1;
reward_captured = 0
reward_nc = 0
captured_index = []
shock = 0
reward_treepos = [[500,40],[580,40],[660,40],[500,-40],[580,-40],[660,-40]]

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
