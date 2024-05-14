import pygame
from level_data.level_01 import level_01

# make walls
# make gates
# make buttons
# make 3 players
# ling jump
# other specials

# pygame setup
pygame.init()

# screen = pygame.display.set_mode((1280, 720))
screen = pygame.display.set_mode((1080, 920))
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

my_font = pygame.font.SysFont("Roboto", 30)
text_surface = my_font.render("Level " + level_01[0][0], False, (155,155,155))

class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def get_x(self):
    return self.x

  def set_x(self, x):
    self.x = x

  def get_y(self):
    return self.y
  
  def set_y(self, y):
    self.y = y


p = Player(size,size)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

  x_int = int(p.get_x() / size)
  y_int = int(p.get_y() / size)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        if x_int > 0 and level_01[y_int][x_int - 1] == "-":
          p.set_x(p.get_x() - size)
      if event.key == pygame.K_UP:
        if y_int > 0 and level_01[y_int - 1][x_int] == "-":
          p.set_y(p.get_y() - size)
      if event.key == pygame.K_RIGHT:
        if x_int < len(level_01[0]) - 1 and level_01[y_int][x_int + 1] == "-":
          p.set_x(p.get_x() + size)
      if event.key == pygame.K_DOWN:
        if y_int < len(level_01) - 1 and level_01[y_int + 1][x_int] == "-":
          p.set_y(p.get_y() + size)


  # screen.blit(floor_tile_01, (0,0))
  screen.fill("black")  
  # fill the screen with a color to wipe away anything from last frame

  # RENDER YOUR GAME HERE

  for [row_num, row] in enumerate(level_01):
    for [col_num, ele] in enumerate(row):
      dest = (col_num * size, row_num * size)
      match ele:
        case '-':
          screen.blit(floor, dest)
        case 'l':
          screen.blit(wall, dest)
        case 'c':
          screen.blit(chloe_img, dest)
        case 'p':
          screen.blit(probie_img, dest)
        case 'n':
          screen.blit(natalie_img, dest)


  # text_surface = my_font.render("Level " + level_01[0][2], False, (155,155,155))
  # screen.blit(text_surface, (64,64))


  
  pygame.draw.rect(screen, "lime", (p.get_x(),p.get_y(),size,size))




  # flip() the display to put your work on screen
  pygame.display.flip()


  dt = clock.tick(60) / 1000

pygame.quit()