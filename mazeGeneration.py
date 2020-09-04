import pygame
import math
import time
import random
#from utilities import *
from maze_utilities import *
from gButton_utilities import *
from maze import dfsBacktrackingMaze

pygame.init()
color  = {"blue":(0,0,255),"light_blue":(173,216,230), "steel_blue":(70,130,180), "yelllow":(255,249,10),
          "dark_brown":(77,38,2), "brown":(247,125,10),  "orange":(247,46,10),"dark_orange":(255,140,0),
          "yellow":(247,239,10), "bright_blue":(10,247,208), "lilac":(247,10,232),
          "pink":(247,10,10), "gray":(150,150,150), "light_gray":(210,210,210), "bright_green":(0,255,0),
          "green":(0,200,0), "bright_red":(255,0,0), "red":(245,45,66)}

white = (255,255,255)
black = (0,0,0)
gray = (200,200,200)

#pygame variables
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
click = pygame.mouse.get_pressed
mouse = pygame.mouse.get_pos
def_font = pygame.font.get_default_font() 


#global variables
default_m, default_n  = 10, 10
m, n  = default_m, default_n
pause = False

#buttons
grun, gquit, gchange_settings, gm, gn = None, None, None, None, None

#messages
title_msg, descr_msg, pick_m_msg, pick_n_msg = None, None, None, None

def set_buttons():
  global grun, gquit, gcontinue, gpause, gchange_settings
  global gm, gn
 
  
  colors = [color["orange"], color["steel_blue"], color["yellow"], color["yellow"]]
  m_rect = (100,120,400,50)
  m_vals = [20,40,60,80, 100]
  m_txt = ["20", "40", "60", "80","100"]
  gm = GroupButton(m_rect, 1,5,5, 2, colors, text = m_txt , values = m_vals)
  gm.set_group()
  n_rect = (100,320, 400, 50)
  
  gn = GroupButton(n_rect, 1,5,5, 2, colors, text = m_txt, values = m_vals)
  gn.set_group()
  runcolors = [color["steel_blue"], color["green"], color["green"]]
  run_rect = (100, 500, 100, 50)
  grun = GButton(run_rect, runcolors, text = "Run",action = run_loop)
  
  change_rect = (screen_width//2 - 80, screen_height-30, 160 ,30)

  gchange_settings = GButton(change_rect,runcolors, text = "Change settings",action = maze_intro)
  quitcolors = [color["dark_orange"], color["red"], color["red"]]
  quit_rect = (400, 500, 100, 50)
  gquit = GButton(quit_rect, quitcolors, text = "Quit", action = quit_game)


def set_messages():
  global title_msg, pick_m_msg, pick_n_msg
  title_msg = Message(screen, "Maze generation", 'freesansbold.ttf', 30,
                          (screen_width/2, 15), color['dark_brown'])
  
  pick_m_msg = Message(screen, "Pick the number of rows", 'freesansbold.ttf', 20,
                                      (screen_width/2, gm.group_rect[1] - 20), color['dark_brown'])
  pick_n_msg = Message(screen, "Pick the number of columns", 'freesansbold.ttf', 20,
                                  (screen_width/2, gn.group_rect[1] - 20 ), color['dark_brown'])




def maze_intro():
  global m, n
  set_buttons()
  set_messages()

  screen.fill(white)  
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
          gm.check_group(event)
          gn.check_group(event)
          grun.button_check(event)
          gquit.button_check(event)
      gm.display_group(screen)
      gn.display_group(screen)
      grun.button_draw(screen)
      gquit.button_draw(screen)  
      title_msg.display_msg()
      pick_m_msg.display_msg()
      pick_n_msg.display_msg()
      m = gm.get_choice(default_m)
      n = gn.get_choice(default_n)
      pygame.display.update()
      clock.tick(10)



def run_loop():
  global m, n,gchange_settings
  path = dfsBacktrackingMaze(m, n)
  
  
  screen = pygame.display.set_mode((screen_width, screen_height))
  

  colors = [color['red'],color['yellow']]
  #Grid:(surface, rows,cols, start_point, colors, values = None)
  #Passage: (grid, path, width, color)
  gr = Grid( screen, m, n,(20,20),colors)
  gr.set_grid()

  psg = Passage(gr,path, 1, white)
  gr.display_grid()
  psg.display_passage(screen)

     


  while True:

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          gchange_settings.button_check(event)
      gchange_settings.button_draw(screen)




  
      pygame.display.flip()

      clock.tick(60)
 

def quit_game():
  pygame.quit()
  quit()
    

maze_intro()

      

    

    
    



    
