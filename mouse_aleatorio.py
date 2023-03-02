# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:03:54 2022

@author: DJK8
"""

import pyautogui
import time
import random

#pyautogui.FAILSAFE = False

t0 = time.time()

#tempo de espera em segundos
t = 10

try:
    while True:
        print('Pressione Ctrl+C para sair...')
        
        
        dt = 1
        while dt <= t:
            print(dt, '/', t)
            dt += 1
            time.sleep(1)

        #time.sleep(t)
        
        x = random.randint(10, 1200)
        y = random.randint(10, 900)
        pyautogui.moveTo(x, y)
        pyautogui.press('shift')
        
        
except:
    print('Execução finalizada:', int(time.time() - t0), 'segundos')

