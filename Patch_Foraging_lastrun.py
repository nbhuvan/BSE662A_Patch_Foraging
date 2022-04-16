#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.2),
    on April 17, 2022, at 02:41
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
expName = 'Patch_Foraging'  # from the Builder filename that created this script
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
    originPath="C:\\Users\\Visitor's Arena\\Documents\\GitHub\\BSE662A_Patch_Foraging\\Patch_Foraging_lastrun.py",
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

state_c = random.randint(0,2)
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

# Initialize components for Routine "Patch_Selection"
Patch_SelectionClock = core.Clock()
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Foraging"
ForagingClock = core.Clock()
reward_value = 10;
cap_time =-1;


# Initialize components for Routine "End"
EndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='This is the end of first trial, now next trial will begin.\nThank you',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
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
        img.size = [size_x * 0.1, size_y * 0.1]
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
        img.size = [size_x * 0.1, size_y * 0.1]
        img_ltree.append(img)
        
    for i in range(state_r):
        img = visual.ImageStim(
            win=win,
            image="tree.png",
            units="pix"
        )
        size_x = img.size[0]
        size_y = img.size[1]
        img.size = [size_x * 0.1, size_y * 0.1]
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
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
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
        #print("state_r",l_c);
        dep_rate = 7 - l_c;
        reward_ctr = dep_rate;
        attack_time = 0;
        flag=0;
        while clock.getTime()<10: # draw moving stimulus
            if(clock.getTime() > reward_ctr): 
                reward_ctr= reward_ctr + dep_rate; 
                rnd = random.randint(0,len(reward_list))
                del reward_list[rnd:rnd +1 ]    
            if state_t == 1:
                pred_x = random.randint(0, 400)
                pred_y = random.randint(0, 600)
                pred_x = pred_x - 250
                if clock.getTime() > attack_time:
                    attack_time = attack_time + 1
                    print("Predator Location",pred_x, pred_y)
                    print("Player Location",p_pos[0],p_pos[1])
                    if abs(p_pos[0]-pred_x)< 60 and  abs(p_pos[1]-pred_y)< 60:
                        cap_txt.text= "Attacked by Predator";
                        print("Attacked by Predator")
                        end_img.draw()
                        core.wait(2)
                        core.quit()
                
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
    
            rect_l[p].pos = p_pos # directly update both x *and* y
            box.draw()
            for j,i in enumerate(reward_list):
                ind_tree = img_tree[i];
                tree_pos_x = ind_tree.pos[0];
                tree_pos_y= ind_tree.pos[1];
                
                if(abs(p_pos[0]-tree_pos_x)< 20 and  abs(p_pos[1]-tree_pos_y)< 20):
                    cap_txt.text= "Reward Captured";
                    del reward_list[j:j+1];
                    cap_time = clock.getTime();
                    # print("capture Time",cap_time);
      
                if(cap_time < clock.getTime()- 0.7 ):
                    cap_txt.text= "Forage";
            
                    
                
            for i in range(n):
                rect_l[i].draw()
            for i in reward_list:
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
        print(key)
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
        dep_rate = 7 - r_c;
        reward_ctr = dep_rate;
        attack_time = 0;
    #    print("state_r",state_r);
        while clock.getTime()<10: # draw moving stimulus
          
            if(clock.getTime() > reward_ctr): 
                reward_ctr= reward_ctr + dep_rate; 
                rnd = random.randint(0,len(reward_list)-1)
                del reward_list[rnd:rnd +1 ]
                #print(reward_list);
            if state_t == 1:
                pred_x = random.randint(0, 400)
                pred_y = random.randint(0, 600)
                pred_x = pred_x + 250
                if clock.getTime() > attack_time:
                    attack_time = attack_time + 1
                    print("Predator Location",pred_x, pred_y)
                    print("Player Location",p_pos[0],p_pos[1])
                    if abs(p_pos[0]-pred_x)< 60 and  abs(p_pos[1]-pred_y)< 60:
                        cap_txt.text= "Attacked by Predator";
                        print("Attacked by Predator")
                        end_img.draw()
                        core.wait(2)
                        core.quit()
            
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
    
            rect_r[p].pos = p_pos # directly update both x *and* y
            box.draw()
            for j,i in enumerate(reward_list):
                ind_tree = img_tree[i];
                tree_pos_x = ind_tree.pos[0];
                tree_pos_y= ind_tree.pos[1];
                
                if(abs(p_pos[0]-tree_pos_x)< 20 and  abs(p_pos[1]-tree_pos_y)< 20):
                    cap_txt.text= "Reward Captured";
                    del reward_list[j:j+1];
                    cap_time = clock.getTime();
                if(cap_time < clock.getTime()- 0.7 ):
                    cap_txt.text= "Forage";
            
            for i in range(n):
                rect_r[i].draw()
            
            for i in reward_list:
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
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'


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
