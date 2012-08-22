#written by Jacob Mason
#Mental Math Companion version 1.0.0
#7/4/2011

import pygame
import random
import sys
import time

class Program():
	'''application framework'''
	def __init__(self):
		'''predifined variables'''
		self.size = (300,500)
		self.screen = pygame.display.set_mode(self.size)
		self.pi = 3.14159265358979323846264 #from memory :)
		self.digit = 0
		self.right = 0
		self.wrong = 0
		self.digit_a = 1
		self.digit_b = 2
		self.digit_c = 1
		self.digit_d = 2
		self.answer = ""
		self.done = False
		self.operation = "*"
		self.move_on = True
		self.objects = []
		#colors
		self.black = (0,0,0)
		self.white = (255,255,255)
		self.blue = (0,0,255)
		self.green = (0,255,0)
		self.red = (255,0,0)
		#configuration
		self.clock = pygame.time.Clock()
		self.background_image = pygame.image.load("background.jpg").convert()
		pygame.font.init()
		self.font1 = pygame.font.Font (None,70) #first font
		self.font2 = pygame.font.Font(None,40) #second font
		self.font3 = pygame.font.Font(None,30) #third font
		self.operand = self.font1.render("*",True,self.red)
	
	def end_option(self): #yea yea.. i know =\ but hey it saves a little typing
		self.operand = py.font1.render(self.operation,True,py.red)
		self.move_on = False
		self.done = True

	def multi1(self):
		'''executes if the related option is chosen'''
		self.digit_a = 1
		self.digit_b = 100
		self.digit_c = 2
		self.digit_d = 10
		self.operation = "*" 
		self.end_option()
	
	def multi2(self):
		self.digit_a = 10
		self.digit_b = 100
		self.digit_c = 10
		self.digit_d = 100
		self.operation = "*"
		self.end_option()
	
	def multi3(self):
		self.digit_a = 100
		self.digit_b = 1000
		self.digit_c = 10
		self.digit_d = 100
		self.operation = "*"
		self.end_option()
	
	def addi(self):
		self.digit_a = 100
		self.digit_b = 1000
		self.digit_c = 100
		self.digit_d = 1000
		self.operation = "+"
		self.end_option()

	def subt(self):
		self.digit_a = 100
		self.digit_b = 1000
		self.digit_c = 10
		self.digit_d = 100
		self.operation = "-"
		self.end_option()
	
	def divid(self):
		self.digit_a = 100
		self.digit_b = 1000
		self.digit_c = 2
		self.digit_d = 10
		self.operation = "/"
		self.end_option()

	def draw(self,h):
		for i in xrange(len(self.objects[h])):
			self.screen.blit(self.objects[h][i].format,self.objects[h][i].xy)


py = Program()

class Link():
	'''framework for the links'''
	def __init__(self,x,y,text,font,color_choice):
		self.x_limit = x
		self.y_limit = y 
		self.xy = (self.x_limit[0],self.y_limit[0])
		self.x_range = self.range_find(x)
		self.y_range = self.range_find(y)
		self.color = color_choice
		self.font = font
		self.text = text
		self.format = eval('py.%s.render("%s",True,py.%s)' % (self.font,self.text,self.color))

	def range_find(self,n):
		res = []
		for i in xrange(n[0],(n[1]+1)):
			res.append(i)
		return res
	
	def c_swap(self,color):
		'''changes a links color in the "format" attribute'''
		self.color = color
		self.format = eval('py.%s.render("%s",True,py.%s)' % (self.font,self.text,self.color))

class Banner():
	def __init__(self,x,y,font,text,color,max = 150, min = 0):
		self.max = max
		self.min = min
		self.xy = (x,y)
		self.font = font
		self.text = text
		self.color = color
		self.i = 0
		self.reverse = False
		self.format = eval('py.%s.render("%s",True,%s)' % (self.font,self.text,self.color))

	def i_swap(self):
		self.color[0] = self.i
		self.format = eval('py.%s.render("%s",True,%s)' % (self.font,self.text,self.color))

class Numbers():
	def __init__(self,x,y,a,b,font = 'font1',color = 'black'):
		self.rand = random.randrange(a,b)
		self.format = eval('py.%s.render("%s",True,py.%s)' % (font,self.rand,color))
		self.xy = x,y

pygame.display.set_caption("Mental Math Companion")

#define banner instance
banner = Banner(2,50,'font1','Mental Math',[0,0,150],170)

#define option instances 
option_1 = Link((35,261),(150,175),'1 by 2 digit multi','font2','black')
option_2 = Link((35,261),(200,225),'2 by 2 digit multi','font2','black')
option_3 = Link((35,261),(250,275),'2 by 3 digit multi','font2','black')
option_4 = Link((35,261),(150,175),'3 by 3 digit addi','font2','black')
option_5 = Link((35,261),(200,225),'3 by 2 digit subt','font2','black')
option_6 = Link((35,261),(250,275),'3 by 1 digit divid','font2','black')
next = Link((115,174),(300,325),'Next','font2','black')
back_to_menu = Link((64,245),(10,30),'back to menu','font2','black')
next.page = 0
#first page objects
py.objects.append([option_1,option_2,option_3,next,banner])
#second page objects
py.objects.append([option_4,option_5,option_6,next,banner])

while True:
	while py.move_on:
		py.screen.blit(py.background_image,[0,0])
		pos = pygame.mouse.get_pos()
		x,y = (pos[0],pos[1])
	
		#hilight when mouse hovers over the links
		for i in xrange(len(py.objects[next.page])-1):
			if x in py.objects[next.page][i].x_range and y in py.objects[next.page][i].y_range:
				py.objects[next.page][i].c_swap('red')
			else:
				py.objects[next.page][i].c_swap('black')

		#produce a glowing effect for the banner
		if banner.reverse:
			if banner.i < banner.max:
				banner.i += 1
				banner.i_swap()
			else:
				banner.reverse = False
		else:
			if banner.i > banner.min:
				banner.i -= 1
				banner.i_swap()
			else:
				banner.reverse = True
				
	
		#catch pygame events 
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				#i still gotta clean up the following quite a bit =\
				#but it works for now..
				print 'mouse coords => %sx,%sy' % (x,y)
				if x in option_1.x_range and y in option_1.y_range and next.page == 0:
					#first option has been selected on first page
					py.multi1()
					break
				elif x in option_2.x_range and y in option_2.y_range and next.page == 0:
					#second option has been selected on first page
					py.multi2()
					break
				elif x in option_3.x_range and y in option_3.y_range and next.page == 0:
					#third option has been selected on first page
					py.multi3()
					break
				elif x in option_4.x_range and y in option_4.y_range and next.page == 1:
					#fourth option has been selected on second page
					py.addi()
					break
				if x in option_5.x_range and y in option_5.y_range and next.page == 1:
					py.subt()
					break
				if x in option_6.x_range and y in option_6.y_range and next.page == 1:
					py.divid()
				if x in next.x_range and y in next.y_range:
					#next was selected on either page
					if next.page == len(py.objects) -1:
						next.page = 0
					else:
						next.page += 1

		#draw objects to the screen	
		time.sleep(.005)
		py.draw(next.page)
		pygame.display.flip()
		
		while py.done:
			py.clock.tick(10)
			once = 0
			
			#create number instances that have their own random values 
			first_number = Numbers(130,125,py.digit_a,py.digit_b)
			second_number = Numbers(130,175,py.digit_c,py.digit_d)
			py.answered = True
			while py.answered:
				pos = pygame.mouse.get_pos()
				x,y = (pos[0],pos[1])
				py.screen.blit(py.background_image,[0,0])

				#storing correct answer 
				if py.operation == "*":
					correct = str(first_number.rand * second_number.rand)
				elif py.operation == "/":
					correct = str(first_number.rand / second_number.rand)
				elif py.operation == "+":
					correct = str(first_number.rand + second_number.rand)
				elif py.operation == "-":
					correct = str(first_number.rand - second_number.rand)
				#check to see if the users value in answer is the correct answer
				if py.answer == correct:
					if not once:
						py.right += 1
					py.answer = ""
					break
				#what to do if the value in answer is not the correct one
				elif py.answer != correct:
					if len(str(correct)) <= len(py.answer):
						if not once:
							''' It's a tad dirty but it's the most
							straight foward way to make sure
							wrong is only increased once every
							time a wrong value is in answer '''
							py.wrong += 1
							once = 1
						
						correct_out = py.font1.render(correct,True,py.black)
						py.screen.blit(correct_out,[125,260])
				
				#hilight back to menu on mouseover
				if x in back_to_menu.x_range and y in back_to_menu.y_range:
					back_to_menu.c_swap('red')
				else:
					back_to_menu.c_swap('black')
				#catch pygame events
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					if event.type == pygame.MOUSEBUTTONDOWN:
						print 'mouse coords => %sx,%sy' % (x,y)
						if x in back_to_menu.x_range and y in back_to_menu.y_range:
							py.done = False
							py.move_on = True
							py.answered = False
							break 

					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_1:
							py.answer += "1"
						elif event.key == pygame.K_2:
							py.answer += "2"
						elif event.key == pygame.K_3:
							py.answer += "3"
						elif event.key == pygame.K_4:
							py.answer += "4"
						elif event.key == pygame.K_5:
							py.answer += "5"
						elif event.key == pygame.K_6:
							py.answer += "6"
						elif event.key == pygame.K_7:
							py.answer += "7"
						elif event.key == pygame.K_8:
							py.answer += "8"
						elif event.key == pygame.K_9:
							py.answer += "9"
						elif event.key == pygame.K_0:
							py.answer += "0"
						elif event.key == pygame.K_BACKSPACE:
							py.answer = py.answer[0:-1]
							py.screen.blit(py.background_image,[0,0])
							
					
					#draw main items
					py.screen.blit(first_number.format,first_number.xy)
					py.screen.blit(second_number.format,second_number.xy)
					py.screen.blit(py.operand,[80,180])
					pygame.draw.line(py.screen,py.red,[105,220],[210,220],5)

					#draw check mark
					pygame.draw.arc(py.screen,py.green,[35,359,250,375],py.pi/1.6,2.5,4)
					pygame.draw.arc(py.screen,py.green,[6,413,62.5,50],.4,py.pi/2,4)

					#draw "X"
					pygame.draw.line(py.screen,py.red,[200,385],[240,431],4)
					pygame.draw.line(py.screen,py.red,[240,385],[200,431],4)

					#display amount of incorrectly answered problems
					wrong_out = py.font1.render(str(py.wrong),True,py.black)
					py.screen.blit(wrong_out,[180,440])

					#display amount of correctly answered problems
					right_out = py.font1.render(str(py.right),True,py.black)
					py.screen.blit(right_out,[30,440])

					#blit current value in the answer variable
					answer_out = py.font1.render(py.answer,True,py.black)
					py.screen.blit(answer_out,[125,220])

					#back to main menu option
					py.screen.blit(back_to_menu.format,back_to_menu.xy)
					pygame.display.flip()



