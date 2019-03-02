#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.0b9),
    on Mon Jan 28 17:54:38 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'VocabTraining'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'group': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/TimothyMcCormick/Desktop/ZIPDISS/VocabTraining (MUST ADD ARQUITECT AND SCULPTOR)/VocabTraining_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "setUp"
setUpClock = core.Clock()
group = expInfo["group"]

# A dictionary, where the key is a block name,
# and the value is the name of the spreadsheet
# containing the trials for that block
condFiles = {
    "A": "VocabTrainingA.xlsx",
    "B": "VocabTrainingB.xlsx",
    }

# Key is group (a string "1", "2", etc.)
# Value is a list containing the blocks in the desired
#   order for the group. 
blockSequences = {
    "1": ["A", "B"], # Group 1 will see A first, then B.
    "2": ["B", "A"],
    }

# Make sure "group" entered in the gui dialog is one that
# we want
assert group in blockSequences, "Invalid group entered"

# Set the block sequence for this participant's group.
blockSeq = blockSequences[group]

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
VocabTrainingInstructions = visual.TextStim(win=win, name='VocabTrainingInstructions',
    text="You're going to learn (or review) some everyday Spanish vocabulary words. As you move through the vocab training, hit space bar to see the next word. After the each of the two rounds of training, you'll be quizzed before moving on to the next part of the study (minimum = 85% correct)\n\nPress 'space' to continue.\n",
    font='Courier',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pickBlocks2"
pickBlocks2Clock = core.Clock()


# Initialize components for Routine "LearningPhase"
LearningPhaseClock = core.Clock()
vocabPicAssoc = visual.TextStim(win=win, name='vocabPicAssoc',
    text='default text',
    font='courier',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
TranslationTraining = visual.TextStim(win=win, name='TranslationTraining',
    text='default text',
    font='courier',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
pressSpace = visual.TextStim(win=win, name='pressSpace',
    text="Press 'Space' to continue.",
    font='courier',
    pos=(0, -.75), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "PostTraining"
PostTrainingClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="Great! Are you ready to show what you've learned? On the next section, you'll need to identify the words, with at least an 80% accuracy rate.\n\nIf you want to see these words again, click 'F'. \n\nIf you're ready to move on, click 'J'.",
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
instructions2 = visual.TextStim(win=win, name='instructions2',
    text='Remember: You need to have \nat least 85% correct in order \nto continue to the next part\nof the experiment.\n\nYou\'ll need to respond using the keys: "a", "f", "j" and ";", which correspond to the position of the picture on the screen.\n\nPress \'space\' to continue.',
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
Question = visual.TextStim(win=win, name='Question',
    text='¿Cuál imágen representa...',
    font='courier',
    pos=(0, .75), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
imageA = visual.ImageStim(
    win=win, name='imageA',
    image='sin', mask=None,
    ori=0, pos=(-0.75, 0), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imageF = visual.ImageStim(
    win=win, name='imageF',
    image='sin', mask=None,
    ori=0, pos=(-0.25, 0), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
imageJ = visual.ImageStim(
    win=win, name='imageJ',
    image='sin', mask=None,
    ori=0, pos=(0.25, 0), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
imageSemicolon = visual.ImageStim(
    win=win, name='imageSemicolon',
    image='sin', mask=None,
    ori=0, pos=(.75, 0), size=(0.45, 0.45),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
criticalText = visual.TextStim(win=win, name='criticalText',
    text='default text',
    font='courier',
    pos=(0, .5), height=0.1, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);


# Initialize components for Routine "Rest"
RestClock = core.Clock()
restPhase = visual.TextStim(win=win, name='restPhase',
    text="Great! You've learned (or reviewed) 20 new words! \n\nTake a short break if you need, because there are 20 more words to learn!\n\nPress 'space' when you're ready to continue.",
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "SignOut"
SignOutClock = core.Clock()
goodbye = visual.TextStim(win=win, name='goodbye',
    text="Great! You've mastered these vocabulary items. \n\nShow the researcher this screen and they'll help you move on to the next part of the experiment.",
    font='courier',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setUp"-------
t = 0
setUpClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

# keep track of which components have finished
setUpComponents = []
for thisComponent in setUpComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "setUp"-------
while continueRoutine:
    # get current time
    t = setUpClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setUpComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setUp"-------
for thisComponent in setUpComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "setUp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ContinueSpace = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [VocabTrainingInstructions, ContinueSpace]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *VocabTrainingInstructions* updates
    if t >= 0.0 and VocabTrainingInstructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        VocabTrainingInstructions.tStart = t
        VocabTrainingInstructions.frameNStart = frameN  # exact frame index
        VocabTrainingInstructions.setAutoDraw(True)
    
    # *ContinueSpace* updates
    if t >= 0.0 and ContinueSpace.status == NOT_STARTED:
        # keep track of start time/frame for later
        ContinueSpace.tStart = t
        ContinueSpace.frameNStart = frameN  # exact frame index
        ContinueSpace.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(ContinueSpace.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if ContinueSpace.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            ContinueSpace.keys = theseKeys[-1]  # just the last key pressed
            ContinueSpace.rt = ContinueSpace.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if ContinueSpace.keys in ['', [], None]:  # No response was made
    ContinueSpace.keys=None
thisExp.addData('ContinueSpace.keys',ContinueSpace.keys)
if ContinueSpace.keys != None:  # we had a response
    thisExp.addData('ContinueSpace.rt', ContinueSpace.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=len(condFiles), method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pickBlocks2"-------
    t = 0
    pickBlocks2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # If we're on the 0th repetition (in our case meaning the 1st block),
    # get the 0th item in blockSeq list we made earlier.
    block = blockSeq[blocks.thisRepN]
    
    # Get the conditions file for that block
    condFile = condFiles[block]
    # keep track of which components have finished
    pickBlocks2Components = []
    for thisComponent in pickBlocks2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pickBlocks2"-------
    while continueRoutine:
        # get current time
        t = pickBlocks2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pickBlocks2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pickBlocks2"-------
    for thisComponent in pickBlocks2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "pickBlocks2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    repeatTrainingloop = data.TrialHandler(nReps=999, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='repeatTrainingloop')
    thisExp.addLoop(repeatTrainingloop)  # add the loop to the experiment
    thisRepeatTrainingloop = repeatTrainingloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeatTrainingloop.rgb)
    if thisRepeatTrainingloop != None:
        for paramName in thisRepeatTrainingloop:
            exec('{} = thisRepeatTrainingloop[paramName]'.format(paramName))
    
    for thisRepeatTrainingloop in repeatTrainingloop:
        currentLoop = repeatTrainingloop
        # abbreviate parameter names if possible (e.g. rgb = thisRepeatTrainingloop.rgb)
        if thisRepeatTrainingloop != None:
            for paramName in thisRepeatTrainingloop:
                exec('{} = thisRepeatTrainingloop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        learningLoop = data.TrialHandler(nReps=1, method='fullRandom', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(condFile),
            seed=None, name='learningLoop')
        thisExp.addLoop(learningLoop)  # add the loop to the experiment
        thisLearningLoop = learningLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLearningLoop.rgb)
        if thisLearningLoop != None:
            for paramName in thisLearningLoop:
                exec('{} = thisLearningLoop[paramName]'.format(paramName))
        
        for thisLearningLoop in learningLoop:
            currentLoop = learningLoop
            # abbreviate parameter names if possible (e.g. rgb = thisLearningLoop.rgb)
            if thisLearningLoop != None:
                for paramName in thisLearningLoop:
                    exec('{} = thisLearningLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "LearningPhase"-------
            t = 0
            LearningPhaseClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            vocabPicAssoc.setText(TrainingFull)
            TranslationTraining.setText(Translation)
            key_resp_3 = event.BuilderKeyResponse()
            image.setImage(imagename)
            # keep track of which components have finished
            LearningPhaseComponents = [vocabPicAssoc, TranslationTraining, key_resp_3, image, pressSpace]
            for thisComponent in LearningPhaseComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "LearningPhase"-------
            while continueRoutine:
                # get current time
                t = LearningPhaseClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *vocabPicAssoc* updates
                if t >= 0.0 and vocabPicAssoc.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    vocabPicAssoc.tStart = t
                    vocabPicAssoc.frameNStart = frameN  # exact frame index
                    vocabPicAssoc.setAutoDraw(True)
                
                # *TranslationTraining* updates
                if t >= 0.0 and TranslationTraining.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    TranslationTraining.tStart = t
                    TranslationTraining.frameNStart = frameN  # exact frame index
                    TranslationTraining.setAutoDraw(True)
                
                # *key_resp_3* updates
                if t >= 0 and key_resp_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_3.tStart = t
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if key_resp_3.status == STARTED:
                    theseKeys = event.getKeys(keyList=['space'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                        key_resp_3.rt = key_resp_3.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
                
                # *image* updates
                if t >= 0.0 and image.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image.tStart = t
                    image.frameNStart = frameN  # exact frame index
                    image.setAutoDraw(True)
                
                # *pressSpace* updates
                if t >= 1.0 and pressSpace.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    pressSpace.tStart = t
                    pressSpace.frameNStart = frameN  # exact frame index
                    pressSpace.setAutoDraw(True)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in LearningPhaseComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "LearningPhase"-------
            for thisComponent in LearningPhaseComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys=None
            learningLoop.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                learningLoop.addData('key_resp_3.rt', key_resp_3.rt)
            # the Routine "LearningPhase" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'learningLoop'
        
        
        # ------Prepare to start Routine "PostTraining"-------
        t = 0
        PostTrainingClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        keyresponse4 = event.BuilderKeyResponse()
        
        # keep track of which components have finished
        PostTrainingComponents = [text, keyresponse4]
        for thisComponent in PostTrainingComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "PostTraining"-------
        while continueRoutine:
            # get current time
            t = PostTrainingClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            
            # *keyresponse4* updates
            if t >= 0.0 and keyresponse4.status == NOT_STARTED:
                # keep track of start time/frame for later
                keyresponse4.tStart = t
                keyresponse4.frameNStart = frameN  # exact frame index
                keyresponse4.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(keyresponse4.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if keyresponse4.status == STARTED:
                theseKeys = event.getKeys(keyList=['f', 'j'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    keyresponse4.keys = theseKeys[-1]  # just the last key pressed
                    keyresponse4.rt = keyresponse4.clock.getTime()
                    # was this 'correct'?
                    if (keyresponse4.keys == str('j')) or (keyresponse4.keys == 'j'):
                        keyresponse4.corr = 1
                    else:
                        keyresponse4.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PostTrainingComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PostTraining"-------
        for thisComponent in PostTrainingComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if keyresponse4.keys in ['', [], None]:  # No response was made
            keyresponse4.keys=None
            # was no response the correct answer?!
            if str('j').lower() == 'none':
               keyresponse4.corr = 1;  # correct non-response
            else:
               keyresponse4.corr = 0;  # failed to respond (incorrectly)
        # store data for repeatTrainingloop (TrialHandler)
        repeatTrainingloop.addData('keyresponse4.keys',keyresponse4.keys)
        repeatTrainingloop.addData('keyresponse4.corr', keyresponse4.corr)
        if keyresponse4.keys != None:  # we had a response
            repeatTrainingloop.addData('keyresponse4.rt', keyresponse4.rt)
        if keyresponse4.corr:
            repeatTrainingloop.finished = True
        # the Routine "PostTraining" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 999 repeats of 'repeatTrainingloop'
    
    
    # set up handler to look after randomisation of conditions etc
    repeatloop = data.TrialHandler(nReps=999, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='repeatloop')
    thisExp.addLoop(repeatloop)  # add the loop to the experiment
    thisRepeatloop = repeatloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeatloop.rgb)
    if thisRepeatloop != None:
        for paramName in thisRepeatloop:
            exec('{} = thisRepeatloop[paramName]'.format(paramName))
    
    for thisRepeatloop in repeatloop:
        currentLoop = repeatloop
        # abbreviate parameter names if possible (e.g. rgb = thisRepeatloop.rgb)
        if thisRepeatloop != None:
            for paramName in thisRepeatloop:
                exec('{} = thisRepeatloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Instructions2"-------
        t = 0
        Instructions2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        ContinueSpace2 = event.BuilderKeyResponse()
        # keep track of which components have finished
        Instructions2Components = [instructions2, ContinueSpace2]
        for thisComponent in Instructions2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Instructions2"-------
        while continueRoutine:
            # get current time
            t = Instructions2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *instructions2* updates
            if t >= 0.0 and instructions2.status == NOT_STARTED:
                # keep track of start time/frame for later
                instructions2.tStart = t
                instructions2.frameNStart = frameN  # exact frame index
                instructions2.setAutoDraw(True)
            
            # *ContinueSpace2* updates
            if t >= 0.0 and ContinueSpace2.status == NOT_STARTED:
                # keep track of start time/frame for later
                ContinueSpace2.tStart = t
                ContinueSpace2.frameNStart = frameN  # exact frame index
                ContinueSpace2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(ContinueSpace2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if ContinueSpace2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    ContinueSpace2.keys = theseKeys[-1]  # just the last key pressed
                    ContinueSpace2.rt = ContinueSpace2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Instructions2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Instructions2"-------
        for thisComponent in Instructions2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if ContinueSpace2.keys in ['', [], None]:  # No response was made
            ContinueSpace2.keys=None
        repeatloop.addData('ContinueSpace2.keys',ContinueSpace2.keys)
        if ContinueSpace2.keys != None:  # we had a response
            repeatloop.addData('ContinueSpace2.rt', ContinueSpace2.rt)
        # the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop1 = data.TrialHandler(nReps=1, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(condFile),
            seed=None, name='loop1')
        thisExp.addLoop(loop1)  # add the loop to the experiment
        thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
        if thisLoop1 != None:
            for paramName in thisLoop1:
                exec('{} = thisLoop1[paramName]'.format(paramName))
        
        for thisLoop1 in loop1:
            currentLoop = loop1
            # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
            if thisLoop1 != None:
                for paramName in thisLoop1:
                    exec('{} = thisLoop1[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "trial"-------
            t = 0
            trialClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            # update component parameters for each repeat
            keyresponse = event.BuilderKeyResponse()
            imageA.setImage(ColumnA)
            imageF.setImage(ColumnF)
            imageJ.setImage(ColumnJ)
            imageSemicolon.setImage(ColumnSemicolon)
            criticalText.setText(MatchingSection)
            ''' reset the counter at the beginning of each practice loop:'''
            if loop1.thisN == 0:
                number_correct = 0
            # keep track of which components have finished
            trialComponents = [Question, keyresponse, imageA, imageF, imageJ, imageSemicolon, criticalText]
            for thisComponent in trialComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "trial"-------
            while continueRoutine:
                # get current time
                t = trialClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Question* updates
                if t >= 0.0 and Question.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    Question.tStart = t
                    Question.frameNStart = frameN  # exact frame index
                    Question.setAutoDraw(True)
                
                # *keyresponse* updates
                if t >= 0.0 and keyresponse.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    keyresponse.tStart = t
                    keyresponse.frameNStart = frameN  # exact frame index
                    keyresponse.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(keyresponse.clock.reset)  # t=0 on next screen flip
                    event.clearEvents(eventType='keyboard')
                if keyresponse.status == STARTED:
                    theseKeys = event.getKeys(keyList=['a', 'f', 'j', 'semicolon'])
                    
                    # check for quit:
                    if "escape" in theseKeys:
                        endExpNow = True
                    if len(theseKeys) > 0:  # at least one key was pressed
                        keyresponse.keys = theseKeys[-1]  # just the last key pressed
                        keyresponse.rt = keyresponse.clock.getTime()
                        # was this 'correct'?
                        if (keyresponse.keys == str(CorrectAnswer)) or (keyresponse.keys == CorrectAnswer):
                            keyresponse.corr = 1
                        else:
                            keyresponse.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *imageA* updates
                if t >= 0.0 and imageA.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    imageA.tStart = t
                    imageA.frameNStart = frameN  # exact frame index
                    imageA.setAutoDraw(True)
                
                # *imageF* updates
                if t >= 0.0 and imageF.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    imageF.tStart = t
                    imageF.frameNStart = frameN  # exact frame index
                    imageF.setAutoDraw(True)
                
                # *imageJ* updates
                if t >= 0.0 and imageJ.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    imageJ.tStart = t
                    imageJ.frameNStart = frameN  # exact frame index
                    imageJ.setAutoDraw(True)
                
                # *imageSemicolon* updates
                if t >= 0.0 and imageSemicolon.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    imageSemicolon.tStart = t
                    imageSemicolon.frameNStart = frameN  # exact frame index
                    imageSemicolon.setAutoDraw(True)
                
                # *criticalText* updates
                if t >= 0.0 and criticalText.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    criticalText.tStart = t
                    criticalText.frameNStart = frameN  # exact frame index
                    criticalText.setAutoDraw(True)
                
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "trial"-------
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if keyresponse.keys in ['', [], None]:  # No response was made
                keyresponse.keys=None
                # was no response the correct answer?!
                if str(CorrectAnswer).lower() == 'none':
                   keyresponse.corr = 1;  # correct non-response
                else:
                   keyresponse.corr = 0;  # failed to respond (incorrectly)
            # store data for loop1 (TrialHandler)
            loop1.addData('keyresponse.keys',keyresponse.keys)
            loop1.addData('keyresponse.corr', keyresponse.corr)
            if keyresponse.keys != None:  # we had a response
                loop1.addData('keyresponse.rt', keyresponse.rt)
            if keyresponse.corr:
                number_correct = number_correct + 1
            
            ''' if this is the final repetition, check the proportion correct.'''
            if loop1.thisN +1 == loop1.nTotal:
                if number_correct/(loop1.nTotal) >= 0.85:
                    ''' terminate the outer loop so no more practice happens:'''
                    repeatloop.finished = True
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1 repeats of 'loop1'
        
        thisExp.nextEntry()
        
    # completed 999 repeats of 'repeatloop'
    
    
    # ------Prepare to start Routine "Rest"-------
    t = 0
    RestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5 = event.BuilderKeyResponse()
    if blocks.thisN + 1 == blocks.nTotal:
        continueRoutine = False
    # keep track of which components have finished
    RestComponents = [restPhase, key_resp_5]
    for thisComponent in RestComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Rest"-------
    while continueRoutine:
        # get current time
        t = RestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *restPhase* updates
        if t >= 0.0 and restPhase.status == NOT_STARTED:
            # keep track of start time/frame for later
            restPhase.tStart = t
            restPhase.frameNStart = frameN  # exact frame index
            restPhase.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_5.keys = theseKeys[-1]  # just the last key pressed
                key_resp_5.rt = key_resp_5.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rest"-------
    for thisComponent in RestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    blocks.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        blocks.addData('key_resp_5.rt', key_resp_5.rt)
    
    # the Routine "Rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed len(condFiles) repeats of 'blocks'


# ------Prepare to start Routine "SignOut"-------
t = 0
SignOutClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
SignOutComponents = [goodbye, key_resp_2]
for thisComponent in SignOutComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "SignOut"-------
while continueRoutine:
    # get current time
    t = SignOutClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *goodbye* updates
    if t >= 0.0 and goodbye.status == NOT_STARTED:
        # keep track of start time/frame for later
        goodbye.tStart = t
        goodbye.frameNStart = frameN  # exact frame index
        goodbye.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['g'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SignOutComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SignOut"-------
for thisComponent in SignOutComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "SignOut" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
