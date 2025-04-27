#importing all standard libraries which can be used
import pygame
import numpy as np
import random
import math
import sys
import os
import time

#importing my modules
from starting_game import *
from input_player1 import *
from input_player2 import *
from p1_vs_p2 import *

######## main file ###########
start_game() #used to start game and ask player details and take you into game
player1_name = player1() #function to take player1 name  
print("Player 1 name:", player1_name) #print player1 name
player2_name = player2() #function to take player2 name
print("Player 2 name:", player2_name) #print player2 name
player1_vs_player2(player1_name, player2_name) #function to show player1 vs player2 screen
pygame.quit()