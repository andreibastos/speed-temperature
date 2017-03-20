#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
import time

PWM_FREQUENCY = 100  #Hertz
GPIO_FAN = 5 #pin number

#configurando GPIO
# import RPi.GPIO as IO
# IO.setmode (IO.BCM)
# GPIO.setup(GPIO_FAN ,GPIO.OUT)
# pwm=GPIO.PWM(GPIO_FAN,100)     #Configura para 100 Hz
# pwm.start(100)

max_temperatura = 0; 
min_temperatura = 0;

while 1:
		

	#ler temperatura
	temperatura = call(["/opt/vc/bin/vcgencmd", "measure_temp"])
	#salva em algum lugar pra ver historico


	#verifica se a temperatura atual é a maior registrada
	if temperatura > max_temperatura:
		max_temperatura = temperatura

	diff_temperatura = max_temperatura - min_temperatura

	duty = 0
	if diff_temperatura!=0:
		duty = temperatura/(diff_temperatura*1.2)

	print duty

	time.spleep(1);





