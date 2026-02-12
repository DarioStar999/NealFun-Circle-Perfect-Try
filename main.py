from pynput.mouse import Button, Controller
import ctypes, time, math
user32 = ctypes.windll.user32
x = user32.GetSystemMetrics(0) #78 all monitor
y = user32.GetSystemMetrics(1) #79 all monitor
center = x//2 , y//2
print("x,y:",x,y)
print("center",center)
mouse = Controller()
print("Mouse position: {}".format(mouse.position))
print("waiting 5 second..")
time.sleep(5)
angle = 0
radius = 400
x = center[0]+radius * math.cos(angle)
y = center[1]+radius * math.sin(angle)
mouse.position = (int(x),int(y))
mouse.press(Button.left)
while angle < 2 * math.pi:
    x = center[0]+radius * math.cos(angle)
    y = center[1]+radius * math.sin(angle)
    mouse.position = (int(x),int(y))
    angle += 0.1
    time.sleep(0.01)
mouse.release(Button.left)