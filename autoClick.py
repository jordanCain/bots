import pyautogui
import random
import time
import numpy

for i in range(1, 0, -1):
    print(i)
    time.sleep(1)
print('starting')

# alchLocation = pyautogui.locateOnScreen('alchIcon.png')
# pyautogui.moveTo(alchLocation)

#Make sure we start with mage book open
# print(pyautogui.locateOnScreen('mageBook.png'))
# pyautogui.click('mageBook.png')

# alchIconLocation = pyautogui.locateOnScreen('alchIcon.png')
# pyautogui.moveTo(alchIconLocation)
alchCount = 70

initialCursorPoint = pyautogui.position()

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

for i in range(350):
    if(random.randint(1,111) == 2):
        print("long sleep 17-40")
        time.sleep(random.randint(190, 400)/10)
    pyautogui.click()
    time.sleep(random.randint(18,57)/100)
    pyautogui.click()
    if(random.randint(1,35) == 5):
        target = initialCursorPoint[0] + (random.randint(-3,3)), initialCursorPoint[1] + (random.randint(-2,2))
        moveToTarget(target)
    time.sleep(random.randint(225,250)/100)
    if(random.randint(1,27) == 3):
        distractedWait = (random.randint(150,900)/100)
        print('distracted: ' + str(distractedWait))
        time.sleep(distractedWait)
        if(random.randint(1,3) == 3):
            target = initialCursorPoint[0] + (random.randint(-3,3)), initialCursorPoint[1] + (random.randint(-2,2))
            moveToTarget(target)