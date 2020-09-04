import pygame
import math
import time

class Cell:
    def __init__(self, index, rect, colors, value = None):
        self.value = value
        self.rect = rect
        self.colors = colors
        self.index = index

    def get_cell_value(self):
        return self.value

    def get_cell_index(self):
        return self.index

    def get_center(self):
        x, y, w, h = self.rect
        return x + w//2, y + h//2
    
    def change_color(self, colors):
        self.colors = colors
       

    def render(self,surface, contour = None):
        color, cont_color = self.colors
        pygame.draw.rect(surface,color, self.rect)
        if contour:
            pygame.draw.rect(surface,cont_color,self.rect, contour)

    def redraw_site(self, surface, colors):
        self.change_color(colors)
        self.render(surface)

    def __repr__(self):
        return f'cell_index:{self.index},rect:{self.rect}'
    


class Grid:
    def __init__(self, surface, rows,cols, start_point, colors, values = None):
        self.grid = []
        self.surface = surface
 
        self.x, self.y  = start_point
        self.rows, self.cols = rows, cols
        self.values = values
        self.colors = colors
 

    def calculate_cell_dim(self):
        _,_,width, height = self.surface.get_rect()
         
        cell_width = (width - 2*self.x) // self.cols
        cell_height = (height - 2*self.y) // self.rows
        return cell_width, cell_height

    def set_grid(self):
        cell_width, cell_height = self.calculate_cell_dim()
        x, y  = self.x, self.y
        for i in range(self.rows * self.cols):
            x += cell_width
            if not i % self.cols:
                y += cell_height if i > 0 else 0
                x = self.x
            cell_rect = pygame.Rect(x,y, cell_width, cell_height)
           
            cell = Cell(i, cell_rect, self.colors,
                        value = self.values[i] if self.values else None)
            self.grid.append(cell)
        


    def ind_to_rowcol(self, i):
        return divmod(i, self.cols)

    def get_cell(self, r, c):
        return self.grid[r*self.cols + c]


    def display_grid(self):
        for cell in self.grid:
            cell.render(self.surface)

    def __repr__(self):
        s = ''
        for i in range(len(self.grid)):
            s += str(self.grid[i])
        return s
                    


class Passage():
    def __init__(self, grid, path, width, color):
        self.grid = grid
        self.path = path
        self.width = width
        self.color = color



    def display_passage(self, surface):
        prev_cell = self.grid.get_cell(*self.path[0])
        
        prev = prev_cell.get_center()
        i = 1
        while i < len(self.path):
            cur_cell = self.grid.get_cell(*self.path[i])
            cur = cur_cell.get_center()
            pygame.draw.line(surface,self.color, prev, cur, self.width)
            prev = cur
            i += 1
            
            
            
    
     

class Message:
    def __init__(self, surface, msg, font, font_size, msg_center, color, background_color = None):
        
        self.surface = surface
        text_font = pygame.font.Font(font, font_size)
        self.textSurface = text_font.render(msg, True, color)
        self.textRect = self.textSurface.get_rect()
        self.textRect.center = msg_center
        self.background_color = background_color
        if background_color:
            background_rect = surface.subsurface(self.textRect)
            background_rect.fill(background_color)
 

    def display_msg(self):
        
        self.surface.blit(self.textSurface, self.textRect)
  
        
    def clear_msg(self):
        clean_surf = self.textRect.inflate(20,0)
        clean_surf = self.surface.subsurface(clean_surf)
        
        if self.background_color:
            clean_surf.fill(self.bacground_color)
        else:
            clean_surf.fill((255,255,255))
        

  
            
