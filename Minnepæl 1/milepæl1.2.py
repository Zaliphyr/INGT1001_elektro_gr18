from sense_hat import SenseHat
from time import sleep, time
from datetime import datetime as dt

from milepæl1 import calc_pressure_Pa

senseHat = SenseHat()

#Konstanter
a = -0.0065
R = 287.06
g_0 = 9.81
N = 200

path = "/home/p1/Documents" #Skriv din egen mappe du ansker dataen skal havne i 
path = path.rstrip("/")+"/høydedata.csv" #formaterer path riktig for & få filtypen vi vil ha

#Variabler
T_116 = 16 + 273.15
p_1= 100000 #Trykket målt ved heyden h_1.
h_1 = 0 #Vi gjør målingene relative dersom vi ønsker ved à sette h_1 = e


def write_to_log(write_data):
    with open (path, "a") as f:
        f.write(str(write_data) + "\n")

def calc_pressure_pa():
    p = 0
    for _ in range(N):
        p += senseHat.pressure
        sleep(1/N)
    return p*100/N #vi vil ha p 1 Pa, og multipliserer derfor med 100 etter vi deler på N

def stick_down():
    for e in senseHat.stick.get_events():
        if e.direction =='down':
            return 1

senseHat.show_message("Venstre: Mål     Høyre: Kalibrer     Ned: Avbryt", 0.03)

while True:
    event = senseHat.stick.wait_for_event()
    if event.direction == "left":
        start = time()
    
        write_to_log("\n\n### New measurements started at: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " ###\n")

        while stick_down()!=1:
            p = calc_pressure_Pa()
            h = (T_1 / a) * ( (p/p_1)**(-a*R/g_0) - 1) + h_1

            now = time() - start

            write_to_log(str(now) + "," + str(p) + "," + str(h) + "," + str(senseHat.temp))

            senseHat.show_message(str(round(h,2)) + "m", 0.03)

        if event.direction == "right":
            while stick_down()!=1:
                T_1 = senseHat.temp + 273.15
                p_1 = calc_pressure_pa()
                senseHat.show_message(str(int(p_1)) + " Pa " +str(round(T_1)) + "K", 0.03)
