import pygame
from level_data.level_01 import level_01

# things to fix marked with xxxx

# chloe box
# probie swap
# probie fling
# special rotation
# add more gates
# make some levels
# redo player sprites
# level select
# main menu
# level editor
# sound effects

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
running = True


size = 48
wall = pygame.image.load('images/wall.png')
floor = pygame.image.load('images/floor.png')

natalie_img = pygame.image.load('images/natalie.png')
natalie_select_img = pygame.image.load('images/natalie_select.png')
chloe_img = pygame.image.load('images/chloe.png')
chloe_select_img = pygame.image.load('images/chloe_select.png')
probie_img = pygame.image.load('images/probie.png')
probie_select_img = pygame.image.load('images/probie_select.png')

rbh = pygame.image.load('images/rb_horgate.png')
robh = pygame.image.load('images/rob_horgate.png')
rboh = pygame.image.load('images/rbo_horgate.png')
roboh = pygame.image.load('images/robo_horgate.png')
red_button = pygame.image.load('images/red_button.png')
blue_button = pygame.image.load('images/blue_button.png')

my_font = pygame.font.SysFont("Roboto", 30)
text_surface = my_font.render("Level " + level_01[0][0], False, (155,155,155))

button_list = ["red", "blu", "gre"]
can_move = ["-  ", "red", "blu", "gre", "roboh"]
occupied = []
active_buttons = []

move_val = 1


def can_move_to (move_x, move_y):
  return curr_stage[move_y][move_x] in can_move and [move_x, move_y] not in occupied

# prev x and y are where we started
# curr x and y are where we end up
def movement(prev_x, prev_y, curr_x, curr_y):
  occupied.remove([prev_x, prev_y])
  occupied.append([curr_x, curr_y])
  # track all tiles that have a player type thing on them

  # weird, want to fix this xxxx
  prev_tile = curr_stage[prev_y][prev_x]
  if prev_tile == s_p.get_name() + "  ":
    curr_stage[prev_y][prev_x] = "-  "
  if prev_tile in button_list:
    active_buttons.remove(prev_tile)
  if curr_stage[curr_y][curr_x] in button_list:
    active_buttons.append(curr_stage[curr_y][curr_x])
  # update which buttons are held
  n.set_ling_jump(False)


class Player:
  def __init__(self, x, y, name, img, selec_img, selected = False):
    self.x = x
    self.y = y
    self.name = name
    self.img = img
    self.selec_img = selec_img
    self.selected = selected
    self.ling_jump = False

  def get_x(self):
    return self.x

  def set_x(self, x):
    self.x = x

  def get_y(self):
    return self.y
  
  def set_y(self, y):
    self.y = y

  def get_name(self):
    return self.name

  def is_selected(self):
    return self.selected

  def get_img(self):
    if self.is_selected():
      return self.selec_img
    else:
      return self.img

  def set_selected(self, val):
    self.selected = val

  def is_ling_jump(self):
    return self.ling_jump

  def set_ling_jump(self, val):
    self.ling_jump = val

c = Player(0, 0, "c", chloe_img, chloe_select_img, True)
p = Player(1, 0, "p", probie_img, probie_select_img, False)
n = Player(1, 1, "n", natalie_img, natalie_select_img, False)

curr_level = level_01
curr_stage = curr_level.copy()

for [row_num, row] in enumerate(curr_stage):
  for [col_num, ele] in enumerate(row):
    dest = (col_num, row_num)
    match ele:
      case 'c  ':
        c.set_x(dest[0])
        c.set_y(dest[1])
        occupied.append([c.get_x(), c.get_y()])
      case 'p  ':
        p.set_x(dest[0])
        p.set_y(dest[1])
        occupied.append([p.get_x(), p.get_y()])
      case 'n  ':
        n.set_x(dest[0])
        n.set_y(dest[1])
        occupied.append([n.get_x(), n.get_y()])

if c.is_selected:
  s_p = c
elif p.is_selected:
  s_p = p
else:
  s_p = n

x_int = s_p.get_x()
y_int = s_p.get_y()
if curr_stage[y_int][x_int] in button_list:
  active_buttons.append(curr_stage[y_int][x_int])



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  for event in pygame.event.get():
    x_int = s_p.get_x()
    y_int = s_p.get_y()
    if s_p.is_ling_jump():
      move_val = 2
    else:
      move_val = 1
    prev_tile = curr_stage[y_int][x_int]
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        if x_int > move_val - 1 and can_move_to(x_int - move_val, y_int):
          movement(x_int, y_int, x_int - move_val, y_int)
          s_p.set_x(s_p.get_x() - move_val)
      elif event.key == pygame.K_UP:
        if y_int > move_val - 1 and can_move_to(x_int, y_int - move_val):
          movement(x_int, y_int, x_int, y_int - move_val)
          s_p.set_y(s_p.get_y() - move_val)
      elif event.key == pygame.K_RIGHT:
        if x_int < len(curr_stage[0]) - move_val and can_move_to(x_int + move_val, y_int):
          movement(x_int, y_int, x_int + move_val, y_int)
          s_p.set_x(s_p.get_x() + move_val)
      elif event.key == pygame.K_DOWN:
        if y_int < len(curr_stage) - move_val and can_move_to(x_int,y_int + move_val):
          movement(x_int, y_int, x_int, y_int + move_val)
          s_p.set_y(s_p.get_y() + move_val)
      elif event.key == pygame.K_LCTRL:
        if c.is_selected():
          c.set_selected(False)
          p.set_selected(True)
          s_p = p
        elif p.is_selected():
          p.set_selected(False)
          n.set_selected(True)
          s_p = n
        else:
          n.set_selected(False)
          c.set_selected(True)
          s_p = c
      elif event.key == pygame.K_k:
        if n.is_selected():
          s_p.set_ling_jump(not s_p.is_ling_jump())
      elif event.key == pygame.K_a:
        print(n.ling_jump)


  # screen.blit(floor_tile_01, (0,0))
  screen.fill("black")  
  # fill the screen with a color to wipe away anything from last frame

  # RENDER YOUR GAME HERE

  for [row_num, row] in enumerate(curr_stage):
    for [col_num, ele] in enumerate(row):
      dest_size = (col_num * size, row_num * size)
      match ele:
        case '-  ':
          screen.blit(floor, dest_size)
        case 'l  ':
          screen.blit(wall, dest_size)
        case 'c  ':
          screen.blit(floor, dest_size)
        case 'p  ':
          screen.blit(floor, dest_size)
        case 'n  ':
          screen.blit(floor, dest_size)
        case 'red':
          screen.blit(red_button, dest_size)
        case 'blu':
          screen.blit(blue_button, dest_size)
        case 'rbh' | 'robh' | 'rboh' | 'roboh':
          if "red" in active_buttons and "blu" in active_buttons:
            curr_stage[row_num][col_num] = 'roboh'
            screen.blit(roboh, dest_size)
          elif "red" in active_buttons:
            curr_stage[row_num][col_num] = 'robh'
            screen.blit(robh, dest_size)
          elif "blu" in active_buttons:
            curr_stage[row_num][col_num] = 'rboh'
            screen.blit(rboh, dest_size)
          else:
            curr_stage[row_num][col_num] = 'rbh'
            screen.blit(rbh, dest_size)




  screen.blit(c.get_img(), (c.get_x() * size,c.get_y() * size))
  screen.blit(p.get_img(), (p.get_x() * size,p.get_y() * size))
  screen.blit(n.get_img(), (n.get_x() * size,n.get_y() * size))




  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()