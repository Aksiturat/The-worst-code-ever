from tkinter import *
from PIL import Image
from math import *

import matplotlib.colors
import pygame 
import time
import math
from values import *
from objects import *
#from terrain import *
try:
    import android
    andr = True
except ImportError:
    andr = False
#root=Tk()

#w=root.winfo_screenwidth()
#h=root.winfo_screenheight()

#can=Canvas (root, width=w, height=h, bg="#aaffff")

#can.pack()




def mousedown():
	global drawable
	for figure in drawable:
		figure.inside_borders()
def mousemove():
	global drawable
	for figure in drawable:
		figure.inside_borders()
def mouseup():
	
	for figure in drawable:
		try:
			figure.released()
		except:
			None
	
def gameplay():
	while True:
		bip=time.time()
		global print_obj
		global pressed
		global drawable
		global draw_hexes
		
		global labir_border
		global print_margin
		
		try:
			pressed
		except:
			pressed=0
		try:
				for i in range (0,len(print_obj)):
					screen.blit(print_obj[i], (300,300))
		
		except:
				None
		screen.fill((240,120,240))
		for event in pygame.event.get():

			if (event.type==pygame.QUIT):
				exit()
			if event.type == pygame.MOUSEBUTTONUP:
				pressed=0
				mouseup()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pressed=1
				mousedown()

				
			if event.type == pygame.MOUSEMOTION:
				pressed=1
				mousemove()
			
		if(pressed==1):
			mousemove()
			pygame.draw.circle(screen, (200,0,0),(300,300),40)

			
		for figure in drawable:
			figure.draw()
				
			
		
		draw(0,"flat")	
		
		draw(labir_border,"labir")
		
			
		try:
			for i in range(0,len(print_obj)):
				for j in range(0,len(print_obj[i])):
					screen.blit(print_obj[i][j], (print_margin*5+p*2*(i//20),p*5+p/3*(i%20)))
		except:
			None
		player.draw()
		player.view()
	#	counter=0
		#for i in range(w):
#			for j in range(h):
#				if(particles[i][j]):
#					counter+=1
		screen.blit((my_font.render(str(bip-time.time()), False, (0, 0, 0))), (w/2,h*2/3))
		screen.blit((my_font.render(str(y_field), False, (0, 0, 0))), (w/3,h*2/3))
	#	screen.blit((my_font.render(str(counter), False, (0, 0, 0))), (w/3,h*2.1/3))
		pygame.display.flip()
		fps.tick(FPS)
		
		


	

def to_hex(col ):
			temp1="#"
			for i in range(3):
				if(col[i]<16):
						temp1+="0"
				temp1+=hex(col[i])[2:]
			return(temp1)

			


		
		
def print(text):
	global print_margin
	global print_obj
	try: print_margin
	except: print_margin=0
	try: print_obj
	except: print_obj=[]
	try:
		global print_count
		print_count+=1
	
	except:
		print_count=0
	print_obj.append([])
	if(type(text)==int):
		print_obj[len(print_obj)-1].append(my_font.render(str(text), False, (0, 0, 0)))
	else:
		text_unite=""
		for print_word in range (len(text)):	
			text_unite+=str(text[print_word])
		print_obj[len(print_obj)-1].append(my_font.render(str(text_unite), False, (0, 0, 0)))
			

gameplay()
#root.mainloop()