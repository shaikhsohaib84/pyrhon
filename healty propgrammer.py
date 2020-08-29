from pygame import mixer
import time
# import random
import datetime

# t = time.localtime().tm_hour #get current hour time
# c_hr = datetime.datetime.strptime(str(t), "%H") #convert  24hr into 12hr
# hr = c_hr.strftime("%I") #save convert  24hr into 12hr
flag = True
liter = 1

def water():
    min = time.localtime().tm_min
    global liter, flag
    while flag:
        if liter <= 3:  # For water
            n = 0
            while n < 3:  # for 3 time to drink water
                n += 1
                time.sleep(n*120)  # sleep for interval
                print(f"plz drink {liter}-l water\n")
                liter += 1
                mixer.init()
                mixer.music.load("water.mp3")
                mixer.music.set_volume(0.7)
                mixer.music.play(-1)
                acc = input("enter drank to stop\n")  # accept drank to stop water alarm
                if acc == "drank":
                    f = open("user.txt", "a+")
                    f.write(f"{liter} of Water drink at this Time : {time.asctime()} \n")
                    mixer.music.stop()
                else:
                    print("wrong input")
                    # water()
                    continue
        else:
            flag = False



def eye():
    print("time to excercise for eye")
    hr = int(time.localtime().tm_hour)
    flag = True
    while flag:
        if hr > 8:
            mixer.init()
            mixer.music.load("eye.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play(-1)
            e = input("enter eye to stop alarm\n")
            if e == "eye":
                f = open("user.txt", "a+")
                f.write(f"eye excersice at this Time : {time.asctime()} \n")
                mixer.music.stop()
                flag = False

def activity():
    print("time to excercise for body")
    hr = int(time.localtime().tm_hour)
    flag = True
    while flag:
        if hr > 8:
            mixer.init()
            mixer.music.load("phy.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play(-1)
            e = input("enter phy to stop alarm\n")
            if e == "phy":
                f = open("user.txt", "a+")
                f.write(f"physical activity at this Time : {time.asctime()} \n")
                mixer.music.stop()
                flag = False

if __name__ == '__main__':
    h = datetime.datetime.strptime(str(time.localtime().tm_hour), "%H") #get hours which is in 24hr format
    m = datetime.datetime.strptime(str(time.localtime().tm_min), "%M") #get min which is in 24hr format
    a = h.strftime("%I") #convert 24hours into 12hr format
    b = m.strftime("%M") #convert min into 12hr format
    mode = h.strftime("%p") #AM/PM
    print(f"{a}:{b}:{mode}")
    lst = [water, eye, activity]
    while 1:
        for i in range(len(lst)):
            if lst[i] == water:
                if a >="9" or a <= "5":
                        print("water time")
                        water()
                        print(time.sleep(int(a) * 60))
                        time.sleep(int(a)*60)

                else:
                    break
            elif lst[i] == eye:
                if a >="11" or a <= "5":
                    if mode >= "AM" or mode <= "PM":
                        print("eye time")
                        eye()
                        print(time.sleep(int(a) * 60))
                        time.sleep(int(a) * 60)
                else:
                    break
            elif lst[i] == activity:
                if a >="3" or a <= "5":
                        activity()
                        print(time.sleep(int(a) * 60))
                        time.sleep(int(a) * 60)
                else:
                    break