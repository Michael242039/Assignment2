#Created by: Michael Taylor
#Created on: September 30, 2017
#Created for ICS3U
#This program calculates the height of a man based off of how long hes been falling
import ui

GRAVITY = 9.81
	
def calculate_button_pressed(sender):
	seconds = float(view['seconds_input'].text)
	view['seconds_label'].text = "{0:.2f}".format(seconds)
	height = (100 - (GRAVITY*seconds)/2)
	
	if height < 0:
		height = 0
	
	view['man'].y = -(height*5)+500
	view['height_label'].text = 'height: ' + "{0:.2f}".format(height) + 'm'

view = ui.load_view()
view.present('sheet')
