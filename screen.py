from mss import mss
import datetime
import os
import sys
import time
tiempo_espera = 15
fechayhora = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
timeout = time.time() + tiempo_espera


def TimeOut():
    if time.time()> timeout:
        return True
    else: 
        return False



while True:
    ca = TimeOut()
    if ca == True:
        with mss() as captura:
            captura.shot(output = "capturas//captura "+fechayhora+".png")
        timeout = time.time() + tiempo_espera
        fechayhora = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

#OnixBreak

