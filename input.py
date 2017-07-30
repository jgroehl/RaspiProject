import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Button:
	"""This class represents a hardware button that inputs via GPIO"""
	pressed = False
	counter = 0
	gpioPort = 0
	name = "Button"
	lastChecktime = 0
	checkinterval=0.1
	
	def __init__(self, gpioPin, buttonName):
		self.gpioPort=gpioPin
		self.name = buttonName
		GPIO.setup(gpioPin, GPIO.IN)
		

	def checkInput(self):
		if (time.time() - self.lastChecktime) > self.checkinterval:
			if GPIO.input(self.gpioPort):
				if not self.pressed:
					self.counter = self.counter+1
					self.pressed = True
					print("Pressed "+self.name+": "+str(self.counter))
			else:
				if self.pressed:
					self.pressed = False
			self.lastChecktime = time.time()


buttonList = []
buttonList.append(Button(26, "Right"))
buttonList.append(Button(19, "A"))
buttonList.append(Button(13, "Start"))
buttonList.append(Button(6, "Select"))
buttonList.append(Button(21, "Left"))
buttonList.append(Button(20, "B"))
buttonList.append(Button(16, "Up"))
buttonList.append(Button(12, "Down"))


while True:
	for btn in buttonList:
		time.sleep(0.01)
		btn.checkInput()
