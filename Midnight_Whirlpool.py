import os
import pygame, sys
import random
from pygame import Rect
from pygame.math import Vector2

# Make the window centered
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Store the data about the game
class GameState():
    
    def __init__(self):
        
        # Define the basic attributes of the world
        self.state = 'title_screen'
        self.worldSize = Vector2(14,12)
        self.beenToRoom0 = False
        self.beenToRoom1 = False
        self.beenToRoom2 = False
        self.beenToRoom3 = False
        self.beenToRoom4 = False
        self.beenToRoom5 = False
        self.beenToRoom6 = False
        self.beenToRoom7 = False
        
        self.room0()
        
        self.room1_chest_items = [RedPotion(self), BluePotion(self)]
        self.room5_chest_items = [RedPotion(self), BluePotion(self), RedPotion(self), BluePotion(self), BluePotion(self)]
        
        self.backgroundAngle = 0
        self.fight_background = Vector2(0,11)
        
        # Make an inventory and chests that can add things to them
        self.inventory = []
    
    @property
    def worldWidth(self):
        return int(self.worldSize.x)
    
    @property
    def worldHeight(self):
        return int(self.worldSize.y)
    
    def room0(self):
        if self.beenToRoom0 == False:
            self.units = [
                Wizard(self, Vector2(6,6), Vector2(0,0))
                ]
        else:
            del self.units[1:]
                
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(9,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(7,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(8,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(5,5), Vector2(4,5), Vector2(13,5), None, Vector2(14,5), Vector2(1,5), Vector2(0,5), Vector2(9,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(8,5), None, None, None, None, None, None, Vector2(12,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(0,6), Vector2(2,6), Vector2(1,6), Vector2(1,6), Vector2(1,6), Vector2(3,6), Vector2(1,6), Vector2(4,6), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(6,2), Vector2(2,4), "room1")
            ]
        
        self.torches = [
            Torch(Vector2(4,2), Vector2(0,7), False),
            Torch(Vector2(7,2), Vector2(0,7), True),
            Torch(Vector2(3,6), Vector2(4,7), False),
            Torch(Vector2(9,5), Vector2(4,7), True)
            ]
        
        self.chests = []
        
        self.keys = []
        
        self.clocks = []
        
        self.background = Vector2(4,9)
        
        self.beenToRoom0 = True
    
    def room1(self):
        if self.beenToRoom1 == False:
            self.units.append(Slime(self, Vector2(8,6), Vector2(0,1), "Earth Slime"))    # Green Slime
            self.units.append(Slime(self, Vector2(5,6), Vector2(4,1), "Ice Slime"))      # Blue Slime
            self.units.append(Guard(self, Vector2(10,4), Vector2(4,2), "Warden of Ice"))  # Blue Guard
            self.units.append(Guard(self, Vector2(9,3), Vector2(0,2), "Warden of Earth"))# Green Guard
            
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(7,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(8,6), Vector2(5,6),Vector2(5,6), None, None, None,],
            [None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),Vector2(5,6), None, None, None,],
            [None, None, None, Vector2(7,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(6,6),Vector2(5,6), None, None, None,],
            [None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(7,6), Vector2(5,6), Vector2(5,6),Vector2(5,6), None, None, None,],
            [None, None, None, Vector2(5,6), Vector2(5,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),Vector2(5,6), None, None, None,],
            [None, None, None, Vector2(8,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(7,6),Vector2(5,6), None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, Vector2(5,5), Vector2(0,5), Vector2(3,5), Vector2(13,5), None, Vector2(14,5), Vector2(1,5), Vector2(4,5), Vector2(3,5), Vector2(9,5), None, None],
            [None, None, Vector2(7,5), None, None, None, None, None, None, None, None, Vector2(10,5), None, None],
            [None, None, Vector2(15,5), None, None, None, None, None, None, None, None, Vector2(17,5), None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, Vector2(16,5), None, None, None, None, None, None, None, None, Vector2(18,5), None, None],
            [None, None, Vector2(7,5), None, None, None, None, None, None, None, None, Vector2(10,5), None, None],
            [None, None, Vector2(6,5), None, None, None, None, None, None, None, None, Vector2(11,5), None, None],
            [None, None, Vector2(0,6), Vector2(1,6), Vector2(2,6), Vector2(19,5), None, Vector2(20,5), Vector2(3,6), Vector2(1,6), Vector2(1,6), Vector2(4,6), None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(6,9), Vector2(8,4), "room0"),
            Door(Vector2(6,2), Vector2(2,4), "room2"),
            Door(Vector2(11,5), Vector2(6,4), "room3"),
            Door(Vector2(2,5), Vector2(4,4), "room5")
            ]
        
        self.torches = [
            Torch(Vector2(4,2), Vector2(0,7), False),
            Torch(Vector2(8,2), Vector2(0,7), True),
            Torch(Vector2(2,6), Vector2(4,7), False),
            Torch(Vector2(10,7), Vector2(4,7), True)
            ]
        
        self.chests = [
            Chest(Vector2(10,3), Vector2(0,4), self.room1_chest_items, "room1", False)
            ]
        
        self.keys = []
        
        self.clocks = []
        
        self.background = Vector2(6,9)
        
        self.beenToRoom1 = True
        
    def room2(self):
        if self.beenToRoom2 == False:
            self.units.append(Cyclops(self, Vector2(5,5), Vector2(8,2), "Earth Cyclops"))
            self.units.append(Cyclops(self, Vector2(8,5), Vector2(8,1), "Ice Cyclops"))
            
            
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, Vector2(9,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(11,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(11,6), Vector2(6,6), Vector2(5,6), Vector2(10,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(6,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(11,6), Vector2(5,6), Vector2(5,6), Vector2(7,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(10,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6),None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(5,5), Vector2(3,5), Vector2(13,5), None, Vector2(14,5), Vector2(1,5), Vector2(4,5), Vector2(9,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(8,5), None, None, None, None, None, None, Vector2(12,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(0,6), Vector2(2,6), Vector2(19,5), None, Vector2(20,5), Vector2(3,6), Vector2(1,6), Vector2(4,6), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(6,9), Vector2(8,4), "room1"),
            Door(Vector2(6,2), Vector2(2,4), "room4")
            ]
        
        self.torches = [
            Torch(Vector2(5,2), Vector2(0,7), False),
            Torch(Vector2(7,2), Vector2(0,7), True),
            Torch(Vector2(3,6), Vector2(4,7), False),
            Torch(Vector2(9,5), Vector2(4,7), True)
            ]
        
        self.chests = []
        
        self.keys = []
        
        self.clocks = []
        
        self.background = Vector2(8,9)
        
        self.beenToRoom2 = True
        
    def room3(self):
        if self.beenToRoom3 == False:
            self.units.append(Mask(self, Vector2(3,5), Vector2(4,3), "Haunted Mask"))
            self.units.append(Mask(self, Vector2(7,5), Vector2(4,3), "Haunted Mask"))
            self.units.append(Mask(self, Vector2(11,5), Vector2(4,3), "Haunted Mask"))
        
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, Vector2(5,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), Vector2(5,6), Vector2(9,6), None,],
            [None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), None,],
            [None, Vector2(10,6), Vector2(5,6), Vector2(5,6), Vector2(12,6), Vector2(5,6), Vector2(7,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [Vector2(5,5), Vector2(0,5), Vector2(3,5), Vector2(0,5), Vector2(0,5), Vector2(0,5), Vector2(2,5), Vector2(0,5), Vector2(1,5), Vector2(4,5), Vector2(0,5), Vector2(2,5), Vector2(0,5), Vector2(9,5)],
            [Vector2(15,5), None, None, None, None, None, None, None, None, None, None, None, None, Vector2(17,5)],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [Vector2(16,5), None, None, None, None, None, None, None, None, None, None, None, None, Vector2(18,5)],
            [Vector2(0,6), Vector2(2,6), Vector2(1,6), Vector2(1,6), Vector2(2,6), Vector2(1,6), Vector2(1,6), Vector2(1,6), Vector2(3,6), Vector2(1,6), Vector2(2,6), Vector2(1,6), Vector2(1,6), Vector2(4,6)],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(0,5), Vector2(4,4), "room1"),
            Door(Vector2(13,5), Vector2(6,4), "room6")
            ]
        
        self.torches = [
            Torch(Vector2(4,3), Vector2(0,7), False),
            Torch(Vector2(8,3), Vector2(0,7), True),
            Torch(Vector2(0,4), Vector2(4,7), False),
            Torch(Vector2(12,6), Vector2(4,7), True)
            ]
        
        self.chests = []
        
        self.keys = []
        
        self.clocks = []
        
        self.background = Vector2(0,9)
        
        self.beenToRoom3 = True
        
    def room4(self):
        if self.beenToRoom4 == False:
            self.units.append(Knight(self, Vector2(6,4), Vector2(0,3), "Dazed Knight"))
            self.units.append(Spider(self, Vector2(5,6), Vector2(12,2), "Spectral Spider"))
            self.units.append(Spider(self, Vector2(8,6), Vector2(12,2), "Spectral Spider"))
            
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, Vector2(5,6), Vector2(8,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(12,6), Vector2(5,6), Vector2(6,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(12,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(10,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(7,6), Vector2(9,6),None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(5,5), Vector2(3,5), Vector2(13,5), None, Vector2(14,5), Vector2(1,5), Vector2(4,5), Vector2(9,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(8,5), None, None, None, None, None, None, Vector2(12,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(0,6), Vector2(2,6), Vector2(19,5), None, Vector2(20,5), Vector2(3,6), Vector2(1,6), Vector2(4,6), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(6,9), Vector2(8,4), "room2"),
            Door(Vector2(6,2), Vector2(10,4), "room7", True)
            ]
        
        self.torches = [
            Torch(Vector2(4,2), Vector2(0,7), False),
            Torch(Vector2(7,2), Vector2(0,7), True),
            Torch(Vector2(3,6), Vector2(4,7), False),
            Torch(Vector2(9,7), Vector2(4,7), True)
            ]
        
        self.chests = []
        
        self.keys = []
        
        self.clocks = []
        
        self.background = Vector2(10,9)
        
        self.beenToRoom4 = True
        
    def room5(self):
        
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, Vector2(11,6), Vector2(5,6), Vector2(5,6), Vector2(6,6), None, None, None, None, None,],
            [None, None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), None, None, None, None, None,],
            [None, None, None, None, None, Vector2(5,6), Vector2(7,6), Vector2(5,6), Vector2(5,6), None, None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [ None, None, None, None,Vector2(5,5), Vector2(0,5), Vector2(2,5), Vector2(0,5), Vector2(1,5), Vector2(9,5), None, None, None, None],
            [None, None, None, None,Vector2(6,5), None, None, None, None, Vector2(17,5), None, None, None, None],
            [None, None, None, None,Vector2(7,5), None, None, None, None, None, None, None, None, None],
            [None, None, None, None,Vector2(6,5), None, None, None, None, Vector2(18,5), None, None, None, None],
            [ None, None, None, None,Vector2(0,6), Vector2(1,6), Vector2(1,6), Vector2(1,6), Vector2(3,6), Vector2(4,6), None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(9,5), Vector2(6,4), "room1")
            ]
        
        self.torches = [
            Torch(Vector2(6,3), Vector2(0,7), False),
            Torch(Vector2(4,5), Vector2(4,7), False),
            Torch(Vector2(8,6), Vector2(4,7), True)
            ]
        
        self.chests = [
            Chest(Vector2(6,5), Vector2(0,4), self.room5_chest_items, "room5", True)
            ]
        
        self.keys = []
        
        self.clocks = []
        
        self.background = Vector2(4,9)
        
        self.beenToRoom5 = True
    
    def room6(self):        
            
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, Vector2(5,6), Vector2(10,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(11,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), Vector2(6,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(11,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(6,6),None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(5,5), Vector2(1,5), Vector2(0,5), Vector2(1,5), Vector2(0,5), Vector2(1,5), Vector2(4,5), Vector2(9,5), None, None, None],
            [None, None, None, Vector2(15,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(16,5), None, None, None, None, None, None, Vector2(12,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(0,6), Vector2(2,6), Vector2(2,6), Vector2(2,6), Vector2(2,6), Vector2(3,6), Vector2(1,6), Vector2(4,6), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(3,5), Vector2(4,4), "room3")
            ]
        
        self.torches = [
            Torch(Vector2(6,3), Vector2(0,7), False),
            Torch(Vector2(3,6), Vector2(4,7), False),
            Torch(Vector2(9,5), Vector2(4,7), True)
            ]
        
        self.chests = []
        
        self.keys = [
            Key(Vector2(7,5), Vector2(12,4))
            ]
        
        self.clocks = []
        
        self.background = Vector2(2,9)
        
        self.beenToRoom6 = True
        
    def room7(self):
        
        if self.beenToRoom7 == False:
            self.units.append(TwoHeadedBoy(self, Vector2(6,5), Vector2(12,1), "Two Headed Boy"))
            
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, Vector2(9,6), Vector2(6,6), Vector2(5,6), Vector2(10,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(8,6), Vector2(6,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(10,6), Vector2(5,6), Vector2(12,6), Vector2(5,6), Vector2(6,6),None, None, None, None,],
            [None, None, None, None, Vector2(5,6), Vector2(12,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(5,6),None, None, None, None,],
            [None, None, None, None, Vector2(10,6), Vector2(5,6), Vector2(5,6), Vector2(5,6), Vector2(10,6), Vector2(11,6),None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(5,5), Vector2(3,5), Vector2(1,5), Vector2(1,5), Vector2(2,5), Vector2(1,5), Vector2(4,5), Vector2(9,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(11,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(6,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(8,5), None, None, None, None, None, None, Vector2(12,5), None, None, None],
            [None, None, None, Vector2(7,5), None, None, None, None, None, None, Vector2(10,5), None, None, None],
            [None, None, None, Vector2(0,6), Vector2(2,6), Vector2(19,5), None, Vector2(20,5), Vector2(3,6), Vector2(1,6), Vector2(4,6), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = [
            Door(Vector2(6,8), Vector2(8,4), "room4")
            ]
        
        self.torches = [
            Torch(Vector2(5,2), Vector2(0,7), False),
            Torch(Vector2(7,2), Vector2(0,7), True),
            Torch(Vector2(3,6), Vector2(4,7), False),
            Torch(Vector2(9,5), Vector2(4,7), True)
            ]
        
        self.chests = []
        
        self.keys = []
        
        if self.beenToRoom7 == False:
            self.clocks = []
        else:
            self.clocks = [
                AlarmClock(Vector2(7,4), Vector2(13,4))
                ]
        
        self.background = Vector2(0,9)
        
        self.beenToRoom7 = True
        
    def home(self):
            
        self.ground = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), None, None, None, None,],
            [None, None, None, None, Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(14,6), Vector2(13,6), Vector2(13,6), None, None, None, None,],
            [None, None, None, None, Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(14,7), Vector2(13,6), Vector2(13,6), None, None, None, None,],
            [None, None, None, None, Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), None, None, None, None,],
            [None, None, None, None, Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), Vector2(13,6), None, None, None, None,],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        self.walls = [
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, Vector2(17,6), Vector2(15,6), Vector2(16,6), Vector2(15,6), Vector2(16,6), Vector2(15,6), Vector2(16,6), Vector2(19,6), None, None, None],
            [None, None, None, Vector2(18,6), None, None, None, None, None, None, Vector2(20,6), None, None, None],
            [None, None, None, Vector2(18,6), None, None, None, None, Vector2(15,7), Vector2(16,7), Vector2(20,6), None, None, None],
            [None, None, None, Vector2(18,6), None, None, None, None, Vector2(15,8), Vector2(16,8), Vector2(20,6), None, None, None],
            [None, None, None, Vector2(18,6), None, None, None, None, None, None, Vector2(20,6), None, None, None],
            [None, None, None, Vector2(18,6), None, None, None, None, None, None, Vector2(20,6), None, None, None],
            [None, None, None, Vector2(21,6), Vector2(22,6), Vector2(22,6), Vector2(22,6), Vector2(22,6), Vector2(22,6), Vector2(22,6), Vector2(23,6), None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, None, None, None, None]
            ]
        # Make collision rectangles for the walls
        self.wall_coll_rects = []
        for y in range(int(self.worldSize.y)):
            for x in range(int(self.worldSize.x)):
                if not self.walls[y][x] is None:
                    self.wall_coll_rects.append(Wall(Vector2(x,y), Vector2(64,64)))
                    
        self.doors = []
        
        self.torches = []
        
        self.chests = []
        
        self.keys = []
        
        self.clocks = [
            AlarmClock(Vector2(7,4), Vector2(13,4))
            ]
        
        self.background = Vector2(12,9)
        
        
    def gameOver(self, ui):
        self.state = 'game_over'
        
        self.beenToRoom1 = False
        self.beenToRoom2 = False
        self.beenToRoom3 = False
        self.beenToRoom4 = False
        self.beenToRoom5 = False
        self.beenToRoom6 = False
        self.beenToRoom7 = False
        
        self.room0()
        ui.new_room_entered = True
        ui.current_room = "room0"
        
        self.room1_chest_items = [RedPotion(self), BluePotion(self)]
        self.room5_chest_items = [RedPotion(self), BluePotion(self), RedPotion(self), BluePotion(self), BluePotion(self)]
        
        ui.attack_tick = -8000
        ui.fight_frameCounter = 0
        
        self.units[0].position = Vector2(6,6)
        self.units[0].coll_rect.update(6 * 64 + 2, 6 * 64 + 2, 60, 60)
        self.units[0].tile = Vector2(0,0)
        self.units[0].health = 100
        self.units[0].mana = 40
        self.inventory = []
        self.played_gameoversound = False
            
class GameItem():
    def __init__(self, position, tile):
        self.position = position
        self.tile = tile
        
class Unit(GameItem):
    
    def __init__(self, state, position, tile):
        self.state = state
        self.alive = True
        super().__init__(position, tile)
        # Make an invisible rectangle around the mobs for collision detection
        self.coll_rect = pygame.Rect(position.x* 64 + 2, position.y * 64 + 2, 60, 60) # Change the 64, 64, if you change the cellwidtth/height!
        
    def isWiz(self):
        raise NotImplementedError()
        
class Wizard(Unit):
   
    def __init__(self, state, position, tile):
        super().__init__(state, position, tile)
        self.health = 100
        self.mana = 40
        self.max_health = 100
        self.max_mana = 40
        self.damage = 5
        self.attacks = {"Bump": 2 * self.damage,
                        "Fireball": 5 * self.damage,
                        "Black Hole": 15 * self.damage
                        }
        self.attacks_manacost = {"Bump": 0,
                        "Fireball": 5,
                        "Black Hole": 15
                        }
        
    def isWiz(self):
        return True

class Mob(Unit):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile)
        self.fight_tile = 2 * tile
        self.name = name
        self.isBoss = False
        
    def isWiz(self):
        return False
    
    def summonClock(self, gameState):
        if self.isBoss == True:
            gameState.clocks.append(AlarmClock(Vector2(7,4), Vector2(13,4)))
    
class Slime(Mob):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile, name)
        self.health = 20
        self.damage = 10
        self.attacks = {"Scratch": self.damage,
                        "Sleep": 0
                        }
        
class Guard(Mob):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile, name)
        self.health = 50
        self.damage = 15
        self.attacks = {"Light": self.damage,
                        "Meditate": 0
                        }
        
class Mask(Mob):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile, name)
        self.health = 40
        self.damage = 10
        self.moveVector = Vector2(0, 0.05)
        self.faces_forward = True
        self.attacks = {"Spook": self.damage,
                        "Creep": 2 * self.damage
                        }
        
class Knight(Mob):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile, name)
        self.health = 100
        self.damage = 30
        self.attacks = {"Slash": self.damage,
                        "Ignite": 2 * self.damage,
                        "Pray": 0
                        }
        
class Cyclops(Mob):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile, name)
        self.health = 70
        self.damage = 25
        self.attacks = {"Wonder": 0,
                        "Smash": self.damage,
                        "Frenzy": 2 * self.damage
                        }
        
class Spider(Mob):
    
    def __init__(self, state, position, tile, name):
        super().__init__(state, position, tile, name)
        self.health = 30
        self.damage = 15
        self.attacks = {"Bite": self.damage,
                        "Poison": 2 * self.damage
                        }
        
class TwoHeadedBoy(Mob):
    
        def __init__(self, state, position, tile, name):
            super().__init__(state, position, tile, name)
            self.health = 100
            self.damage = 5
            self.isBoss = True
            self.attacks = {"Fireball": 5 * self.damage,
                    "Black Hole": 15 * self.damage
                    }
    
class Torch(GameItem):
    
    def __init__(self, position, tile, isFlipped):
        super().__init__(position, tile)
        self.isFlipped = isFlipped
        
class Wall(GameItem):
    
    def __init__(self, position, tile):
        super().__init__(position, tile)
        # Make an invisible rectangle around the mobs for collision detection
        self.coll_rect = pygame.Rect(position.x*64, position.y*64, 64, 64) # Change the 64, 64, if you change the cellwidtth/height!
        
class AlarmClock(GameItem):
    
    def __init__(self, position, tile):
        super().__init__(position, tile)
        # Make an invisible rectangle around the mobs for collision detection
        self.coll_rect = pygame.Rect(position.x*64, position.y*64, 64, 64) # Change the 64, 64, if you change the cellwidtth/height!
        
    def wakeUp(self, gameState):
        if gameState.state != 'awake':
            gameState.state = 'awake'
            gameState.home()
            gameState.units[0].tile.x += 8
            pygame.mixer.music.load("SFX/home_song.mp3")
            pygame.mixer.music.play(loops=-1)
        
        
class Door(GameItem):
    
    # argumentumkent atadni a szintet ?!
    def __init__(self, position, tile, room, needsKey = False):
        super().__init__(position, tile)
        # Make an invisible rectangle around the mobs for collision detection
        self.coll_rect = pygame.Rect(position.x*64 - 6, position.y*64 - 6, 76, 76) # Change the 64, 64, if you change the cellwidtth/height!
        self.room = room
        self.isOpen = False
        self.isUsed = False
        self.needsKey = needsKey
        
    def openDoor(self, gameState):
        if self.isOpen == False and len(gameState.units) == 1:
            if self.needsKey == False:
                self.tile.x += 1
                self.isOpen = True
        
    def useDoor(self, ui, gameState, unit):
        if self.isUsed == False and len(gameState.units) == 1 and self.needsKey == False:
        
            if self.room == "room0":
                gameState.room0()
                unit.coll_rect.move_ip(0, -5 * 64 + 12)
                unit.position = Vector2(6,3)
                
            elif self.room == "room1":
                gameState.room1()
                if ui.current_room == "room0":
                    unit.coll_rect.move_ip(0, 5 * 64 - 12)
                    unit.position = Vector2(6,8)
                elif ui.current_room == "room2":
                    unit.coll_rect.move_ip(0, -5 * 64 + 12)
                    unit.position = Vector2(6,3)
                elif ui.current_room == "room3":
                    unit.coll_rect.move_ip(9 * 64 - 12, 0)
                    unit.position = Vector2(10,5)
                elif ui.current_room == "room5":
                    unit.coll_rect.move_ip(-5 * 64 + 12, 0)
                    unit.position = Vector2(3,5)
                    
            elif self.room == "room2":
                gameState.room2()
                if ui.current_room == "room1":
                    unit.coll_rect.move_ip(0, 5 * 64 - 12)
                    unit.position = Vector2(6,8)
                elif ui.current_room == "room4":
                    unit.coll_rect.move_ip(0, -5 * 64 + 12)
                    unit.position = Vector2(6,3)
                    
            elif self.room == "room3":
                gameState.room3()
                if ui.current_room == "room1":
                    unit.coll_rect.move_ip(-9 * 64 + 12, 0)
                    unit.position = Vector2(1,3)
                if ui.current_room == "room6":
                    unit.coll_rect.move_ip(8 * 64 - 12, 0)
                    unit.position = Vector2(12,5)
                    
            elif self.room == "room4":
                gameState.room4()
                if ui.current_room == "room2":
                    unit.coll_rect.move_ip(0, 5 * 64 - 12)
                    unit.position = Vector2(6,8)
                elif ui.current_room == "room7":
                    unit.coll_rect.move_ip(0, -4 * 64 + 12)
                    unit.position = Vector2(6,3)
                    
            elif self.room == "room5":
                gameState.room5()
                if ui.current_room == "room1":
                    unit.coll_rect.move_ip(5 * 64 - 12, 0)
                    unit.position = Vector2(8,5)
            
            elif self.room == "room6":
                gameState.room6()
                if ui.current_room == "room3":
                    unit.coll_rect.move_ip(-8 * 64 + 12, 0)
                    unit.position = Vector2(4,5)
                    
            elif self.room == "room7":
                gameState.room7()
                if ui.current_room == "room4":
                    unit.coll_rect.move_ip(0, 4 * 64 - 12)
                    unit.position = Vector2(6,7)
                
            self.isUsed = True
            ui.current_room = self.room
            ui.new_room_entered = True
            
        else:
            pass
        
class Chest(GameItem):
    
    def __init__(self, position, tile, chest_items, room, isFlipped):
        super().__init__(position, tile)
        # Have collision detection for the chests too!
        self.coll_rect = pygame.Rect(position.x* 64 + 2, position.y * 64 + 2, 60, 60) # Change the 64, 64, if you change the cellwidtth/height!
        self.chest_items = chest_items
        self.isOpen = False
        self.isColliding = False
        self.room = room
        self.isFlipped = isFlipped
        
    def openChest(self, ui):
        if len(self.chest_items) != 0:
            ui.selected_chest_item = self.chest_items[0]
        else:
            ui.selected_chest_item = None
        self.tile = Vector2(1,4)
        self.isOpen = True
        
    def closeChest(self, ui):
        ui.selected_chest_item = None
        self.tile = Vector2(0,4)
        self.isOpen = False
        
    def getChestItem(self, ui, gameState, item):
        if len(gameState.inventory) < 8:
            gameState.inventory.append(item)
            self.chest_items.remove(item)
                
            if len(gameState.inventory) != 0:
                ui.selected_item = gameState.inventory[gameState.inventory.index(item)]
            else:
                ui.selected_item = None
                
class Key(GameItem):
    
    def __init__(self, position, tile):
        super().__init__(position, tile)
        # Make an invisible rectangle around the mobs for collision detection
        self.coll_rect = pygame.Rect(position.x*64, position.y*64, 64, 64) # Change the 64, 64, if you change the cellwidtth/height!
        
    def PickUpKey(self, ui, gameState, inventory):
        if len(gameState.inventory) < 8:
            gameState.inventory.append(DungeonKey(gameState))
            gameState.keys.remove(self)
            if len(gameState.inventory) != 0:
                ui.selected_item = gameState.inventory[0]
            else:
                ui.selected_item = None
        
class InventoryItem():
    
    def __init__(self, gameState):
        self.gameState = gameState
        self.player = self.gameState.units[0]    # player_unit
        
    def use(self):
        raise NotImplementedError()
        
class RedPotion(InventoryItem):
    
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = "Red Potion"
        self.description = "Restores 50 Health Points"
        self.heal = 50
        
    def use(self):
        if self.player.health + self.heal <= self.player.max_health:
            self.player.health += self.heal
        else:
            self.player.health = self.player.max_health
        self.gameState.inventory.remove(self)
        
class BluePotion(InventoryItem):
    
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = "Blue Potion"
        self.description = "Restores 30 Mana Points"
        self.restore = 30
        
    def use(self):
        if self.player.mana + self.restore <= self.player.max_mana:
            self.player.mana += self.restore
        else:
            self.player.mana = self.player.max_mana
        self.gameState.inventory.remove(self)
        
class DungeonKey(InventoryItem):
    
    def __init__(self, gameState):
        super().__init__(gameState)
        self.name = "Dungeon Key"
        self.description = "Opens any door, that you can't go through"
        
    def use(self):
        for door in self.gameState.doors:
            if door.needsKey == True:
                door.needsKey = False
        self.gameState.inventory.remove(self)

# Update the data about the game
class Command():
    
    def run(self):
        raise NotImplementedError()    # So that I don't forget to implement this method in every child class
        
class MoveCommand(Command):
    
    def __init__(self, ui, gameState, unit, moveVector):
        self.ui = ui
        self.gameState = gameState
        self.unit = unit
        self.moveVector = moveVector
        
    def run(self):
        # Update the sprite of the wizard to face in the direction he's moving
        if self.unit.isWiz() == True:
            if self.moveVector.x < 0 and self.moveVector.y == 0:
                self.unit.tile.x = 2
            elif self.moveVector.x > 0 and self.moveVector.y == 0:
                self.unit.tile.x = 1
            elif self.moveVector.x == 0 and self.moveVector.y < 0:
                self.unit.tile.x = 3
            elif self.moveVector.x == 0 and self.moveVector.y > 0:
                self.unit.tile.x = 0
            elif self.moveVector.x > 0 and self.moveVector.y > 0:
                self.unit.tile.x = 4
            elif self.moveVector.x > 0 and self.moveVector.y < 0:
                self.unit.tile.x = 6
            elif self.moveVector.x < 0 and self.moveVector.y > 0:
                self.unit.tile.x = 5
            elif self.moveVector.x < 0 and self.moveVector.y < 0:
                self.unit.tile.x = 7
                
            if self.gameState.state == 'awake':
                self.unit.tile.x += 8
        elif self.unit.name == "Haunted Mask":
            if self.moveVector.y < 0:
                self.unit.faces_forward = False
                self.unit.tile.x = 8
            elif self.moveVector.y > 0 and self.unit.faces_forward == False:
                self.unit.faces_forward = True
                self.unit.tile.x = 4
            
        # Compute the new position of the wizard and move its collision rectangle
        newPos = self.unit.position + self.moveVector
        self.unit.coll_rect.move_ip(int(self.moveVector.x * 64), int(self.moveVector.y * 64))
        
        # Collision detection for outside of the world
        if self.unit.coll_rect.left <= 0 or self.unit.coll_rect.right >= self.gameState.worldWidth * 64:
            self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
            return
        elif self.unit.coll_rect.top <= 0 or self.unit.coll_rect.bottom >= self.gameState.worldHeight * 64:
            self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
            return
        
        #Collision detection for walls:
        collision_tolerance = 20
        for wall in self.gameState.wall_coll_rects:
            if self.unit.coll_rect.colliderect(wall.coll_rect):
                if abs(wall.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(wall.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(wall.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(wall.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    # Collision detection for masks and walls
                    if self.unit.isWiz() == False:
                        newPos = self.unit.position - self.moveVector
                        self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                        self.unit.moveVector *= -1
                    return
                
        # Collision detection for doors
        for door in self.gameState.doors:
            if self.unit.coll_rect.colliderect(door.coll_rect):
                if abs(door.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(door.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(door.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(door.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    door.useDoor(self.ui, self.gameState, self.unit)
                    return
            else:
                self.ui.new_room_entered = False
                
        # Collision detection for the chests
        for chest in self.gameState.chests:
            if self.unit.coll_rect.colliderect(chest.coll_rect):
                if abs(chest.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(chest.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(chest.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(chest.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    chest.isColliding = True
                    return
            else:
                chest.isColliding = False
                
        # Collision detection for the keys
        for key in self.gameState.keys:
            if self.unit.coll_rect.colliderect(key.coll_rect):
                if abs(key.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(key.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(key.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(key.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    key.PickUpKey(self.ui, self.gameState, self.gameState.inventory)
                    self.ui.getitem_sound.play()
                    return
                
        # Collision detection for the clocks
        for clock in self.gameState.clocks:
            if self.unit.coll_rect.colliderect(clock.coll_rect):
                if abs(clock.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(clock.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(clock.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(clock.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    clock.wakeUp(self.gameState)
                    return
        
        # Collision detection for the other mobs
        for other_unit in self.gameState.units:
            if not other_unit.isWiz() and self.unit.coll_rect.colliderect(other_unit.coll_rect):
                if abs(other_unit.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(other_unit.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(other_unit.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(other_unit.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    # Start a fight
                    print("Start fight!")
                    self.ui.fighting_unit = other_unit
                    self.ui.fight_state_tick = pygame.time.get_ticks()
                    self.gameState.state = 'fight_state'
                    print("Your Healh is: ", self.unit.health)
                    print("Enemy's Health is: ", other_unit.health)
                    if other_unit.isBoss == False:
                        pygame.mixer.music.load("SFX/fight_song.mp3")
                        pygame.mixer.music.play(loops=-1)
                    else:
                        pygame.mixer.music.load("SFX/boss_song.mp3")
                        pygame.mixer.music.play(loops=-1)
                    return
            elif other_unit.isWiz() and self.unit.coll_rect.colliderect(other_unit.coll_rect):
                if abs(other_unit.coll_rect.top - self.unit.coll_rect.bottom) < collision_tolerance or \
                abs(other_unit.coll_rect.bottom - self.unit.coll_rect.top) < collision_tolerance or \
                abs(other_unit.coll_rect.right - self.unit.coll_rect.left) < collision_tolerance or \
                abs(other_unit.coll_rect.left - self.unit.coll_rect.right) < collision_tolerance:
                    self.unit.coll_rect.move_ip(-int(self.moveVector.x * 64), -int(self.moveVector.y * 64))
                    # Start a fight
                    print("Start fight!")
                    self.ui.fighting_unit = self.unit
                    self.ui.fight_state_tick = pygame.time.get_ticks()
                    self.gameState.state = 'fight_state'
                    print("Your Healh is: ", other_unit.health)
                    print("Enemy's Health is: ", self.unit.health)
                    if self.unit.isBoss == False:
                        pygame.mixer.music.load("SFX/fight_song.mp3")
                        pygame.mixer.music.play(loops=-1)
                    else:
                        pygame.mixer.music.load("SFX/boss_song.mp3")
                        pygame.mixer.music.play(loops=-1)
                    return
        
        self.unit.position = newPos
        
class AttackCommand(Command):
    
    def __init__(self, ui, gameState, active_attack):
        self.gameState = gameState
        self.ui = ui
        self.active_attack = active_attack
        
    def run(self):
        if self.ui.player_unit.mana >= self.ui.player_unit.attacks_manacost[self.active_attack]:
            self.ui.player_attacks = True
            self.ui.attack_tick = pygame.time.get_ticks()
            self.ui.fighting_unit.health -= self.ui.player_unit.attacks[self.active_attack]
            self.ui.player_unit.mana -= self.ui.player_unit.attacks_manacost[self.active_attack]
            # The moment of your attack is tracked by this bool
            if self.ui.fighting_unit.health > 0:
                # Make a list out of the possible attacks of the fighting mob and chhose one attack randomly
                attack_list = list(self.ui.fighting_unit.attacks.items())
                self.ui.enemy_random_attack = random.choice(attack_list)
                print(self.ui.enemy_random_attack)
                # The moment of the enemy's attack is tracked by this other bool
                self.ui.enemy_attacks = True
                self.ui.player_unit.health -= int(self.ui.enemy_random_attack[1])
                self.ui.enemy_attacks = False
                if self.ui.player_unit.health > 0:
                    print("Your Healh is: ", self.ui.player_unit.health)
                    print("Enemy's Health is: ", self.ui.fighting_unit.health)
                    # self.ui.selected_attack = self.ui.attack_list[0]
                    return
                else:
                    self.ui.player_unit.health = 0
            else:
                print("Your Healh is: ", self.ui.player_unit.health)
                print("Enemy's Health is: 0")
                self.ui.fighting_unit.summonClock(self.gameState)
        else:
            pass
           
class Layer():
    
    def __init__(self, ui, imageFile):
        self.ui = ui
        self.texture = pygame.image.load(imageFile)
        
    def renderTile(self, surface, position, tile, size = Vector2(1,1), angle = 0, isFlipped = False, scale = False):
        # Location on screen
        spritePoint = position.elementwise() * self.ui.cellSize
        
        # Texture
        texturePoint = tile.elementwise()*self.ui.cellSize
        textureRect = Rect(int(texturePoint.x), int(texturePoint.y), self.ui.cellWidth * int(size.x), self.ui.cellHeight * int(size.y))

        # Draw it out
        if angle == 0 and isFlipped == False and scale == False:
            surface.blit(self.texture, spritePoint, textureRect)
        elif angle != 0 and isFlipped == False and scale == False:
            # Extract the tile in the surface
            textureTile = pygame.Surface((self.ui.cellWidth * int(size.x), self.ui.cellHeight * int(size.y)), pygame.SRCALPHA)
            textureTile.blit(self.texture, (0,0), textureRect)
            # Rotate the surface with the tile
            rotatedTile = pygame.transform.rotate(textureTile, angle)
            # Compute the new coordinate on the screen, knowing that we rotate around the center of the tile
            spritePoint.x -= (rotatedTile.get_width() - textureTile.get_width()) // 2
            spritePoint.y -= (rotatedTile.get_height() - textureTile.get_height()) // 2
            # Render the rotated tile
            surface.blit(rotatedTile, spritePoint)
        elif angle == 0 and isFlipped == True and scale == False:
            # Extract the tile in the surface
            textureTile = pygame.Surface((self.ui.cellWidth * int(size.x), self.ui.cellHeight * int(size.y)), pygame.SRCALPHA)
            textureTile.blit(self.texture, (0,0), textureRect)
            flippedTile = pygame.transform.flip(textureTile, True, False)
            surface.blit(flippedTile, spritePoint)
        elif angle == 0 and isFlipped == False and scale == True:
            # Extract the tile in the surface
            textureTile = pygame.Surface((self.ui.cellWidth * int(size.x), self.ui.cellHeight * int(size.y)), pygame.SRCALPHA)
            textureTile.blit(self.texture, (0,0), textureRect)
            scaledTile = pygame.transform.scale2x(textureTile)
            surface.blit(scaledTile, spritePoint)
            
    
    def render(self, surface):
        raise NotImplementedError()    # note to self, to include it
        
class TitleLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.frameCounter = ui.frameCounter
        
    def render(self, surface):
        if self.gameState.state == 'title_screen':
            self.renderTile(surface, Vector2(0,0), Vector2(0,0), self.gameState.worldSize)    # Ha van ott valami akkor rajzolja ki
            self.frameCounter += 1
            if not self.frameCounter % 30:
                pass
                self.frameCounter = 0
            elif not self.frameCounter < 15:
                pygame.draw.rect(surface, (0,0,0), (128, 480, 256, 32))
                
class EndScreenLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def renderText(self, surface, text, position, color):
        text_surface =  self.ui.game_font.render(text, True, color)
        surface.blit(text_surface, position)
        
    def render(self, surface):
        pass
        if self.gameState.state == 'awake':
            self.renderText(surface, "You woke up.", (336,668), (255,255,255))
            
class GameOverLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def renderText(self, surface, text, position, color):
        text_surface =  self.ui.game_font.render(text, True, color)
        surface.blit(text_surface, position)
        
    def render(self, surface):
        if self.gameState.state == 'game_over':
            surface.fill((0,0,0))
            self.renderText(surface, "You have died, but thats's okay.", (128,192), (255,255,255))
            self.renderText(surface, "You can start again by pressing space.", (128,256), (255,255,255))
            if self.gameState.played_gameoversound == False:
                pygame.mixer.music.stop()
                self.ui.gameover_sound.play()
                self.gameState.played_gameoversound = True
                  
class GroundLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def render(self, surface):
        for y in range(self.gameState.worldHeight):
            for x in range(self.gameState.worldWidth):
                tile = self.gameState.ground[y][x]
                if not tile is None:
                    self.renderTile(surface, Vector2(x,y), tile)
                    
class WallsLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def render(self, surface):
        for y in range(self.gameState.worldHeight):
            for x in range(self.gameState.worldWidth):
                tile = self.gameState.walls[y][x]
                if not tile is None:
                    self.renderTile(surface, Vector2(x,y), tile)

class UnitsLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.frameCounter = ui.frameCounter
        
    def render(self, surface):
        if self.ui.new_room_entered == True:
            self.frameCounter = 0
            
        self.frameCounter += 1
        for unit in self.gameState.units:
            # If the unit is not a wizard, then go through their 4 frame animation cycle
            if unit.isWiz() == False:
                if unit.name == "Haunted Mask" and unit.moveVector.y < 0:
                    self.renderTile(surface, unit.position, unit.tile)
                    self.frameCounter = 0
                else:  
                    if not self.frameCounter % 60:
                        unit.tile.x -= 3
                        self.frameCounter = 0
                    elif not self.frameCounter % 15:
                        unit.tile.x += 1
                self.renderTile(surface, unit.position, unit.tile)
                
            else:
                self.renderTile(surface, Vector2(unit.coll_rect.x / 64, unit.coll_rect.y / 64), unit.tile)
            
class BackgroundLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState, size):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.size = size
        self.backgroundAngle = ui.backgroundAngle
        self.frameCounter = ui.frameCounter
        
    def render(self, surface):
        self.frameCounter += 1
        if not self.frameCounter % 15:
            self.backgroundAngle += 90
            self.frameCounter = 0
            
        for y in range(0, self.gameState.worldHeight, int(self.size.x)):
            for x in range(0, self.gameState.worldWidth, int(self.size.y)):
                self.renderTile(surface, Vector2(x,y), self.gameState.background, self.size, self.backgroundAngle)
                
class TorchLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState, size):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.size = size
        self.frameCounter = ui.frameCounter
        
    def render(self, surface):
        if self.ui.new_room_entered == True:
            self.frameCounter = 0
            
        self.frameCounter += 1
        for torch in self.gameState.torches:
            if not self.frameCounter % 30:
                torch.tile.x -=2
                self.frameCounter = 0
            elif not self.frameCounter % 15:
                torch.tile.x +=2
            self.renderTile(surface, torch.position, torch.tile, self.size, 0, torch.isFlipped)
            
class DoorsLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def render(self, surface):
        for door in self.gameState.doors:
            door.openDoor(self.gameState)
            self.renderTile(surface, door.position, door.tile)
            
class ChestLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def render(self, surface):
        for chest in self.gameState.chests:
            self.renderTile(surface, chest.position, chest.tile, Vector2(1,1), 0, chest.isFlipped)
            
class KeyLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def render(self, surface):
        for key in self.gameState.keys:
            self.renderTile(surface, key.position, key.tile)
            
class ClockLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        
    def render(self, surface):
        for clock in self.gameState.clocks:
            self.renderTile(surface, clock.position, clock.tile)
            
class FightBackgroundLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState, size):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.frameCounter = ui.frameCounter
        self.tile = gameState.fight_background
        self.size = size
    
    def render(self, surface):
        if self.gameState.state == 'fight_state':
            self.frameCounter += 1
            if not self.frameCounter % 60:
                self.tile.x -= 3 * self.size.x
                self.frameCounter = 0
            elif not self.frameCounter % 15:
                self.tile.x += self.size.x
            self.renderTile(surface, Vector2(4,2), self.tile, self.size)

class TextBoxLayer(Layer):
    
    def __init__(self, ui, imageFile, gameState):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.healthbox_tile = Vector2(12,19)
        self.healthbox_size =Vector2(3,2)
        self.battlebox_tile = Vector2(0,19)
        self.battlebox_size = Vector2(12,2)
        self.inventorybox_tile = Vector2(15,19)
        self.inventorybox_size = Vector2(7,4)
        self.played_win_song = False
        
    def renderText(self, surface, text, position, color):
        text_surface =  self.ui.game_font.render(text, True, color)
        surface.blit(text_surface, position)
        
    def render(self, surface):
        # Render the health box
        if self.gameState.state != 'awake':
            self.renderTile(surface, Vector2(0,0), self.healthbox_tile, self.healthbox_size)
            self.renderText(surface, "HP      " + str(self.ui.player_unit.health), (20,20), (255,255,255))
            self.renderText(surface, "MP      " + str(self.ui.player_unit.mana), (20,52), (255,255,255))
        
        # Render/Open the invertory if we pressed the e button
        if self.ui.inventory_open == True and self.gameState.state == 'dungeon_floor':
            self.renderTile(surface, Vector2(0,2), self.inventorybox_tile, self.inventorybox_size)
            self.renderText(surface, "Backpack:", (20,148), (255,255,255))
            if len(self.gameState.inventory) != 0:
                for item in self.gameState.inventory:
                    if item == self.ui.selected_item:
                        self.renderText(surface, item.name, (20 + 208 * (self.gameState.inventory.index(item) % 2 ), 196 + 48 * int(self.gameState.inventory.index(item) / 2) ), (255,255,255))
                    else:
                        self.renderText(surface, item.name, (20 + 208 * (self.gameState.inventory.index(item) % 2 ), 196 + 48 * int(self.gameState.inventory.index(item) / 2) ), (155,155,155))
                   
        # Render the items in a chest
        for chest in self.gameState.chests:
            if chest.isOpen == True and self.gameState.state == 'dungeon_floor':
                self.renderTile(surface, Vector2(0,2), self.inventorybox_tile, self.inventorybox_size)
                self.renderText(surface, "Chest:", (20,148), (255,255,255))
                if len(chest.chest_items) != 0:
                    for item in chest.chest_items:
                        if item == self.ui.selected_chest_item:
                            self.renderText(surface, item.name, (20 + 208 * (chest.chest_items.index(item) % 2 ), 196 + 48 * int(chest.chest_items.index(item) / 2) ), (255,255,255))
                        else:
                            self.renderText(surface, item.name, (20 + 208 * (chest.chest_items.index(item) % 2 ), 196 + 48 * int(chest.chest_items.index(item) / 2) ), (155,155,155))
            
        # Render the fight boxt if the game is in fight state
        if self.gameState.state == 'fight_state':
            if pygame.time.get_ticks() - self.ui.fight_state_tick > 500:
                # Draw the black box
                self.renderTile(surface, Vector2(1,10), self.battlebox_tile, self.battlebox_size)
                # Draw the attack names
                if pygame.time.get_ticks() - self.ui.fight_state_tick > 2500:
                    attack_texts = list(self.ui.player_unit.attacks.keys())
                    for text in attack_texts:
                        if text == self.ui.selected_attack:
                            self.renderText(surface, text, (92 + 160 * attack_texts.index(text), 668), (255,255,255))
                            if self.ui.player_attacks == False:
                                self.renderText(surface, str(self.ui.player_unit.attacks_manacost[text]) + " MP" , (92 + 160 * attack_texts.index(text), 716), (255,255,255))
                        else:
                            self.renderText(surface, text, (92 + 160 * attack_texts.index(text), 668), (155,155,155))
                            if self.ui.player_attacks == False:
                                self.renderText(surface, str(self.ui.player_unit.attacks_manacost[text]) + " MP" , (92 + 160 * attack_texts.index(text), 716), (155,155,155))

                # You have encountered ...
                if pygame.time.get_ticks() - self.ui.fight_state_tick < 2500:
                    self.renderText(surface, "You have encountered " + self.ui.fighting_unit.name, (92,668), (255,255,255))          
                # Draw the damage of the attack
                if self.ui.player_attacks == True:
                    # You have used ...
                    if pygame.time.get_ticks() - self.ui.attack_tick < 1000:
                        self.renderText(surface, "You have used " + self.ui.selected_attack, (92,716), (255,255,255))
                    # ... hp of damage the enemy
                    if pygame.time.get_ticks() - self.ui.attack_tick > 2000 and pygame.time.get_ticks() - self.ui.attack_tick < 4000:
                        self.renderText(surface, str(int(self.ui.player_unit.attacks[self.ui.selected_attack])) + " HP of Damage to " + self.ui.fighting_unit.name, (92,716), (255,255,255))                  
                    
                    if self.ui.fighting_unit.health > 0:
                        # Enemy have have used ...
                        if pygame.time.get_ticks() - self.ui.attack_tick > 4000 and pygame.time.get_ticks() - self.ui.attack_tick < 6000:
                            self.renderText(surface, self.ui.fighting_unit.name + " have used " + self.ui.enemy_random_attack[0], (92,716), (255,255,255))
                        # You have suffered .. HP of damage
                        if pygame.time.get_ticks() - self.ui.attack_tick > 6000 and pygame.time.get_ticks() - self.ui.attack_tick < 8000:
                            self.renderText(surface, "You have suffered " + str(self.ui.enemy_random_attack[1]) + " HP of Damage", (92,716), (255,255,255))
                        # Set back everything to normal
                        if pygame.time.get_ticks() - self.ui.attack_tick > 8000:
                            if self.ui.player_unit.health > 0:
                                self.ui.player_attacks = False
                                self.ui.selected_attack = self.ui.attack_list[0]
                                self.ui.enemy_random_attack = None
                            else:
                                self.gameState.gameOver(self.ui)
                    else:
                        if pygame.time.get_ticks() - self.ui.attack_tick > 4000 and pygame.time.get_ticks() - self.ui.attack_tick < 8000:
                            self.renderText(surface, self.ui.fighting_unit.name + " fainted ", (92,716), (255,255,255))
                            
                            if self.played_win_song == False:
                                pygame.mixer.music.load("SFX/win_song.mp3")
                                pygame.mixer.music.play(loops=-1)
                                self.played_win_song = True
                                
                        if pygame.time.get_ticks() - self.ui.attack_tick > 8000:
                            # Remove the enemy from the game
                            self.gameState.units.remove(self.ui.fighting_unit)
                            self.gameState.state = 'dungeon_floor'
                            self.ui.fight_frameCounter = 0
                            self.played_win_song = False
                            self.ui.selected_attack = self.ui.attack_list[0]
                            pygame.mixer.music.load("SFX/dungeon_song.mp3")
                            pygame.mixer.music.play(loops=-1)
                if self.ui.enemy_attacks == True:
                    pass
        
class FightUnitLayer(Layer):
    def __init__(self, ui, imageFile, gameState, size):
        super().__init__(ui, imageFile)
        self.gameState = gameState
        self.ui = ui
        self.size = size
        
    def render(self, surface):
        if self.gameState.state == 'fight_state':
            self.ui.fight_frameCounter += 1
            if not self.ui.fight_frameCounter % 60:
                self.ui.fighting_unit.fight_tile.x -= 3 * self.size.x
                self.ui.fight_frameCounter = 0
            elif not self.ui.fight_frameCounter % 15:
                self.ui.fighting_unit.fight_tile.x += 1 * self.size.x
            self.renderTile(surface, Vector2(6,6), self.ui.fighting_unit.fight_tile, self.size)
        else:
            pass
        
class UserInterface():
    
    def __init__(self):
        pygame.init()
        
        # Make a Game State
        self.gameState = GameState()
        
        # Render properties of a cell in the game and load in the tileset
        self.cellSize = Vector2(64,64)
        
        # Loop properties
        self.clock = pygame.time.Clock()
        self.running = True
        self.backgroundAngle = self.gameState.backgroundAngle
        self.frameCounter = 0
        self.fight_frameCounter = 0
        
        # Room properties
        self.new_room_entered = False
        self.current_room = "room0"
        
        # Window properties
        windowSize = self.gameState.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x),int(windowSize.y)))
        pygame.display.set_caption("Midnight Whirlpool")
        pygame.display.set_icon(pygame.image.load("icon.png"))
        
        # Set up music
        pygame.mixer.music.load("SFX/title_song.mp3")
        pygame.mixer.music.play(loops=-1)
        self.gameover_sound = pygame.mixer.Sound("SFX/gameover_sound.wav")
        self.getitem_sound = pygame.mixer.Sound("SFX/getitem_sound.wav")
        self.getitem_sound.set_volume(0.8)
        self.useitem_sound = pygame.mixer.Sound("SFX/useitem_sound.wav")
        self.useitem_sound.set_volume(0.8)
                
        # Controlls
        self.commands = []
        self.player_unit = self.gameState.units[0]
        
        # Set up an inventory
        self.inventory_open = False
        self.selected_item = None
        
        # Set up chests
        self.selected_chest_item = None
        
        # Set up the fight mechanism
        self.fighting_unit = None
        self.attack_list = list(self.player_unit.attacks.keys())
        self.selected_attack = self.attack_list[0]
        self.enemy_random_attack = None
        self.player_attacks = False
        self.enemy_attacks = False
        self.attack_tick = -8000
        self.fight_state_tick = None
        
        # Font of the gametext
        self.game_font = pygame.font.Font('Minecraft.ttf', 32)

        # The layers of graphics
        self.layers = [
            BackgroundLayer(self, "tileset.png", self.gameState, Vector2(2,2)),
            GroundLayer(self, "tileset.png", self.gameState),
            WallsLayer(self, "tileset.png", self.gameState),
            DoorsLayer(self, "tileset.png", self.gameState),
            TorchLayer(self, "tileset.png", self.gameState, Vector2(2,2)),
            ChestLayer(self, "tileset.png", self.gameState),
            KeyLayer(self, "tileset.png", self.gameState),
            ClockLayer(self, "tileset.png", self.gameState),
            UnitsLayer(self, "tileset.png", self.gameState),
            FightBackgroundLayer(self, "tileset.png", self.gameState, Vector2(6,8)),
            FightUnitLayer(self, "bigmob_tileset.png", self.gameState, Vector2(2,2)),
            TextBoxLayer(self, "tileset.png", self.gameState),
            TitleLayer(self, 'title_tile.png', self.gameState),
            GameOverLayer(self, 'title_tile.png', self.gameState),
            EndScreenLayer(self, 'title_tile.png', self.gameState)
            ]

    @property
    def cellWidth(self):
        return int(self.cellSize.x)
    
    @property
    def cellHeight(self):
        return int(self.cellSize.y)

    def processInput(self):
        if self.gameState.state == 'title_screen' or self.gameState.state == 'game_over':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        break
                    elif event.key == pygame.K_SPACE:
                        self.gameState.state = 'dungeon_floor'
                        pygame.mixer.music.load("SFX/dungeon_song.mp3")
                        pygame.mixer.music.play(loops=-1)
                        break
        
        # Contols of the wizard using the keyboard if its on the dungeon floor
        elif self.gameState.state == 'dungeon_floor' or self.gameState.state == 'awake':
            moveVector = Vector2()
            # see if there are any chests opened
            opened_chests = []
            for chest in self.gameState.chests:
                opened_chests.append(chest.isOpen)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        break
                    # Open a chest if you are next to it with q
                    if event.key == pygame.K_q:
                        for chest in self.gameState.chests:
                            if chest.isColliding == True and chest.isOpen == False:
                                chest.openChest(self)
                                self.inventory_open = False
                            elif chest.isOpen == True:
                                chest.closeChest(self)
                    for chest in self.gameState.chests:
                        if chest.isOpen == True and len(chest.chest_items) != 0:
                            if event.key == pygame.K_d:
                                if chest.chest_items.index(self.selected_chest_item) + 1 < len(chest.chest_items):
                                    self.selected_chest_item = chest.chest_items[ chest.chest_items.index(self.selected_chest_item) + 1 ]
                                else:
                                    self.selected_chest_item = chest.chest_items[0]
                            elif event.key == pygame.K_a:
                                if chest.chest_items.index(self.selected_chest_item) - 1 >= 0:
                                    self.selected_chest_item = chest.chest_items[ chest.chest_items.index(self.selected_chest_item) - 1 ]
                                else:
                                    self.selected_chest_item = chest.chest_items[-1]
                            elif event.key == pygame.K_s:
                                if chest.chest_items.index(self.selected_chest_item) + 2 < len(chest.chest_items):
                                    self.selected_chest_item = chest.chest_items[ chest.chest_items.index(self.selected_chest_item) + 2 ]
                                elif chest.chest_items.index(self.selected_chest_item) == len(chest.chest_items) - 1:
                                    self.selected_chest_item = chest.chest_items[1]
                                elif chest.chest_items.index(self.selected_chest_item) == len(chest.chest_items) - 2:
                                    self.selected_chest_item = chest.chest_items[0]
                            elif event.key == pygame.K_w:
                                if chest.chest_items.index(self.selected_chest_item) - 2 >= 0:
                                    self.selected_chest_item = chest.chest_items[ chest.chest_items.index(self.selected_chest_item) - 2 ]
                                elif chest.chest_items.index(self.selected_chest_item) == 0:
                                    self.selected_chest_item = chest.chest_items[-2]
                                elif chest.chest_items.index(self.selected_chest_item) == 1:
                                    self.selected_chest_item = chest.chest_items[-1]
                            elif event.key == pygame.K_SPACE:
                                # Use the item
                                 chest.getChestItem(self, self.gameState, self.selected_chest_item)
                                 self.getitem_sound.play()
                                 if len(chest.chest_items) != 0:
                                     self.selected_chest_item = chest.chest_items[0]
                                 else:
                                     self.selected_chest_item = None
                                
                    # You can open your inventory with e, if there are no opened chests
                    if event.key == pygame.K_e and not any(opened_chests) and self.gameState.state == 'dungeon_floor':
                        if self.inventory_open == False:
                            self.inventory_open = True
                        elif self.inventory_open == True:
                            self.inventory_open = False
                    if self.inventory_open == True and len(self.gameState.inventory) >= 2:
                        # Navigate in the inventory
                        if event.key == pygame.K_d:
                            if self.gameState.inventory.index(self.selected_item) + 1 < len(self.gameState.inventory):
                                self.selected_item = self.gameState.inventory[ self.gameState.inventory.index(self.selected_item) + 1 ]
                            else:
                                self.selected_item = self.gameState.inventory[0]
                        elif event.key == pygame.K_a:
                            if self.gameState.inventory.index(self.selected_item) - 1 >= 0:
                                self.selected_item = self.gameState.inventory[ self.gameState.inventory.index(self.selected_item) - 1 ]
                            else:
                                self.selected_item = self.gameState.inventory[-1]
                        elif event.key == pygame.K_s:
                            if self.gameState.inventory.index(self.selected_item) + 2 < len(self.gameState.inventory):
                                self.selected_item = self.gameState.inventory[ self.gameState.inventory.index(self.selected_item) + 2 ]
                            elif self.gameState.inventory.index(self.selected_item) == len(self.gameState.inventory) - 1:
                                self.selected_item = self.gameState.inventory[1]
                            elif self.gameState.inventory.index(self.selected_item) == len(self.gameState.inventory) - 2:
                                self.selected_item = self.gameState.inventory[0]
                        elif event.key == pygame.K_w:
                            if self.gameState.inventory.index(self.selected_item) - 2 >= 0:
                                self.selected_item = self.gameState.inventory[ self.gameState.inventory.index(self.selected_item) - 2 ]
                            elif self.gameState.inventory.index(self.selected_item) == 0:
                                self.selected_item = self.gameState.inventory[-2]
                            elif self.gameState.inventory.index(self.selected_item) == 1:
                                self.selected_item = self.gameState.inventory[-1]
                    if self.inventory_open == True and len(self.gameState.inventory) != 0:
                        if event.key == pygame.K_SPACE:
                            # Use the item
                             self.gameState.inventory[self.gameState.inventory.index(self.selected_item)].use()
                             self.useitem_sound.play()
                             if len(self.gameState.inventory) != 0:
                                 self.selected_item = self.gameState.inventory[0]
                             else:
                                 self.selected_item = None
                            
            if self.inventory_open == False and not any(opened_chests):
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_d]:
                    moveVector.x = 0.1
                if pressed[pygame.K_a]: 
                    moveVector.x = -0.1
                if pressed[pygame.K_s]:
                    moveVector.y = 0.1
                if pressed[pygame.K_w]:
                    moveVector.y = -0.1
                    
                for mob in self.gameState.units:
                    if mob.isWiz() == False and mob.name =="Haunted Mask":
                        mask_command = MoveCommand(self, self.gameState, mob, mob.moveVector)
                        self.commands.append(mask_command)
                            
                # Keyboard contolls the wizard
                if moveVector.x != 0 or moveVector.y != 0:
                    command = MoveCommand(self, self.gameState, self.player_unit, moveVector)
                    self.commands.append(command)
                
        elif self.gameState.state == 'fight_state':
            if pygame.time.get_ticks() - self.fight_state_tick > 2500 and pygame.time.get_ticks() - self.attack_tick > 8000:
                active_attack = None
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            break
                        # set up the attacks
                        elif event.key == pygame.K_d:
                            if self.attack_list.index(self.selected_attack) + 1 < len(self.attack_list):
                                self.selected_attack = self.attack_list[ self.attack_list.index(self.selected_attack) + 1 ]
                            else:
                                self.selected_attack = self.attack_list[0]
                        elif event.key == pygame.K_a:
                            if self.attack_list.index(self.selected_attack) - 1 >= 0:
                                self.selected_attack = self.attack_list[ self.attack_list.index(self.selected_attack) - 1 ]
                            else:
                                self.selected_attack = self.attack_list[-1]
                        elif event.key == pygame.K_SPACE:
                            active_attack = self.selected_attack
                            
                if not active_attack is None:
                    command = AttackCommand(self, self.gameState, active_attack)
                    self.commands.append(command)
            else:
                 for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        break
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            break
                        # set up the attacks
                        elif event.key == pygame.K_d:
                            pass
                        elif event.key == pygame.K_a:
                            pass
                        elif event.key == pygame.K_SPACE:
                            pass
                
    def update(self):
        for command in self.commands:
            command.run()
        self.commands.clear()    # Empty the commands list
        
    def render(self):
        for layer in self.layers:
            layer.render(self.window)
        
        pygame.display.update()
                
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60) # 60
            
            
userinterface = UserInterface()
userinterface.run()
pygame.quit()
sys.exit()