import pyautogui



MHposMonkeyLeftX = 945
MHposMonkeyY = 630
MHposMonkeyRightX = 1070
MHposChinookIconX = 400
MHposChinookIconY = 1030

def MovingHouse():
    for i in range(1000):
        pyautogui.moveTo(posChinookIconX,posChinookIconY,1)
        pyautogui.leftClick()
        pyautogui.moveTo(posMonkeyLeftX, posMonkeyY,duration=1)
        pyautogui.dragTo(x=posMonkeyRightX,y=posMonkeyY,duration=1,button="left")
        pyautogui.sleep(1)
        pyautogui.moveTo(posChinookIconX,posChinookIconY,1)
        pyautogui.leftClick()
        pyautogui.moveTo(posMonkeyRightX,posMonkeyY, duration=1)
        pyautogui.dragTo(x=posMonkeyLeftX,y=posMonkeyY,duration=1,button="left")
        pyautogui.sleep(1)

B500 = 0

def Bloontona500():
    pass

FF = 0

def FreakyFriday():
    pass

TTDposMonkeyX = 580
TTDposMonkeyY = 1035
TTDposUpgrade1X = 1550
TTDposUpgrade1Y = 470
TTDposUpgrade2X = TTDposUpgrade1X
TTDposUpgrade2Y = 630
TTDposSellX = 1550
TTDposSellY = 900
TTDposBuyMonkeyX = 1850
TTDposBuyMonkeyY = 200


def ToolsToDarwin():
    for i in range(6200):
        pyautogui.moveTo(TTDposBuyMonkeyX,TTDposBuyMonkeyY)
        pyautogui.dragTo(x=TTDposMonkeyX,y=TTDposMonkeyY,duration=1,button='left')
        pyautogui.sleep(1)
        pyautogui.leftClick()
        pyautogui.moveTo(TTDposUpgrade1X, TTDposUpgrade1Y)
        pyautogui.sleep(1)
        for i in range(5):
            pyautogui.leftClick()
        pyautogui.moveTo(TTDposUpgrade2X,TTDposUpgrade2Y)
        pyautogui.sleep(1)
        for i in range(2):
            pyautogui.leftClick()
        pyautogui.moveTo(TTDposSellX,TTDposSellY)
        pyautogui.sleep(1)
        pyautogui.leftClick()

TGCPlayX=960
TGCPlayY=870
TGCMenuX=1590
TGCMenuY=50
TGCHomeX=850
TGCHomeY=850


def TheGreatestChallenge():
    for i in range(200):    
        pyautogui.moveTo(TGCPlayX, TGCPlayY)
        pyautogui.sleep(1)
        pyautogui.leftClick()
        pyautogui.sleep(3)
        pyautogui.moveTo(TGCMenuX, TGCMenuY)
        pyautogui.sleep(1)
        pyautogui.leftClick()
        pyautogui.moveTo(TGCHomeX, TGCHomeY)
        pyautogui.sleep(1)
        pyautogui.leftClick()
        pyautogui.sleep(2)


# MovingHouse()

# FreakyFriday()

# ToolsToDarwin()

TheGreatestChallenge()