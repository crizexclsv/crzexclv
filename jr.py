import time
import sys
import os
from colorama import init, Fore, Style


init()


os.system('cls' if os.name == 'nt' else 'clear')


lyrics = [
    "Isip at ang puso, bat di'pa palayain",
    "Naka gapos sa kahapon ang init ng damdamin",
    "Paano? Saan? at Kailan ka yayakapin?,",
    "Sa pag ikot ko ng mundo ko sayo, whoa, palagi",
]


def typewriter(line, delay=00.20):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

print(
     Style.BRIGHT +
      Fore.RED + "Palagi" +
      Fore.WHITE + "    by Shanti Dope\n" + 
      Style.RESET_ALL)

for line in lyrics:
    typewriter(Fore.WHITE + line + Style.RESET_ALL)
    time.sleep(0.5)
