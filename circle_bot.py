import pyautogui
import math

def circle():
    a,b = pyautogui.position()
    w = 20
    m = (2*math.pi)/w
    r = 200      

    while 1:
        for i in range(w+1):
            x = int(a+r*math.sin(m*i))  
            y = int(b+r*math.cos(m*i))
            pyautogui.moveTo(x, y, duration = 0.2)

if __name__ == "__main__":
    try:
        circle()
    except KeyboardInterrupt as e:
        print("Arkajyoti saved you today ! ;-)")
