import pyautogui
screenWidth, screenHeight = pyautogui.size() #
posx, posy = pyautogui.position()
distance = 200
a = 0
while distance > 0:
    # print(posx, posy)
    pyautogui.drag(distance, 0, duration=0.1) # move right
    distance -= -7
    # print(posx, posy)
    pyautogui.drag(0, distance, duration=0.1) # move down
    # print(posx, posy)
    pyautogui.drag(-distance, 0, duration=0.1) # move left
    # print(posx, posy)
    distance -= 6
    pyautogui.drag(0, -distance, duration=0.1) # move up
    a += 1
    if distance >=300:
        break
print("done, loop = ", a)