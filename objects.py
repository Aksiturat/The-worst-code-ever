from values import *
from terrain import *
import time
import math
global x_field
global y_field
drawable=[]


class panel(object):
	def __init__(self):
		global drawable
		drawable=[]
		drawable.append(button("labir_build",w-p,w,p*2))
		drawable.append(button("b_add",w-p,w,p))
		drawable.append(button("b_build",w-p,w,0))
		drawable.append(button("left",w-p,w-p/2,p*4))
		drawable.append(button("right",w-p/2,w,p*4))
		drawable.append(slider("x_field",border*1/3,s,border,w-border))
		drawable.append(slider("y_field",border*2/3,s,border,w-border))
		drawable.append(stick("control_movement",w*2/3,w,h-w*1/3))
		drawable.append(stick("control_rotation",w*0,w*1/3,h-w*1/3))
		
class stick(panel):
	def __init__(self,name,a,b,c):
		self.name=name
		self.a=a
		self.b=b
		self.c=c
		self.joy_x=0
		self.joy_y=0
		self.r=abs(a-b)/2
		self.pressed=0
		self.count=time.time()
	def released(self):
		self.joy_x=0
		self.joy_y=0
		self.pressed=0
	def inside_borders(self):
		x_mouse, y_mouse = pygame.mouse.get_pos()
	
		if(self.pressed or ((x_mouse-((self.a+self.b)/2))**2+(y_mouse-self.c)**2)**(1/2)<(abs(self.a-self.b))/2):
			self.pressed=1
			if (((x_mouse-((self.a+self.b)/2))**2+(y_mouse-self.c)**2)**(1/2)<(abs(self.a-self.b))/2):
				self.joy_x=(x_mouse-((self.a+self.b)/2))/((abs(self.a-self.b))/2)
				self.joy_y=(y_mouse-self.c)/((abs(self.a-self.b))/2)
			else:
				self.joy_x=(x_mouse-((self.a+self.b)/2))/((abs(self.a-self.b))/2)
				self.joy_y=(y_mouse-self.c)/((abs(self.a-self.b))/2)
				
				self.joy_x=math.cos(arctg(self.joy_x,self.joy_y))
				self.joy_y=math.sin(arctg(self.joy_x,self.joy_y))
			

			if(self.name=="control_movement"):
				
				player.entity_x+=self.joy_x*player.speed[0][2]/5
				player.entity_y+=self.joy_y*player.speed[0][2]/5
			if(self.name=="control_rotation"):
				player.entity_rx+=self.joy_x**3*player.speed[1][0]
				player.entity_ry+=self.joy_y**3*player.speed[1][0]
			
			
	def draw(self):
		pygame.draw.circle(screen,(0,0,0),((self.a+self.b)/2,self.c),abs(self.a-self.b)/2)
		pygame.draw.circle(screen,(200,0,0),((self.a+self.b)/2+self.joy_x*self.r,self.c+self.joy_y*self.r),abs(self.a-self.b)/5)
def arctg(x,y):
	if(x==0):
		if(y<0):
			return(math.pi*3/4)
		if(y>=0):
			return(math.pi/4)
	else:
		if(x>0):
			return(math.atan(y/x))
		if(x<0):
			return(math.pi+math.atan(y/x))
class button(panel):
	def __init__(self,name,a,b,c):
		self.name=name
		self.a=a
		self.b=b
		self.c=c
		self.count=time.time()
	def inside_borders(self):
		global print_margin
		x_mouse, y_mouse = pygame.mouse.get_pos()
		
		
		if( ((x_mouse-((self.a+self.b)/2))**2+(y_mouse-self.c)**2)**(1/2)<(abs(self.a-self.b))/2):
			if(self.name=="left"):
				print_margin-=1
			if(self.name=="right"):
				print_margin+=1
			if(time.time()-self.count>0.6 and self.name=="labir_build"):
				
				terra()
				terra_smooth()   
			
				labir_shape()
			#print([str(round(time.time(),2))])
#			
#			print([str(round(time.time()-self.count,2))])
			self.count=time.time()
	def draw(self):
		pygame.draw.circle(screen,(0,0,0),((self.a+self.b)/2,self.c),abs(self.a-self.b)/2)
	###	
class slider(panel):
	def __init__(self,name,slider_y,slider_w,slider_x1,slider_x2):
		self.name=name
		self.slider_y=slider_y
		self.slider_x1=slider_x1
		self.slider_x2=slider_x2
		self.slider_w=slider_w
		#self.slider_body=can.create_oval(slider_x1,slider_y-slider_w,slider_x2,slider_y+slider_w,fill="grey", width=s/8,outline="black")
		self.slider_slider=None
		self.slider_position=0.5
		self.value_to_position()
	def draw(self):
		pygame.draw.ellipse(screen, (100,100,100),(self.slider_x1,self.slider_y-self.slider_w,self.slider_x2-self.slider_x1,2*self.slider_w))
		pygame.draw.ellipse(screen, (200,100,100),((self.slider_x1+self.slider_position*(self.slider_x2-self.slider_x1)-self.slider_w,self.slider_y-1.5*self.slider_w,self.slider_w*2,3*self.slider_w)))
	#	print(["aaa"])
		
	def inside_borders(self):
		
		x_mouse, y_mouse = pygame.mouse.get_pos()
		if(self.slider_x1<x_mouse<self.slider_x2 and self.slider_y-self.slider_w<y_mouse<self.slider_y+self.slider_w):
		
			self.slider_position=(x_mouse-self.slider_x1)/(self.slider_x2-self.slider_x1)
			self.value_to_position()
	def value_to_position(self):
		global x_field,y_field
		if(self.name=="x_field"):
				x_field=int(self.slider_position*16)*3
		if(self.name=="y_field"):
				y_field=int(self.slider_position*24)*3
		
class entity:
	def __init__(self,entity_x,entity_y,type):
		self.entity_x,self.entity_y=entity_x,entity_y
		self.entity_rx,self.entity_ry=-90,90
		
		if(type=="human"):
			self.health=[5.0,64,64,64,64,48,128,32]
			self.protection=[[0.0,0.4],8,8,12,12,20,16,[4,8]]
			self.pain=[0.5,2,2,4,4,7,2,[4.5,3]]
			self.speed=[[4,6,8,12,16],[8]]
			self.motion=[0,0,0]
	
	def draw(self):
		pygame.draw.circle(screen,(64,0,64),(player.entity_x,player.entity_y),6)
		pygame.draw.circle(screen,(128,0,64),(player.entity_x+math.cos(math.radians(self.entity_rx))*4,player.entity_y+math.sin(math.radians(self.entity_rx))*4),2)
			#blood larm rarm lleg rleg head, torso, stomack
#	def ranges(self):
	def view(self):
		global particles
		deg=int(self.entity_rx-FOV/2)
		screen_h=0.2*h
		max_len=int(w/3)
		from terrain import visible_objects
		for visible_object in visible_objects:
			if((self.entity_x-visible_object[0])**2+(self.entity_y-visible_object[1])**2>(self.entity_x-visible_object[2])**2+(self.entity_y-visible_object[3])**2):
				visible_object[4]=((self.entity_x-visible_object[2])**2+(self.entity_y-visible_object[3])**2)
			else:
				visible_object[4]=((self.entity_x-visible_object[0])**2+(self.entity_y-visible_object[1])**2)
		visible_objects.sort(key=lambda tup: tup[4])
		
		
		object_r1,object_r2=round((math.degrees(arctg((self.entity_x-visible_objects[0][0]),(self.entity_y-visible_objects[0][1])))+180)%360,0),round((math.degrees(arctg((self.entity_x-visible_objects[0][2]),(self.entity_y-visible_objects[0][3])))+180)%360,0)
		screen.blit((my_font.render(str(deg%360)+" "+str((deg+FOV)%360), False, (0, 0, 0))), (w/2,h*4.5/6))
		
		screen.blit((my_font.render(str(object_r1)+" "+str(object_r2), False, (0, 0, 0))), (w/2,h*4.7/6))
	
	
	
	
			
	#	if(deg%360<((deg+FOV)%360)):
#			zone_1=[[deg%360,((deg+FOV)%360)]]
#		else:
#			zone_1=[[0,((deg+FOV)%360)][deg%360,360]]
	#	screen.blit((my_font.render(str(inview(zone_1,object_r1,object_r2)), False, (0, 0, 0))), (w/2-100,h*4.9/6))
	
	
	
	
	#	for i in range (10):
	#		object_r1,object_r2=arctg((self.entity_x-visible_object[0]),(self.entity_y-visible_object[1])),arctg((self.entity_x-visible_object[2]),(self.entity_y-visible_object[3]))
			#object_rad1,object_rad2=(self.entity_x-visible_object[0])**2+(self.entity_y-visible_object[1])**2,(self.entity_x-visible_object[2])**2+(self.entity_y-visible_object[3])**2
#			pygame.draw.polygon(screen,(64,64,64),(ray_n,0.6*h-4*proection/len),(ray_n,0.6*h+4*proection/len))
		for ray_n in range(0,w):
			len=0
			
			while(len<max_len):
			
	#			if(0<int(self.entity_x+len*math.cos(math.radians(deg)))<w and 0<int(self.entity_y+len*math.sin(math.radians(deg)))<h):
					try:	
						if(particles[int(self.entity_x+len*math.cos(math.radians(deg)))][int(self.entity_y+len*math.sin(math.radians(deg)))]==1):
					
							break
					except:
						break
					len+=0.5
					#	a=int(self.entity_x+len*math.cos(math.radians(deg)))
				#		b=int(self.entity_y+len*math.sin(math.radians(deg)))
					
	#			else:
			#		break
	#	screen.blit((my_font.render(str(a), False, (0, 0, 0))), (w/2,h*4.5/6))
	#	screen.blit((my_font.render(str(b), False, (0, 0, 0))), (w/2,h*5/6))

		#	pygame.draw.line(screen,(0,64,64),(self.entity_x,self.entity_y),(int(self.entity_x+len*math.cos(math.radians(deg))),int(self.entity_y+len*math.sin(math.radians(deg)))))
	#		if ray_n==w//2:
				#screen.blit((my_font.render(str([particles[int(self.entity_x+len*math.cos(math.radians(deg)))][int(self.entity_y+len*math.sin(math.radians(deg)))],[int(self.entity_x+len*math.cos(math.radians(deg)))],"  ",[int(self.entity_y+len*math.sin(math.radians(deg)))]]), False, (0, 0, 0))), (w/2,h*5/6))
			pygame.draw.line(screen,(0,64,64),(ray_n,0.6*h-4*proection/len),(ray_n,0.6*h+4*proection/len))
			deg+=FOV/w
#			
def inview(zone_1,object_r1,object_r2):
#	screen.blit((my_font.render(str(zone_1), False, (0, 0, 0))), (w/2,h*4.9/6))
	if(abs(object_r1-object_r2)<180):
		if(object_r1<object_r2):
			zone_2=[object_r1,object_r2]
		else:
			zone_2=[object_r2,object_r1]
	else:
		if(object_r1<object_r2):
			zone_2=[[0,object_r1],[object_r2,360]]
		else:
			zone_2=[[0,object_r2],[object_r1,360]]
	for i in range(len(zone_1)):
		if(zone_1[i][0]<zone_2[0]<zone_1[i][1] and zone_1[i][0]<zone_2[1]<zone_1[i][1] ):
			
			zone_1.insert(i,[zone_2[1],zone_1[i][1]])
			zone_1.insert(i,[zone_1[i][0],zone_2[0]])
			zone_1.pop(i+2)
		#	zone_1[i]=[[zone_1[i][0],zone_2[0]],[zone_2[1],zone_1[i][1]]]
		if(zone_1[i][0]<zone_2[0]<zone_1[i][1] and zone_1[1]<=zone_2[1]):
			
			zone1[i]=[zone_1[i][0],zone_2[0]]
		if(zone_1[i][0]<zone_2[1]<zone_1[i][1] and zone_2[0]<=zone_1[0]):
			zone1[i]=[zone_2[1],zone_1[i][1]]
	return (zone_1)

player=entity(w/2,400,"human")
enemy=entity(400,200,"human")
panel()
