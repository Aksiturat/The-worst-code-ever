from values import *

import time
from math import *
import random

def terra():
	from objects import x_field,y_field
	global hexes
	global hex_w
	global hex_h
	
	hexes=[]
	hex_w=((w-border*2)*2/(1.5*x_field+0.5))
	hex_h=hex_w*y_field/5*4*(1)
	for i in range(x_field):
		hexes.append([])
		for j in range(y_field):
			hexes[i].append(0)
			if((i+j)%2==0):
				hexes[i][j]=random.randint(0,36)
	
	
def terra_smooth():
	global hexes
	
	global hex_w
	global hex_h
	global hexes_flat
	from objects import x_field,y_field
	l_x,l_y=x_field-1,y_field-1
	hexes_flat=[]
	for i in range(x_field):
		hexes_flat.append([])
		for j in range(y_field):
			hexes_flat[i].append(0)
			if((i+j)%2==0):
				
				hexes_anable=[(i!=0 and j!=0),(i!=l_x and j!=0),(i!=0 and j!=l_y),(i!=l_x and j!=l_y),(i>1),(i<l_x-1)]
				hex_mid=0
				if(hexes_anable[0]):
					hex_mid+=hexes[i-1][j-1]
				if(hexes_anable[1]):
					hex_mid+=hexes[i+1][j-1]
				if(hexes_anable[2]):
					hex_mid+=hexes[i-1][j+1]
				if(hexes_anable[3]):
					hex_mid+=hexes[i+1][j+1]
				if(hexes_anable[4]):
					hex_mid+=hexes[i-2][j]
				if(hexes_anable[5]):
					hex_mid+=hexes[i+2][j]
				hex_mid/=sum(hexes_anable)
				
				hexes_flat[i][j]=hexes[i][j] + ((hex_mid-hexes[i][j] )*(1-1/(log(abs(hex_mid-hexes[i][j] )+1,2)+1)))
	#return(hexes_flat)
	print([len(hexes_flat),len(hexes_flat[0])])
def labir_shape():
	
	global hexes
	global hex_w
	global hex_h
	global hexes_labir
	global labir_border
	global labir_max_count
	from objects import x_field,y_field
	hexes_labir=[]
	labir_max_count=0
	xlab_field,ylab_field=(x_field*(1-labir_border*2)),(y_field*(1-labir_border*2))
	for i in range(int(xlab_field)):
		hexes_labir.append([])
		for j in range(int(ylab_field)+1):
	#		if((x_field-abs(y_field/2-j))*labir_border<=i<=(x_field+abs(y_field/2-j))*(1-labir_border)):
			if((0+(abs(ylab_field/2-j)/ylab_field*xlab_field*(2*0.3))<=i<=xlab_field-1-(abs(ylab_field/2-j)/ylab_field*xlab_field*(2*0.3)))):
				
					
				hexes_labir[i].append([1,0,0,0,0,0,0])
				labir_max_count+=1
			else:
				if(abs(y_field/2-j)==0):
					hexes_labir[i].append([0.5])
				else:
					hexes_labir[i].append([0])

		#print([int((x_field*(1-labir_border*2))/2-1),int(y_field*(1-labir_border*2)/2)*2,"nya"])
	labir_max_count=int(labir_max_count*0.5-20)
	print([int((x_field*(1-labir_border*2))/2-1),"kkk",int(y_field*(1-labir_border*2)/2)*2,"kkk"])
	labir_walls(int((x_field*(1-labir_border*2))/2-1),int(y_field*(1-labir_border*2)/2)*2)
	for i in range(len(hexes_labir)):
			for j in range(len(hexes_labir[0])):
				if((i+j)%2==0):
					
					
					jj=(j+round(labir_border*y_field,0))/2
					ii=(i+round(labir_border*x_field,0))/4*3
					if(hexes_labir[i][j][0]==2):
						#try:
							if(hexes_labir[i][j][1]):
								wall_build(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj),border+hex_w*(ii+0.75),border+hex_h/y_field*(jj))
							if(hexes_labir[i][j][2]):
								wall_build(border+hex_w*ii,border+hex_h/y_field*(jj+0.5),border+hex_w*(ii+0.25),border+hex_h/y_field*(jj))
							if(hexes_labir[i][j][3]):
								wall_build(border+hex_w*ii,border+hex_h/y_field*(jj+0.5),border+hex_w*(ii+0.25),border+hex_h/y_field*(jj+1))
							if(hexes_labir[i][j][4]):
								wall_build(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj+1),border+hex_w*(ii+0.75),border+hex_h/y_field*(jj+1))
							if(hexes_labir[i][j][5]):
								wall_build(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj+1),border+hex_w*(ii+1),border+hex_h/y_field*(jj+0.5))
							if(hexes_labir[i][j][6]):
								wall_build(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj),border+hex_w*(ii+1),border+hex_h/y_field*(jj+0.5))
						#except:
#							print(hexes_labir[i][j])
def wall_build(x1,y1,x2,y2):
	visible_objects.append([x1,y1,x2,y2,0])
#	print("heeelp")
	global particles
	tan=(y2-y1)/(x2-x1)
	
	for ii in range(int(x1),int(x2)+1):
			particles[int(ii)][int(y1+(ii-x1)*tan)]=1
#	if(y1!=y2):
#		tan=(x2-x1)/(y2-y1)
#		if(y1>y2):
#			y1,y2=y2,y1
#		for jj in range(int(y1),int(y2)+1):
#				try:
#					particles[int(x1+(jj-y1)*tan)][int(jj)]=1
#				except:
#					None
	
	#	particles[int(ii-0.5)][int(y1+(ii-0.5-x1)*tan)]=1
#		particles[int(ii)][int(y1+(ii-x1)*tan)]=1
				
def labir_walls(ii,jj):
	global hexes_labir
	global labir_exit
	global labir_stack
	global labir_max_count
	try:
		try:
			labir_stack
		except:
			labir_stack=[]
		labir_choose=[]
		labir_chosen=[None,None,None]
		labir_empty=[]
		labir_ways=0
		labir_count1=0
		labir_ways_arr=[[],[],[],[]]
		try:
			global labir_count
			labir_count+=1
		except:
			labir_count=0
		#labir_max_count=80
	#	can.delete("print")
		temp1=[]
		if (labir_count)>(0.75*labir_max_count) or labir_count==0:
			exit_ready=1
		else:
			exit_ready=0
		if(labir_count==0):
			labir_exit=[[]]
	
		elif(exit_ready):
			
			labir_exit+=[[]]
	#		labir_exit.append([])
	
		if(exit_ready):
			print([len(labir_exit)])
			
			
		for g in range(6):
			if g==0: i,j=ii,jj-2	
			if g==1: i,j=ii-1,jj-1
			if g==2: i,j=ii-1,jj+1
			if g==3: i,j=ii,jj+2
			if g==4: i,j=ii+1,jj+1
			if g==5: i,j=ii+1,jj-1
			
			try:	
				if(i<0 or j<0):
					labir_empty.append(0)
					hexes_labir[ii][jj][1+g]=1
					temp1.append(["br2"])
					if(exit_ready):
						labir_exit[len(labir_exit)-1].append([ii,jj,g])
				elif(hexes_labir[i][j][0]==2):
					hexes_labir[ii][jj][1+g]=hexes_labir[i][j][1+(g+3)%6]
					temp1.append(["tile"])
					labir_empty.append(0)
				elif(hexes_labir[i][j][0]==1):
					labir_count1+=1
					labir_empty.append(labir_count1)
					temp1.append(["emptile"])
				else:
					labir_empty.append(0)
					hexes_labir[ii][jj][1+g]=1
					temp1.append(["br1"])
			except:
				
				labir_empty.append(0)
			
				hexes_labir[ii][jj][1+g]=1
					
				temp1.append(["br2"])
				if(exit_ready):
					labir_exit[len(labir_exit)-1].append([ii,jj,g])
			labir_choose.append([i,j])
	
			if(labir_empty[len(labir_empty)-2]>0 and labir_empty[len(labir_empty)-1]==0 ):
				labir_ways+=1
				
			if(labir_empty[len(labir_empty)-1]>0):
				labir_ways_arr[labir_ways].append(g)
			
			#print([labir_ways,labir_empty])	
		if(labir_empty[5]>0 and labir_empty[0]==0):
				labir_ways+=1
				
		else:
				labir_ways_arr[labir_ways]+=labir_ways_arr[0]
				labir_ways_arr.pop(0)
		
		for g in range(len(labir_ways_arr)-1,0-1,-1):
			if(labir_ways_arr[g]==[]):
				labir_ways_arr.pop(g)
		for g in range(len(labir_exit)-1,0-1,-1):
			if(labir_exit[g]==[]):
				labir_exit.pop(g)
		
		
		
		for k in range(labir_ways):
			labir_chosen[k]=random.randint(0,len(labir_ways_arr[k])-1)
			for gg in range(len(labir_ways_arr[k])):
				None
				if(labir_chosen[k]==gg):
					hexes_labir[ii][jj][labir_ways_arr[k][gg]+1]=0
				else:
					hexes_labir[ii][jj][labir_ways_arr[k][gg]+1]=1
			
		hexes_labir[ii][jj][0]=2
		#print([[labir_count,labir_ways],[labir_empty[5],labir_empty[0]]])	
		if(labir_count==0):
			
			labir_rand=random.randint(0,len(labir_exit[0])-1)
			print([labir_exit,len(labir_exit[0]),labir_rand])
			hexes_labir[ii][jj][1+labir_exit[0][labir_rand][2]]=0
		if(labir_count==labir_max_count):
			labir_rand=[0,0]
			labir_rand[0]=random.randint(1,len(labir_exit)-1)
			labir_rand[1]=random.randint(0,len(labir_exit[labir_rand[0]])-1)
			print([labir_exit])
			print ([labir_rand[0],labir_rand[1]])			
			
			hexes_labir[labir_exit [labir_rand[0]][labir_rand[1]][0]][labir_exit [labir_rand[0]][labir_rand[1]][1]][labir_exit [labir_rand[0]][labir_rand[1]][2]+1]=0
			print(hexes_labir[labir_exit [labir_rand[0]][labir_rand[1]][0]][labir_exit [labir_rand[0]][labir_rand[1]][1]][labir_exit [labir_rand[0]][labir_rand[1]][2]+1])
		if(labir_count<labir_max_count):
		#	print([random.randint(0,0),labir_exit[random.randint(0,len(labir_exit))]])
		#	if(labir_count==0):
	#			hexes_labir[ii][jj][1+labir_exit[0][random.randint(0,len(labir_exit[0])-1)][2]]=0
			
			for g in range(labir_ways): 
				labir_stack.append([labir_choose[labir_ways_arr[g][labir_chosen[g]]][0],labir_choose[labir_ways_arr[g][labir_chosen[g]]][1]])
				
			
	#		print([labir_stack,labir_ways])
			try:
				labir_next=labir_stack.pop(0)
				return labir_walls(labir_next[0],labir_next[1])
			except:
				None
		
	except:
				print([ii," error ",jj])
def draw(hex,mode):

	from objects import x_field,y_field
	global hex_w
	global hex_h
	global draw_hexes
	global particles
	if(mode=="flat"):
		global hexes_flat
		hexes_draw=hexes_flat
	if(mode=="labir"):
		global hexes_labir
		hexes_draw=hexes_labir
	if hexes_draw!=0:
		draw_hexes=[]
		if(hex==0):
			for i in range(x_field):
				for j in range(y_field):
					if((i+j)%2==0):
				#		if(hex==2):
						hex_color=int(hexes_draw[i][j]/36*255)
						
						jj=j/2
						ii=i/4*3
						draw_hexes.append(pygame.draw.polygon(screen, (hex_color,hex_color,hex_color),[(border+hex_w*ii,border+hex_h/y_field*(jj+0.5)),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj)),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj)),(border+hex_w*(ii+1),border+hex_h/y_field*(jj+0.5)),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj+1)),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj+1))]))
		else:
			for i in range(len(hexes_draw)):
				for j in range(len(hexes_draw[0])):
					if((i+j)%2==0):
						hex_color=int(hexes_draw[i][j][0]/3*255)
						
						jj=(j+round(hex*y_field,0))/2
						ii=(i+round(hex*x_field,0))/4*3
						
						draw_hexes.append(pygame.draw.polygon(screen, (hex_color,hex_color,hex_color),[(border+hex_w*ii,border+hex_h/y_field*(jj+0.5)),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj)),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj)),(border+hex_w*(ii+1),border+hex_h/y_field*(jj+0.5)),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj+1)),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj+1))]))
			for i in range(len(hexes_draw)):
				for j in range(len(hexes_draw[0])):
					if((i+j)%2==0):
						hex_color=int(hexes_draw[i][j][0]/3*255)
						
						jj=(j+round(hex*y_field,0))/2
						ii=(i+round(hex*x_field,0))/4*3
						if(hexes_draw[i][j][0]==0):
							screen.blit((my_font.render((str(i)+" "+str(j)), False, (100, 100, 0))), (border+hex_w*ii,border+hex_h/y_field*(jj+0.5)))
						if(hexes_draw[i][j][0]==2):
							
							if(hexes_draw[i][j][2]):
								pygame.draw.line(screen, (200,0,0),(border+hex_w*ii,border+hex_h/y_field*(jj+0.5)),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj)))
							if(hexes_draw[i][j][1]):
								pygame.draw.line(screen, (200,0,0),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj)),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj)))
							if(hexes_draw[i][j][6]):
								pygame.draw.line(screen, (200,0,0),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj)),(border+hex_w*(ii+1),border+hex_h/y_field*(jj+0.5)))
							if(hexes_draw[i][j][5]):
								pygame.draw.line(screen, (200,0,0),(border+hex_w*(ii+1),border+hex_h/y_field*(jj+0.5)),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj+1)))
							if(hexes_draw[i][j][4]):
								pygame.draw.line(screen, (200,0,0),(border+hex_w*(ii+0.75),border+hex_h/y_field*(jj+1)),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj+1)))
							if(hexes_draw[i][j][3]):
								pygame.draw.line(screen, (200,0,0),(border+hex_w*(ii+0.25),border+hex_h/y_field*(jj+1)),(border+hex_w*ii,border+hex_h/y_field*(jj+0.5)))
		for i in range(w):
			for j in range(h):
				if(particles[i][j]==1):
					pygame.draw.circle(screen, (0,0,0),(i,j),1)
	#			