import pygame
import math

pygame.init()

# Window dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# Create the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Menstrual Cycle Simulation")
window.fill((255, 255, 255))

# Dimensions of the sprites
CL_LARGE_WIDTH = 30
CL_LARGE_HEIGHT = 30
CL_MEDIUM_WIDTH = 25
CL_MEDIUM_HEIGHT = 25
CL_SMALL_WIDTH = 20
CL_SMALL_HEIGHT = 20
EGG_WIDTH = 20
EGG_HEIGHT = 20
FOLLICLE_LARGE_WIDTH = 30
FOLLICLE_LARGE_HEIGHT = 30
FOLLICLE_MEDIUM_WIDTH = 25
FOLLICLE_MEDIUM_HEIGHT = 25
FOLLICLE_SMALL_WIDTH = 20
FOLLICLE_SMALL_HEIGHT = 20
ESTROGEN_WIDTH = 10
ESTROGEN_HEIGHT = 10
PROGESTERONE_WIDTH = 10
PROGESTERONE_HEIGHT = 10
LH_WIDTH = 10
LH_HEIGHT = 10
FSH_WIDTH = 10
FSH_HEIGHT = 10
TIME_SLIDER_WIDTH = 15
TIME_SLIDER_HEIGHT = 15
ESTROGEN_SLIDER_WIDTH = 10
ESTROGEN_SLIDER_HEIGHT = 10
PROGESTERONE_SLIDER_WIDTH = 10
PROGESTERONE_SLIDER_HEIGHT = 10
LH_SLIDER_WIDTH = 10
LH_SLIDER_HEIGHT = 10
FSH_SLIDER_WIDTH = 10
FSH_SLIDER_HEIGHT = 10

# Speeds of sprites
ESTROGEN_SPEED = 5
PROGESTERONE_SPEED = 5
LH_SPEED = -5
FSH_SPEED = -5

ANIMATION_INTERVAL = 200
ESTROGEN_SPAWN_INTERVAL = 150
PROGESTERONE_SPAWN_INTERVAL = 150
LH_SPAWN_INTERVAL = 150
FSH_SPAWN_INTERVAL = 150


# Creating Main Simulation Image
backgroundimage = pygame.image.load("Background image.png")
backgroundimage = pygame.transform.scale(backgroundimage, (755, 760))
backgroundimage_rect = backgroundimage.get_rect()

#Centering the image
WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()
backgroundimage_x = (WINDOW_WIDTH - backgroundimage_rect.width) // 2
backgroundimage_y = (WINDOW_HEIGHT - backgroundimage_rect.height) // 2

# Load static images and scale images
background_image = pygame.image.load('Background image.png').convert_alpha()
cl_large_image = pygame.image.load('corpus luteum large.png').convert_alpha()
cl_large_image = pygame.transform.scale(cl_large_image, (50, 50))
cl_medium_image = pygame.image.load('corpus luteum medium.png').convert_alpha()
cl_medium_image = pygame.transform.scale(cl_medium_image, (40, 40))
cl_small_image = pygame.image.load('corpus luteum small.png').convert_alpha()
cl_small_image = pygame.transform.scale(cl_small_image, (30, 30))
egg_cell_image = pygame.image.load('egg cell.png').convert_alpha()
egg_cell_image = pygame.transform.scale(egg_cell_image, (20, 20))
estrogen_molecule_image = pygame.image.load('estrogen molecule.png').convert_alpha()
estrogen_molecule_image = pygame.transform.scale(estrogen_molecule_image, (20, 20))
progesterone_molecule_image = pygame.image.load('progesterone molecule.png').convert_alpha()
progesterone_molecule_image = pygame.transform.scale(progesterone_molecule_image, (20, 20))
FSH_molecule_image = pygame.image.load('FSH molecule.png').convert_alpha()
FSH_molecule_image = pygame.transform.scale(FSH_molecule_image, (20, 20))
LH_molecule_image = pygame.image.load('LH molecule.png').convert_alpha()
LH_molecule_image = pygame.transform.scale(LH_molecule_image, (20, 20))
follicle_ovulates_image = pygame.image.load('follicle ovulates.png').convert_alpha()
follicle_ovulates_image = pygame.transform.scale(follicle_ovulates_image, (50, 50))
follicle_large_image = pygame.image.load('follicle large.png').convert_alpha()
follicle_large_image = pygame.transform.scale(follicle_large_image, (50, 50))
follicle_medium_image = pygame.image.load('follicle medium.png').convert_alpha()
follicle_medium_image = pygame.transform.scale(follicle_medium_image, (40, 40))
follicle_small_image = pygame.image.load('follicle small.png').convert_alpha()
follicle_small_image = pygame.transform.scale(follicle_small_image, (30, 30))
LH_slider_image = pygame.image.load('LH slider.png').convert_alpha()
LH_slider_image = pygame.transform.scale(LH_slider_image, (15, 15))
FSH_slider_image = pygame.image.load('FSH slider.png').convert_alpha()
FSH_slider_image = pygame.transform.scale(FSH_slider_image, (15, 15))
estrogen_slider_image = pygame.image.load('estrogen slider.png').convert_alpha()
estrogen_slider_image = pygame.transform.scale(estrogen_slider_image, (15, 15))
progesterone_slider_image = pygame.image.load('progesterone slider.png').convert_alpha()
progesterone_slider_image = pygame.transform.scale(progesterone_slider_image, (15, 15))
time_slider_image = pygame.image.load('time slider.png').convert_alpha()
time_slider_image = pygame.transform.scale(time_slider_image, (30, 30))

# Create groups
follicle_group = pygame.sprite.GroupSingle()
hormone_group = pygame.sprite.GroupSingle()
slider_group = pygame.sprite.Group()



#Not yet functional.  Hormones will function similar to projectiles in our evil clutches game.
# Create classes
class Hormone(pygame.sprite.Sprite):
    def __init__(self, image, start: tuple, end:tuple, speed, spawn_interval):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.start = start
        self.end = end
        self.t = 0
        self.speed = speed
        self.spawn_interval = spawn_interval 
        self.tolerance = 5 #had precision issues when using exact coordinates for the self.kill
        
    def update(self):
        self.t += self.speed
        if self.t >1:
            self.t = 0
        
        x = (1-self.t) * self.start[0] + self.t * self.end[0]
        y = (1-self.t)*self.start[1]+self.t*self.end[1]
        self.rect.center = (int(x), int(y))
        
        if abs(x - self.end[0]) < self.tolerance and abs(y - self.end[1]) < self.tolerance:
            self.kill()
    
'''def spawn_hormones():
    global estrogen_speed
    global estrogen_speed
    global progesterone_speed 
    global lh_speed 
    global fsh_speed 
    global LH_SPAWN_INTERVAL
    global ESTROGEN_SPAWN_INTERVAL
    global PROGESTERONE_SPAWN_INTERVAL
    global FSH_SPAWN_INTERVAL
    global lhspawn_timer
    global estrogenspawn_timer
    global progesteronespawn_timer
    global fshspawn_timer
    current_time = pygame.time.get_ticks()

    
    if len(estrogen_group) < 15 and current_time - estrogenspawn_timer > ESTROGEN_SPAWN_INTERVAL:
        new_Hormone1 = Hormone(estrogen_molecule_image, (905, 631), (871, 382), estrogen_speed, ESTROGEN_SPAWN_INTERVAL)
        estrogen_group.add(new_Hormone1)
        estrogenspawn_timer = current_time
    
    if len(lh_group) < 15 and current_time - lhspawn_timer > lh_group.sprites()[-1].spawn_interval:
        new_Hormone = Hormone(LH_molecule_image, (1044, 391), (974, 631), lh_speed, LH_SPAWN_INTERVAL)
        lh_group.add(new_Hormone)
        lhspawn_timer = current_time

    if len(progesterone_group) < 15 and current_time - progesteronespawn_timer > progesterone_group.sprites()[-1].spawn_interval: 
        new_Hormone2 = Hormone(progesterone_molecule_image, (923, 609), (883,353),.01, PROGESTERONE_SPAWN_INTERVAL)
        progesterone_group.add(new_Hormone2)
        progesteronespawn_timer = current_time
    
    if len (fsh_group) < 15 and current_time - fshspawn_timer > fsh_group.sprites()[-1].spawn_interval:
        new_Hormone3 = Hormone(FSH_molecule_image, (1021,357), (963,609),.01, FSH_SPAWN_INTERVAL)
        fsh_group.add(new_Hormone3)
        fshspawn_timer = current_time
'''

#Not yet functional.  Beginning outline for moving the follicles.  Plan to make the sliders a subclass.
class Follicle(pygame.sprite.Sprite):
    def __init__(self,image,rect):
        self.image = image
        self.rect = rect
        self.mask = pygame.mask.from_surface(image)

    #if pygame.event.type == MOUSEBUTTONDOWN:
        #if follicle.collidepoint(event.pos):
            #moving = True
        #elif event.type == MOUSEBUTTONUP:
            #moving = False
        #elif pygame.event.type == MOUSEMOTION and moving:
            #follicle.move_ip(event.rel)

class Slider(pygame.sprite.Sprite):
    def __init__(self, image, pos: tuple, size: tuple, min: int, max: int):
        super().__init__()
        self.image = image
        self.pos = pos
        self.size = size
        self.min = min
        self.max = max
        #self.initial_val = (self.max - self.min) * initial_val  # <- percentage
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            if pygame.mouse.get_pressed()[0]:
                pos = mouse_y
                if pos > self.min:
                    pos = self.min
                if pos < self.max:
                    pos = self.max
                self.rect.centery = pos




# Dimensions of the sprites
CL_LARGE_WIDTH = 30

def main():
    lhslider = Slider(LH_slider_image,(920, 425), (15,15), 425, 345)
    fhsslider = Slider(FSH_slider_image, (970,420), (15,15), 420, 340)
    eslider = Slider(estrogen_slider_image, (902,792),(15,15),792, 730)
    pslider = Slider(progesterone_slider_image, (972, 792), (15,15),792, 730)
    slider_group.add(lhslider)
    slider_group.add(fhsslider)
    slider_group.add(eslider)
    slider_group.add(pslider)

    clock = pygame.time.Clock()

    running = True
    # Main game loop
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        window.blit(backgroundimage, (backgroundimage_x, backgroundimage_y))

        slider_group.draw(window)
        slider_group.update()

        window.blit(follicle_small_image, (650, 900))
        window.blit(follicle_medium_image, (700, 900))
        window.blit(follicle_large_image, (750, 900))
        window.blit(follicle_ovulates_image, (850, 900))
        window.blit(cl_small_image, (1100, 900))
        window.blit(cl_medium_image, (1050, 900))
        window.blit(cl_large_image, (1000, 900))
        window.blit(egg_cell_image, (890, 610))
        window.blit(time_slider_image, (940, 230))
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()



