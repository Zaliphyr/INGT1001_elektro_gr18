
# FØRSTE KODE

# HVORDAN BEREGNE DETTE I EN SENSE HAT
"""
Vi har delt programmet vårt inn i flere hoveddeler. 
linje seks til åtte deklarerer vi et par konstante verdier som skal brukes videre i koden. 
Linje elleve til tretten består av variabler som fungerer som input til den hypsometriske ligningen vist på forrige side. 
Fra linje 15 repeterer vi koden som følger etter; da lagrer vi trykket oppgitt i Pa, og regner ut høyden fra variablene våre og 𝑝. 
Så skriver vi ut den beregnede høyden vår.
"""

from sense_hat import SenseHat

senseHat = SenseHat()

# Konstanter
a = -0.0065
R = 287.06
g_0 = 9.81

# Variabler
T_1 = 16 + 273.15       # Temperaturen målt ved h_1. Lag til 273.15 slik at man ikke glemmer at det oppgis i Kelvin
p_1 =                   # Trykket målt i Pa ved høyden h_1

h_1 = 50                # Høyden ved bakkenivå ved hovedbygget til NTNU er 45 meter. 
                        # Det er 50 ved realfagsbygget. Vi tar 50 fordi vi sannsynligvis
                        # er litt over bakken der vi sitter.
                        # Sett verdien til null for å gjøre målinger relative til måleområdet

while True:
    p = senseHat.pressure*100       # Lagrer trykket i Pa i stedet for hPa som en variabel

    h = (T_1/a) * ((p/p_1)**(-a*R/g_0) - 1) + h_1   # Den hyposometriske ligningen

	senseHat.show_message(str(round(h, 2))+"m", 0.08)   # Skriver resultatet til Sense Hat

"""
Trykket, temperaturen, og høyden ved punktet du måler på kan du skaffe eksternt for så å legge inn i koden. 
På en vanlig dag i KJL2 på NTNU vil nok temperaturen være 20.5 grader, og trykket 100 kPa. 
Test om koden fungerer ved å løfte Sense HAT fra gulvet og opp så høyt du klarer og observer høydeforskjellen mellom det den sier. 
Koden og formelen er egentlig egnet for utendørs bruk, men det er tilsvarende trykkfall innad i et rom også. 
Trykksensoren har en nøyaktighet på omtrent 0.01hPa, så den skal kunne merke veldig små forskjeller i høyde, 
omtrent 10cm nøyaktighet burde den ha, men i praksis vil vi se at eksterne faktorer slik som vind, pust, trykkendringer i været, og temperaturforskjeller kan påvirke sensoren. 
Nøyaktigheten ligger nok nærmere ±1 meter. «Støyete» data kan begrenses noe ved å utføre flere målinger og ta gjennomsnittet av de.
"""









# NESTE KODE

# SELVSTENDIGE REFERANSEPUNKT
"""
Sense HAT har jo muligheten til å måle både trykk og temperatur, og om du dermed vet hvilken høyde du allerede befinner deg på vil du ha nok informasjon til å kunne beregne din nye høyde uavhengig av ekstern data. 
For å få nøyaktig og utendørs data burde du være utendørs imens du måler referanseverdiene, og Sense HAT-en burde også ha vært utendørs og avslått en stund for ikke å måle feil temperatur. 
Rpi-en varmer seg nemlig ganske kraftig opp når den kjører, slik som de fleste datamaskiner. 
Nøyaktigheten vil nok fortsatt være god nok til å kunne måle med 2-3 meters feilmargin, så «fort-å-gæli» er akseptabelt i noen omstendigheter, dere får ta den vurderingen selv. 
Mål dermed høyden på KJL2 ved å sette bunnen av auditoriet som referansehøyde ℎ1 = 0, og bevege dere opp til toppen av trappen. 
Send kun ut én fra hver gruppe, så kan dere heller være heiagjeng fra der dere sitter; vi må ta smittevernet seriøst så vi slipper karantene dersom en i klassen blir smittet! 
Du kan også gjøre Sense HAT-en interaktiv for å kunne måle forskjellige data og lagre de nye temperatur- og trykk-målingene ute i felten framfor å kjøre to forskjellige koder og være nødt til å skrive inn de nye verdiene manuelt. 
Her er vårt forslag på hvordan gjøre dette, som er bygget videre fra den tidligere koden, og som også tar gjennomsnitlige målinger for å justere for «støydata»:
"""

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













# NESTE KODE

# LOGGE DATA

"""
Det finnes utallige mange måter å logge data på i Python, men den enkleste er ved bruk av open(). 
Vet vi at vi skal logge til én og samme fil kan det være veldig greit å gjøre om filskrivingen vår til en funksjon for å gjøre koden mer oversiktlig. 
Det kan eksempelvis se slik ut: 
"""

def write_to_log(write_data):
    with open (path, "a") as f:
        f.write(str(write_data) + "\n")

"""
Å bruke «with» vil føre til at filen lukkes automatisk etter vi har skrevet til den, hvor «path» er en variabel som er filplasseringen. 
Ved å lage en funksjon kan vi legge til ekstra linjer eller modifikasjoner, slik som «\n», som betyr «neste linje»/«next line» som skal skje hver gang noe skrives til filen. 
Vi kunne også ha lagt til tidspunktet målingen ble tatt på før dataen, eller en integer for å vise til hvilken linje med data vi nå er på.
"""












# NESTE KODE

# UT PÅ TUR

"""
Gruppa skal nå ta målinger av høydeforskjellen fra elektro ned til samfundet, eller ned til Rema 1000 Elgeseter. 
Husk å opprettholde smittevern. Dere skal bruke relativ høydemåling med data kalibrert etter bakken ved en av utgangene til elektro. 
Dataen skal logges med numpy, vi har laget et kodeeksempel under, og dersom dere ikke får fullført oppgaven innen timen er over, ta kontakt med en annen gruppe og spør om å kopiere målingene deres. 
Om dere har tid til overs på turen kan dere ta noen omveier eller løpe om kapp en plass og se om det synes i målingene. 
Sørg for ikke å avbryte målingene når de har begynt, da dere trenger eduroam for å skru de på igjen. 
Dere kan endre linje 45 slik at dere ikke KAN avbryte målingene dersom dere ønsker det
"""

from sense_hat import sense_hat
from time import sleep

sense = SenseHat()


# Konstanter
a = 0.0065
R = 287.06
g_0 = 9.81 
N = 200 

# Variabler
T_1 = 16 + 273.15 
p_1 = 100000    # Trykket målt i høyden h_1
h_1 = 0         # Vi gjør målingene relative dersom vi ønsker, ved å sette h_1 = 0

def calc_pressure_Pa():
    p = 0 
    for _ in range(N):
        p += sense.pressure 
        sleep(0.001)
    return p*100/N # Vi vil ha p i Pa, og multipliserer derfor med 100 etter vi deler på N


def stick_down():
    for e in sense.stick.get_events():
        if e.direction=='down':
            return 1


def write_to_log(write_data):
    with open("milepæl1_data.py", "a") as f:
        f.write(str(write_data) + "\n")

while True:

    sense.show_message("Venstre: mål - Høyre: Kalibrer - Ned: Avbryt", 0.05)

    event = sense.stick.wait_for_event()

    if event.direction == 'left':
        while stick_down()!=1:
            p = calc_pressure_Pa()
            h = (T_1 / a) * ( (p/p_1)**(-a*R/g_0) -1 ) + h_1
            sense.show_message(str(round(h,2))+"m",0.07)

    if event.direction == 'right':
        while stick_down()!=1:
            T_1 = sense.temp + 273.15
            p_1 = calc_pressure_Pa()
            sense.show_message(str(int(p_1))+" Pa "+str(T_1)+" K ", 0.07)

    








# FRIVILLIG KODE

# ETASJE VISUALISERING

"""
Videre kan dere dra til sentralbygget og ta heisen eller trappen for å finne høyden av bygget (eller så høyt dere kommer, tips: trappen går lengre enn heisen). 
Med den dataen kan dere beregne høyden per etasje. La oss så lage en visuell framvisning på Sense HAT som sier til deg hvilken etasje det er du befinner deg i. 
Her er det ikke så mye hjelp vi skal gi dere, kun en ramme for koden:
"""

from sense_hat import SenseHat

senseHat = SenseHat()

def draw(h):
    # Tegn hvilken etasje du er på
    return h

def calcEtasjer():
    # Konstanter
    a = -0.0065
    R = 287.06
    g_0 = 9.81

    # Variabler
    T_1 = 16 + 273.15
    p_1 =       # Trykket målt ved første etasje
    h_1 = 0     # Starthøyden (første etasje) er definert som 0
    h_e =       # Høyde mellom etasjene

    p = senseHat.pressure*100

    h =         # Hypsometrisk ligning

    etasje = h//h_e
    toppetasje = 14

    if etasje < 0:
        etasje = 0
    elif etasje > toppetasje:
        etasje = toppetasje
    
    return int(etasje)

while True:
    draw(calcEtasjer())


