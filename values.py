import pygame 
from math import *
pygame.init()
global p
p=100
w,h=pygame.display.Info().current_w,pygame.display.Info().current_h
s=((w**2+h**2)**(1/2))/200
border=100
FPS=60
draw_hexes=[]
hexes_flat=0
hexes_labir=0
labir_border=0.2
FOV=90
print_margin=0
particles=[]
visible_objects=[[0,0,w,0,0],[0,h/2,w,h/2,0]]
proection=w/(2*tan(FOV/2))
for i in range(w):
	particles.append([])
	for j in range(h):
		particles[i].append([0])
x_field,y_field=32,32
screen = pygame.display.set_mode((w, h))
fps=pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
print_obj=[]
def print(text):
	global print_margin
	global print_obj
	try: print_margin
	except: print_margin=0
	
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
	
