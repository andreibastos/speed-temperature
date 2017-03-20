#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call, Popen, PIPE
import time

PWM_FREQUENCY = 100  #Hertz
GPIO_FAN = 1 #pin number

#configurando GPIO
import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BCM)
GPIO.setup(GPIO_FAN ,GPIO.OUT)
GPIO.cleanup()
GPIO.setmode (GPIO.BCM)
GPIO.setup(GPIO_FAN ,GPIO.OUT) 
pwm=GPIO.PWM(GPIO_FAN,100)     #Configura para 100 Hz
pwm.start(100)

max_temperatura = 0; 
min_temperatura = 0;

while 1:
		

	#ler temperatura	
	temperatura = float(Popen("/opt/vc/bin/vcgencmd measure_temp", shell=True, stdout=PIPE).stdout.read().replace("temp=","").replace("'C","").replace("\n",""))
	print "temperatura atual: \t" + str(temperatura)  + "°C"


	#salva em algum lugar pra ver historico
	

	#verifica se a temperatura atual é a maior registrada
	if temperatura > max_temperatura:
		max_temperatura = temperatura

	diff_temperatura = max_temperatura - min_temperatura

	duty = 0
	if diff_temperatura!=0:
		duty = int((temperatura/(diff_temperatura*1.2))*100)

	print "duty: \t" + str(duty) + "%"
	pwm.ChangeDutyCycle(duty);
	print("\n")

	time.sleep(1);





