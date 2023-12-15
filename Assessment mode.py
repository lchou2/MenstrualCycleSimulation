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

# Destination Coordinates
UTERUS = (1062, 585)
OVARY = (905, 600)


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

#Timers for hormone spawns
estrogenspawn_timer = pygame.time.get_ticks()
progesteronespawn_timer = pygame.time.get_ticks()
lhspawn_timer = pygame.time.get_ticks()
fshspawn_timer = pygame.time.get_ticks()

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
estrogen_molecule_image = pygame.transform.scale(estrogen_molecule_image, (10, 10))
progesterone_molecule_image = pygame.image.load('progesterone molecule.png').convert_alpha()
progesterone_molecule_image = pygame.transform.scale(progesterone_molecule_image, (10, 10))
FSH_molecule_image = pygame.image.load('FSH molecule.png').convert_alpha()
FSH_molecule_image = pygame.transform.scale(FSH_molecule_image, (10, 10))
LH_molecule_image = pygame.image.load('LH molecule.png').convert_alpha()
LH_molecule_image = pygame.transform.scale(LH_molecule_image, (10, 10))

follicle_ovulates_image = pygame.image.load('follicle ovulates.png').convert_alpha()
follicle_ovulates_image = pygame.transform.scale(follicle_ovulates_image, (50, 50))
follicle_large_image = pygame.image.load('follicle large.png').convert_alpha()
follicle_large_image = pygame.transform.scale(follicle_large_image, (50, 50))
follicle_large_image = pygame.transform.rotate(follicle_large_image, (270))
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

uterine_lining_1= pygame.image.load('uterine lining 1.png').convert_alpha()
uterine_lining_1 = pygame.transform.scale(uterine_lining_1, (73, 100))
uterine_lining_2= pygame.image.load('uterine lining 2.png').convert_alpha()
uterine_lining_2 = pygame.transform.scale(uterine_lining_2, (73, 100))
uterine_lining_3= pygame.image.load('uterine lining 3.png').convert_alpha()
uterine_lining_3 = pygame.transform.scale(uterine_lining_3, (73, 100))
uterine_lining_4= pygame.image.load('uterine lining 4.png').convert_alpha()
uterine_lining_4 = pygame.transform.scale(uterine_lining_4, (73, 100))
uterine_lining_5= pygame.image.load('uterine lining 5.png').convert_alpha()
uterine_lining_5 = pygame.transform.scale(uterine_lining_5, (73, 100))
uterine_lining_6= pygame.image.load('uterine lining 6.png').convert_alpha()
uterine_lining_6 = pygame.transform.scale(uterine_lining_6, (73, 100))

menstruation_1 = pygame.image.load('menstruation 1.png').convert_alpha()
menstruation_1 = pygame.transform.scale(menstruation_1, (70, 200))
menstruation_2 = pygame.image.load('menstruation 2.png').convert_alpha()
menstruation_2 = pygame.transform.scale(menstruation_2, (70, 200))
menstruation_3 = pygame.image.load('menstruation 3.png').convert_alpha()
menstruation_3 = pygame.transform.scale(menstruation_3, (70, 200))
menstruation_4 = pygame.image.load('menstruation 4.png').convert_alpha()
menstruation_4 = pygame.transform.scale(menstruation_4, (70, 200))
menstruation_5 = pygame.image.load('menstruation 5.png').convert_alpha()
menstruation_5 = pygame.transform.scale(menstruation_5, (70, 200))

# Create groups
follicle_group = pygame.sprite.Group()
hormone_group = pygame.sprite.GroupSingle()
slider_group = pygame.sprite.Group()
estrogen_group = pygame.sprite.Group()
lh_group = pygame.sprite.Group()
progesterone_group = pygame.sprite.Group()
fsh_group = pygame.sprite.Group()




#Not yet functional.  Hormones will function similar to projectiles in our evil clutches game.
# Create classes
class Hormone(pygame.sprite.Sprite):
    def __init__(self, image, start: tuple, end:tuple, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.start = start
        self.end = end
        self.t = 0
        self.speed = speed
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
    
def spawn_hormones(lhslider, fshslider, eslider, pslider):
    global estrogen_speed
    global lh_speed
    global fsh_speed
    global progesterone_speed
    global LH_SPAWN_INTERVAL
    global ESTROGEN_SPAWN_INTERVAL
    global PROGESTERONE_SPAWN_INTERVAL
    global FSH_SPAWN_INTERVAL
    global lhspawn_timer
    global estrogenspawn_timer
    global progesteronespawn_timer
    global fshspawn_timer
    current_time = pygame.time.get_ticks()

    lh_slider_pos = lhslider.rect.centery
    fsh_slider_pos = fshslider.rect.centery
    estrogen_slider_pos = eslider.rect.centery
    progesterone_slider_pos = pslider.rect.centery
    
    if len(estrogen_group) < 15 and current_time - estrogenspawn_timer > ESTROGEN_SPAWN_INTERVAL:
        new_Hormone1 = Hormone(estrogen_molecule_image, (905, 631), (871, 382), .01)
        estrogen_group.add(new_Hormone1)
        estrogenspawn_timer = current_time
    
    if len(lh_group) < 15 and current_time - lhspawn_timer > LH_SPAWN_INTERVAL:
        new_Hormone = Hormone(LH_molecule_image, (1044, 391), (974, 631), .01)
        lh_group.add(new_Hormone)
        lhspawn_timer = current_time

    if len(progesterone_group) < 15 and current_time - progesteronespawn_timer > PROGESTERONE_SPAWN_INTERVAL: 
        new_Hormone2 = Hormone(progesterone_molecule_image, (923, 609), (883,353), .01)
        progesterone_group.add(new_Hormone2)
        progesteronespawn_timer = current_time
    
    if len(fsh_group) < 15 and current_time - fshspawn_timer > FSH_SPAWN_INTERVAL:
        new_Hormone3 = Hormone(FSH_molecule_image, (1021,357), (963,609),.01)
        fsh_group.add(new_Hormone3)
        fshspawn_timer = current_time
    
    
    ESTROGEN_SPAWN_INTERVAL = 1100-((792-eslider.rect.centery)/65)*1000
    PROGESTERONE_SPAWN_INTERVAL = 1100-((792-pslider.rect.centery)/65)*1000
    LH_SPAWN_INTERVAL = 1100-((420-lhslider.rect.centery)/80)*1000
    FSH_SPAWN_INTERVAL = 1100-((420-fshslider.rect.centery)/80)*1000


#Not yet functional.  Beginning outline for moving the follicles.  Plan to make the sliders a subclass.
class FollicleSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos: tuple, size: tuple):
        super().__init__()  # Make sure to initialize the superclass
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(image)
        self.pos = pos
        self.size = size
        self.rect.topleft = self.pos
        self.moving = False
        self.has_moved = False


    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.moving = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.moving = False
        elif event.type == pygame.MOUSEMOTION and self.moving:
            self.rect.move_ip(event.rel)

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
    fshslider = Slider(FSH_slider_image, (970,420), (15,15), 420, 340)
    eslider = Slider(estrogen_slider_image, (902,792),(15,15),792, 730)
    pslider = Slider(progesterone_slider_image, (972, 792), (15,15),792, 730)
    slider_group.add(lhslider)
    slider_group.add(fshslider)
    slider_group.add(eslider)
    slider_group.add(pslider)
    cl_large1 = FollicleSprite(cl_large_image,(1000, 900),(30,30))
    follicle_group.add(cl_large1)
    global LH_SPAWN_INTERVAL
    global ESTROGEN_SPAWN_INTERVAL
    global PROGESTERONE_SPAWN_INTERVAL
    global FSH_SPAWN_INTERVAL

    estrogen_group.add(Hormone(estrogen_molecule_image, (905,631),(871, 382), .01))
    lh_group.add(Hormone(LH_molecule_image, (1044,391),(974,631), .01))
    progesterone_group.add(Hormone(progesterone_molecule_image, (923, 609), (883,353),.01))
    fsh_group.add(Hormone(FSH_molecule_image, (1021,357), (963,609),.01))

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
        follicle_group.draw(window)
        follicle_group.update(event)
        spawn_hormones(lhslider, fshslider, eslider, pslider)
        estrogen_group.draw(window)
        progesterone_group.draw(window)
        lh_group.draw(window)
        fsh_group.draw(window)
        estrogen_group.update()
        progesterone_group.update()
        lh_group.update()
        fsh_group.update()
        #window.blit(follicle_small_image, (650, 900))
        #window.blit(follicle_medium_image, (700, 900))
        #window.blit(follicle_large_image, (750, 900))
        #window.blit(follicle_ovulates_image, (850, 900))
        #window.blit(cl_small_image, (1100, 900))
        #window.blit(cl_medium_image, (1050, 900))
        #window.blit(cl_large_image, (1000, 900))
        #window.blit(egg_cell_image, (890, 610))
        #window.blit(time_slider_image, (940, 230))
        pygame.display.update()

    pygame.quit()



if __name__ == "__main__":
    main()



