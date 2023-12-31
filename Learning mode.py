import pygame
import math
pygame.font.init()
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

#Hormone spawn intervals
ESTROGEN_SPAWN_INTERVAL = 1500
PROGESTERONE_SPAWN_INTERVAL = 1500
LH_SPAWN_INTERVAL = 1500
FSH_SPAWN_INTERVAL = 1500

#Timers for hormone spawns
estrogenspawn_timer = pygame.time.get_ticks()
progesteronespawn_timer = pygame.time.get_ticks()
lhspawn_timer = pygame.time.get_ticks()
fshspawn_timer = pygame.time.get_ticks()
# spawn_interval = 1000

# Creating Main Simulation Image
backgroundimage = pygame.image.load("Background image.png")
backgroundimage = pygame.transform.scale(backgroundimage, (755, 760))
backgroundimage_rect = backgroundimage.get_rect()

# Centering the image
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
estrogen_group = pygame.sprite.Group()
lh_group = pygame.sprite.Group()
progesterone_group = pygame.sprite.Group()
fsh_group = pygame.sprite.Group()

#hormone levels for hormone spawns %estrogen, %progesterone, % LH, % FSH
hormone_levels = {
    0: [0.38, 0.21, 0.26, 0.48],
    1: [0.32, 0.19, 0.32, 0.63],
    2: [0.27, 0.17, 0.32, 0.63],
    3: [0.28, 0.18, 0.32, 0.63],
    4: [0.28, 0.18, 0.32, 0.63],
    5: [0.29, 0.18, 0.32, 0.63],
    6: [0.31, 0.19, 0.32, 0.63],
    7: [0.31, 0.19, 0.32, 0.63],
    8: [0.32, 0.19, 0.32, 0.58],
    9: [0.45, 0.20, 0.32, 0.53],
    10: [0.58, 0.20, 0.32, 0.48],
    11: [0.71, 0.20, 0.32, 0.43],
    12: [0.83, 0.21, 0.63, 0.70],
    13: [0.87, 0.21, 1.00, 1.00],
    14: [0.71, 0.26, 0.63, 0.70],
    15: [0.58, 0.34, 0.42, 0.43],
    16: [0.54, 0.43, 0.40, 0.41],
    17: [0.60, 0.69, 0.38, 0.40],
    18: [0.64, 0.86, 0.36, 0.39],
    19: [0.79, 0.95, 0.35, 0.38],
    20: [0.87, 0.97, 0.34, 0.36],
    21: [0.96, 1.00, 0.33, 0.35],
    22: [0.99, 1.00, 0.32, 0.34],
    23: [1.00, 1.00, 0.31, 0.33],
    24: [0.90, 0.98, 0.29, 0.31],
    25: [0.77, 0.97, 0.28, 0.30],
    26: [0.64, 0.90, 0.27, 0.29],
    27: [0.51, 0.83, 0.26, 0.28],
    28: [0.38, 0.78, 0.25, 0.26],
    29: [0.29, 0.74, 0.24, 0.25]
}

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
    
def spawn_hormones(day):
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

    #spawns hormones and spaces them out correctly (1100 spreads them while 1000 or 1050 clumps)
    if day in hormone_levels.keys():
            ESTROGEN_SPAWN_INTERVAL = 1100-hormone_levels[day][0]*1000
            PROGESTERONE_SPAWN_INTERVAL = 1100-hormone_levels[day][1]*1000
            LH_SPAWN_INTERVAL = 1100-hormone_levels[day][2]*1000
            FSH_SPAWN_INTERVAL = 1100-hormone_levels[day][3]*1000

# Time slider dictionary of coordinates by day
# to center time_slider subtract 17 from each coordinate
time_slider = {
    0:(940, 232),
    1:(1000, 238),
    2: (1040, 245),
    3: (1093, 271),
    4: (1133, 297),
    5: (1170, 343),
    6: (1200, 384),
    7: (1222, 435),
    8: (1236, 514),
    9: (1227, 603),
    10: (1199, 677),
    11: (1161, 723),
    12: (1123, 761),
    13: (1062, 798),
    14: (1000, 818),
    15: (940, 828),
    16: (867, 814),
    17: (792, 788),
    18: (745, 752),
    19: (707, 715),
    20: (683, 681),
    21: (653, 615),
    22: (641, 545),
    23: (648, 460),
    24: (674, 391),
    25: (701, 345),
    26: (744, 298),
    27: (783, 268),
    28: (834, 244),
    29: (886, 232)
    }

# Egg dictionary of coordinates by day
egg_movement = {
    15: (890, 615),
    16: (878, 609),
    17: (868, 586),
    18: (865, 566),
    19: (890, 540),
    20: (925, 545),
    21: (957, 555),
    22: (991, 565),
    23: (1014, 570),
    24: (1051, 584),
    25: (1088, 597),
    26: (1088, 625),
    27: (1088, 645),
    28: (1088, 665),
    29: (1088, 685)
    }

# list of follicle & corpus luteum images by day
follicle_changes = {
    1: follicle_small_image,
    5: follicle_medium_image,
    10: follicle_large_image,
    15: follicle_ovulates_image,
    16: cl_large_image,
    20: cl_medium_image,
    25: cl_small_image
    }

# list of uterine lining images by day
uterine_lining_changes = {
    6: uterine_lining_1,
    9: uterine_lining_2,
    12: uterine_lining_3,
    16: uterine_lining_4,
    20: uterine_lining_5,
    24: uterine_lining_6
    }

# list of menstruation images by day
menstrual_lining_changes = {
    0: menstruation_1,
    1: menstruation_2,
    2: menstruation_3,
    3: menstruation_4,
    4: menstruation_5
    }

# captions to display in a text box by day
# explanations to display in a text box by day
captions = {
    2:"",
    3:"",
    4:"",
    5: "Follicle grows and releases estrogen.",
    9:"",
    10: "Follicle matures. High estrogen levels stimulate the brain to release LH and FSH.  Estrogen also causes the lining of uterus to thicken.",
    11:"",
    13:"",
    14: "LH and FSH peak. The mature follicle continues to keep estrogen levels high, growing the uterine lining.",
    15: "High LH and FSH levels cause ovulation. The egg cell moves from the follicle into the fallopian tube.",
    16: "The follicle becomes the corpus luteum.  The egg drifts through the fallopian tube and is fertilized if sperm are present.",
    17: "The corpus luteum releases progesterone and estrogen, which inhibits the brain and maintains the lining of the uterus.",
    20: "Progesterone and estrogen levels peak. The corpus luteum is degenerating.  The egg drifts.",
    25: "The corpus luteum shrivels until it is used up.  Progesterone and estrogen levels begin to fall. The egg drifts into the uterus.",
    27: "The unfertilized egg is in the uterus.  Estrogen and Progesterone levels fall dramatically because the corpus luteum is gone.",
    0: "The low estrogen and progesterone levels cause the uterine lining to be shed (called menstruation). The cycle begins again."
}

def main():
    global LH_SPAWN_INTERVAL
    global ESTROGEN_SPAWN_INTERVAL
    global PROGESTERONE_SPAWN_INTERVAL
    global FSH_SPAWN_INTERVAL

    estrogen_group.add(Hormone(estrogen_molecule_image, (905,631),(871, 382), .01))
    lh_group.add(Hormone(LH_molecule_image, (1044,391),(974,631), .01))
    progesterone_group.add(Hormone(progesterone_molecule_image, (923, 609), (883,353),.01))
    fsh_group.add(Hormone(FSH_molecule_image, (1021,357), (963,609),.01))

    running = True

    # Main simulation loop
    day = 0
    first_cycle = True
    follicle_image = follicle_changes[1]
    uterine_image = uterine_lining_changes[6]
    caption_text = ""

    while running:
        window.fill ((255,255,255))
        # set keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    day = day + 1
                    if day > 29:
                        day = 0
                        first_cycle = False
                if event.key == pygame.K_BACKSPACE:
                    day = day - 1
                    if day <0:
                        day = 28
            if pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                pos = mouse_x
                pos2 = mouse_y
                print(pos, pos2)

        # display background image and hormone sliders
        window.blit(backgroundimage, (backgroundimage_x, backgroundimage_y))

        # Set up the font object and draw the text box to the screen
        font = pygame.font.Font(None, 28)
        if ((first_cycle and day > 0) or (not first_cycle)) and day in captions.keys():
            caption_text = captions[day]
        caption_text_box = font.render(caption_text, False, (132,4,132))
        window.blit(caption_text_box, (250, 150))

        # display images, change them according to the day in the cycle
        if day in time_slider.keys() :
            window.blit(time_slider_image, time_slider[day])
        if day in follicle_changes.keys() :
            follicle_image = follicle_changes[day]
        if day > 0 and day <=26:
            window.blit(follicle_image, OVARY)
        if day in uterine_lining_changes.keys() :
            uterine_image = uterine_lining_changes[day]
        if day >=6:
            window.blit(uterine_image, UTERUS)
        if first_cycle == False:
            if day in menstrual_lining_changes.keys():
                window.blit(menstrual_lining_changes[day], UTERUS)
        if day in egg_movement.keys() :
            window.blit(egg_cell_image, egg_movement[day])
        if day in hormone_levels.keys():
            window.blit(estrogen_slider_image, (904, 792-65*hormone_levels[day][0]))
            window.blit(progesterone_slider_image, (972, 792-65*hormone_levels[day][1]))
            window.blit(LH_slider_image, (922, 420-80*hormone_levels[day][2]))
            window.blit(FSH_slider_image, (972, 420-80*hormone_levels[day][3]))

    # time slider circle code - too mathematical for our background image
    #    window.blit(time_slider_image, (math.sin(day/28*360)*300+940,-math.cos(day/28*360)*300+532))

        spawn_hormones(day)
        estrogen_group.draw(window)
        progesterone_group.draw(window)
        lh_group.draw(window)
        fsh_group.draw(window)
        estrogen_group.update()
        progesterone_group.update()
        lh_group.update()
        fsh_group.update()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()



