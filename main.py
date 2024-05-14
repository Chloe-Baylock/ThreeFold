import pygame
from level_data.level_01 import level_01

# ling jump
# other specials

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
# cannot_move = ["l  ", "c  ", "p  ", "n  ", "rbh", "robh", "rboh"]
active_buttons = []


class Player:
  def __init__(self, x, y, name, img, selected = False):
    self.x = x
    self.y = y
    self.name = name
    self.selected = selected
    self.img = img

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
    return self.img

  def set_selected(self, val):
    self.selected = val

c = Player(0, 0, "c", chloe_img, True)
p = Player(size, 0, "p", probie_img, False)
n = Player(size, size, "n", natalie_img, False)

curr_level = level_01
curr_stage = curr_level.copy()

for [row_num, row] in enumerate(curr_stage):
  for [col_num, ele] in enumerate(row):
    dest = (col_num * size, row_num * size)
    match ele:
      case 'c  ':
        c.set_x(dest[0])
        c.set_y(dest[1])
        occupied.append([int(c.get_x() / size), int(c.get_y() / size)])
      case 'p  ':
        p.set_x(dest[0])
        p.set_y(dest[1])
        occupied.append([int(p.get_x() / size), int(p.get_y() / size)])
      case 'n  ':
        n.set_x(dest[0])
        n.set_y(dest[1])
        occupied.append([int(n.get_x() / size), int(n.get_y() / size)])

if c.is_selected:
  s_p = c
elif p.is_selected:
  s_p = p
else:
  s_p = n

x_int = int(s_p.get_x() / size)
y_int = int(s_p.get_y() / size)
if curr_stage[y_int][y_int] in button_list:
  active_buttons.append(curr_stage[y_int][y_int])



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window


  for event in pygame.event.get():
    x_int = int(s_p.get_x() / size)
    y_int = int(s_p.get_y() / size)
    prev_tile = curr_stage[y_int][x_int]
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        if x_int > 0 and curr_stage[y_int][x_int - 1] in can_move and [x_int - 1, y_int] not in occupied:
          print([x_int,y_int])
          occupied.remove([x_int,y_int])
          occupied.append([x_int - 1,y_int])
          if prev_tile == s_p.get_name() + "  ":
            curr_stage[y_int][x_int] = "-  "
          if prev_tile in button_list:
            active_buttons.remove(prev_tile)
          if curr_stage[y_int][x_int - 1] in button_list:
            active_buttons.append(curr_stage[y_int][x_int - 1])
          s_p.set_x(s_p.get_x() - size)
      elif event.key == pygame.K_UP:
        if y_int > 0 and curr_stage[y_int - 1][x_int] in can_move and [x_int, y_int - 1] not in occupied:
          occupied.remove([x_int,y_int])
          occupied.append([x_int,y_int - 1])
          if prev_tile == s_p.get_name() + "  ":
            curr_stage[y_int][x_int] = "-  "
          if prev_tile in button_list:
            active_buttons.remove(prev_tile)
          if curr_stage[y_int - 1][x_int] in button_list:
            active_buttons.append(curr_stage[y_int - 1][x_int])
          s_p.set_y(s_p.get_y() - size)
      elif event.key == pygame.K_RIGHT:
        if x_int < len(curr_stage[0]) - 1 and curr_stage[y_int][x_int + 1] in can_move and [x_int + 1, y_int] not in occupied:
          occupied.remove([x_int,y_int])
          occupied.append([x_int + 1, y_int])
          if prev_tile == s_p.get_name() + "  ":
            curr_stage[y_int][x_int] = "-  "
          if prev_tile in button_list:
            active_buttons.remove(prev_tile)
          if curr_stage[y_int][x_int + 1] in button_list:
            active_buttons.append(curr_stage[y_int][x_int + 1])
          s_p.set_x(s_p.get_x() + size)
      elif event.key == pygame.K_DOWN:
        if y_int < len(curr_stage) - 1 and curr_stage[y_int + 1][x_int] in can_move and [x_int, y_int + 1] not in occupied:
          occupied.remove([x_int,y_int])
          occupied.append([x_int,y_int + 1])
          if prev_tile == s_p.get_name() + "  ":
            curr_stage[y_int][x_int] = "-  "
          if prev_tile in button_list:
            active_buttons.remove(prev_tile)
          if curr_stage[y_int + 1][x_int] in button_list:
            active_buttons.append(curr_stage[y_int + 1][x_int])
          s_p.set_y(s_p.get_y() + size)
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
      elif event.key == pygame.K_a:
        print(occupied)
        print(curr_level)


  # screen.blit(floor_tile_01, (0,0))
  screen.fill("black")  
  # fill the screen with a color to wipe away anything from last frame

  # RENDER YOUR GAME HERE

  for [row_num, row] in enumerate(curr_stage):
    for [col_num, ele] in enumerate(row):
      dest = (col_num * size, row_num * size)
      match ele:
        case '-  ':
          screen.blit(floor, dest)
        case 'l  ':
          screen.blit(wall, dest)
        case 'c  ':
          screen.blit(floor, dest)
        case 'p  ':
          screen.blit(floor, dest)
        case 'n  ':
          screen.blit(floor, dest)
        case 'red':
          screen.blit(red_button, dest)
        case 'blu':
          screen.blit(blue_button, dest)
        case 'rbh' | 'robh' | 'rboh' | 'roboh':
          if "red" in active_buttons and "blu" in active_buttons:
            curr_stage[row_num][col_num] = 'roboh'
            screen.blit(roboh, dest)
          elif "red" in active_buttons:
            curr_stage[row_num][col_num] = 'robh'
            screen.blit(robh, dest)
          elif "blu" in active_buttons:
            curr_stage[row_num][col_num] = 'rboh'
            screen.blit(rboh, dest)
          else:
            curr_stage[row_num][col_num] = 'rbh'
            screen.blit(rbh, dest)


  # text_surface = my_font.render("Level " + curr_level[0][2], False, (155,155,155))
  # screen.blit(text_surface, (64,64))


  screen.blit(c.get_img(), (c.get_x(),c.get_y()))
  screen.blit(p.get_img(), (p.get_x(),p.get_y()))
  screen.blit(n.get_img(), (n.get_x(),n.get_y()))




  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()