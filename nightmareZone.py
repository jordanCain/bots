import pyautogui
from pynput.mouse import Listener
import random
import time
import numpy
from tkinter import *

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pyautogui.PAUSE = 0  # Default: 0.1

for i in range(1, 0, -1):
    print(i)
    time.sleep(1)
print('Starting')

bagLocation = pyautogui.locateCenterOnScreen('./images/bagIcon.png')
bagLocation = bagLocation[0]-2,bagLocation[1]-3
skillsLocation = pyautogui.locateOnScreen('./images/skillsIcon.png')
skillsLocation = skillsLocation[0]-4,skillsLocation[1]-12
strengthLocation = skillsLocation[0]-7,skillsLocation[1]+75

def openBag():
    print('Opening bag')
    if(pyautogui.locateOnScreen('./images/bagIcon.png')):
        targetCursorPoint = bagLocation[0]+random.randint(0,24), bagLocation[1]+random.randint(0,26)
        moveToTarget(targetCursorPoint)
        pyautogui.click()
    else:
        print('Unable to locate bag')

def openSkills():
    print('Open skills')
    if(pyautogui.locateOnScreen('./images/skillsIcon.png')):
        targetCursorPoint = skillsLocation[0]+random.randint(0,30), skillsLocation[1]+random.randint(0,30)
        moveToTarget(targetCursorPoint)
        pyautogui.click()
    else:
        print('Unable to locate skills')

def hoverStrength():
    print('Hover strength')
    targetCursorPoint = strengthLocation[0]+random.randint(0,48), strengthLocation[1]+random.randint(0,9)
    moveToTarget(targetCursorPoint)

def drinkAbsorbtion():
    absorbtionPotionLocation = pyautogui.locateOnScreen('./images/absorbtionPotion.png')
    if(absorbtionPotionLocation):
        targetCurosPoint = absorbtionPotionLocation[0] - 4 + random.randint(0,14), absorbtionPotionLocation[1]+random.randint(2,21)
        moveToTarget(targetCurosPoint)
        for i in range(7):
            pyautogui.click()
            time.sleep(random.randint(56,94)/100)

def getLowestCombatPotion():
    if (pyautogui.locateOnScreen('./images/combatPotions/combatPotion1.png')):
        return pyautogui.locateOnScreen('./images/combatPotions/combatPotion1.png')
    if (pyautogui.locateOnScreen('./images/combatPotions/combatPotion2.png')):
        return pyautogui.locateOnScreen('./images/combatPotions/combatPotion2.png')
    if (pyautogui.locateOnScreen('./images/combatPotions/combatPotion3.png')):
        return pyautogui.locateOnScreen('./images/combatPotions/combatPotion3.png')
    if (pyautogui.locateOnScreen('./images/combatPotions/combatPotion4.png')):
        return pyautogui.locateOnScreen('./images/combatPotions/combatPotion4.png')

def drinkCombatPotion():
    combatPotionLocation = getLowestCombatPotion()
    if(combatPotionLocation):
        targetCursorPos = combatPotionLocation[0] - 4 + random.randint(0,14), combatPotionLocation[1] + random.randint(2,21)
        moveToTarget(targetCursorPos)
        pyautogui.click()
        offScreenMouseLocation = combatPotionLocation[0] + random.randint(150, 250), combatPotionLocation[1] + random.randint(0, 300)
        moveToTarget(offScreenMouseLocation)

def eatRockcake():
    if not (pyautogui.locateOnScreen('./images/minimumHealth.png')):
        rockcakeLocation = pyautogui.locateOnScreen('./images/rockcake.png')
        targetCursorPos = rockcakeLocation[0] + random.randint(0,20), rockcakeLocation[1] + random.randint(0,21)
        moveToTarget(targetCursorPos)
        
        keepClicking = True
        while(keepClicking):
            for i in range(random.randint(2,7)):
                pyautogui.click()
                time.sleep(random.randint(12, 19)/100)
            if(pyautogui.locateOnScreen('./images/minimumHealth.png')):
                keepClicking = False
        offScreenMouseLocation = rockcakeLocation[0] + random.randint(150, 250), rockcakeLocation[1] + random.randint(0, 300)
        moveToTarget(offScreenMouseLocation)
    else:
        print('No need to eat rock cake')

def shouldLowerHealth():
    if not (pyautogui.locateOnScreen('./images/minimumHealth.png')):
        print('might lower health')
        if random.randint(1,6) == 1:
            return True
    print('Not lowering health')
    return False

def shouldDrinkAbsorbtion():
    # if(pyautogui.locateOnScreen('./images/absorbtionPotions/700Absorbs.png') or pyautogui.locateOnScreen('./images/absorbtionPotions/700Absorbs2.png')):
    #     print('found 7**')
    #     if random.randint(1,12) == 1:
    #         return True
    if( pyautogui.locateOnScreen('./images/absorbtionPotions/600Absorbs.png') or 
        pyautogui.locateOnScreen('./images/absorbtionPotions/600Absorbs2.png') or 
        pyautogui.locateOnScreen('./images/absorbtionPotions/600Absorbs3.png')):
        print('found 6**')
        if random.randint(1,10) == 1:
            return True
    if(pyautogui.locateOnScreen('./images/absorbtionPotions/500Absorbs.png') or pyautogui.locateOnScreen('./images/absorbtionPotions/500Absorbs2.png')):
        print('found 5**')
        if random.randint(1,6) == 1:
            return True
    if(pyautogui.locateOnScreen('./images/absorbtionPotions/400Absorbs.png') or pyautogui.locateOnScreen('./images/absorbtionPotions/400Absorbs2.png')):
        print('found 4**')
        if random.randint(1,5) == 1:
            return True
    if(pyautogui.locateOnScreen('./images/absorbtionPotions/200Absorbs.png')):
        print('found 2**')
        if random.randint(1,2) == 1:
            return True
    if(pyautogui.locateOnScreen('./images/absorbtionPotions/200Absorbs.png')):
        print('found 2**')
        return True

def logout():
    moveToTarget(pyautogui.locateCenterOnScreen('./images/logoutIcon.png'))
    pyautogui.click()
    moveToTarget(pyautogui.locateCenterOnScreen('./images/logoutButton.png'))
    pyautogui.click()
    
def moveToTarget(targetPoint):
    startPoint = pyautogui.position()
    steps = getSteps(startPoint, targetPoint)

    x = numpy.linspace(startPoint[0], targetPoint[0], num=steps, dtype='int')
    y = numpy.linspace(startPoint[1], targetPoint[1], num=steps, dtype='int')

    for i in range(x.__len__()):
        pyautogui.moveTo(x[i],y[i])

def getSteps(initialCursorPoint, targetCursorPoint):
    steps = (abs(initialCursorPoint[0] - targetCursorPoint[0]) + abs(initialCursorPoint[1] - targetCursorPoint[1])) / 2
    if steps > 60 :
        steps = steps/2
    return int(round(steps))


# Decide if should eat rock cake
# Drink super combat once every 17 minutes (somewhere between 17 and 18...)
# Drink absorbtion 
iterationCount = 0
totalSleepTime = 0
iterationSleeptime = 0
while (True):
    if not (pyautogui.locateOnScreen('./images/nightmareActive.png')):
        print('Exiting')
        time.sleep(random.randint(5,60))
        logout()
        break
    if (iterationCount >= 14 and iterationSleeptime >= 870):
        drinkCombatPotion()
        eatRockcake()
        iterationCount = 0
        iterationSleeptime = 0
    if (shouldDrinkAbsorbtion()):
        drinkAbsorbtion()
        eatRockcake()
    if (shouldLowerHealth()):
        eatRockcake()
    sleeptime = random.randint(40,80)
    iterationCount += 1
    iterationSleeptime += sleeptime
    totalSleepTime += sleeptime
    print(  'iteration count: ' + str(iterationCount) + 
            ' sleeping: ' + str(sleeptime) + 
            ' iteration sleep time: ' + str(iterationSleeptime) +
            ' totalSlept: ' + str(totalSleepTime))
    time.sleep(sleeptime)
