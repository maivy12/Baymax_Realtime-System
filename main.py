print("Hello LAB2")
import time
from scheduler import *
from task1 import *
from task2 import *
import requests

scheduler = Scheduler()
scheduler.SCH_Init()

task1a = Task1(0)
task1b = Task1(1)

scheduler.SCH_Add_Task(task1a.Task1_Run, 1000, 5000)
scheduler.SCH_Add_Task(task1b.Task1_Run, 2000, 4000)

while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)
    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break

task1b.camera.release()
task1a.camera.release()
cv2.destroyAllWindows()