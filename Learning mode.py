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

# Speeds of sprites
estrogen_speed = 0.01  # Set the speed for estrogen group
progesterone_speed = 0.01  # Set the speed for progesterone group
lh_speed = 0.01  # Set the speed for LH group
fsh_speed = 0.01  # Set the speed for FSH group

ANIMATION_INTERVAL = 200
ESTROGEN_SPAWN_INTERVAL = 150
PROGESTERONE_SPAWN_INTERVAL = 150
LH_SPAWN_INTERVAL = 150
FSH_SPAWN_INTERVAL = 150

#Timers for hormone spawns
spawn_timer = pygame.time.get_ticks()
spawn_interval = 1000 

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
pituitary_group = pygame.sprite.Group()
slider_group = pygame.sprite.Group()

# Not yet functional.  Hormones will function similar to projectiles in our evil clutches game.
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
    
def spawn_hormones():
    global spawn_timer
    global estrogen_speed
    global estrogen_speed
    global progesterone_speed 
    global lh_speed 
    global fsh_speed 
    current_time = pygame.time.get_ticks()
    
 

    
    if len(estrogen_group) < 15 and current_time - spawn_timer > spawn_interval:
        new_Hormone = Hormone(LH_molecule_image, (1044, 391), (974, 631), lh_speed)
        new_Hormone1 = Hormone(estrogen_molecule_image, (905, 631), (871, 382), estrogen_speed)
        new_Hormone2 = Hormone(progesterone_molecule_image, (923, 609), (883, 353), progesterone_speed)
        new_Hormone3 = Hormone(FSH_molecule_image, (1021, 357), (963, 609), fsh_speed)
        
        lh_group.add(new_Hormone)
        estrogen_group.add(new_Hormone1)
        progesterone_group.add(new_Hormone2)
        fsh_group.add(new_Hormone3)
        
        spawn_timer = current_time
# Not yet functional.  Beginning outline for moving the follicles.  Plan to make the sliders a subclass.
class Follicle(pygame.sprite.Sprite):
    def __init__(self,image,rect):
        super().__init__()
        self.image = image
        self.rect = rect
        self.mask = pygame.mask.from_surface(image)

    #if pygame.event.type == MOUSEBUTTONDOWN:
        #if follicle.collidepoint(event.pos):
            # moving = True
        #elif event.type == MOUSEBUTTONUP:
            #moving = False
        #elif pygame.event.type == MOUSEMOTION and moving:
            #follicle.move_ip(event.rel)

class Slider(pygame.sprite.Sprite):
    def __init__(self, image, pos: tuple, size: tuple, initial_val: float, min: int, max: int):
        super().__init__()
        self.image = image
        self.pos = pos
        self.size = size
        self.min = min
        self.max = max
        self.initial_val = (self.max - self.min) * initial_val  # <- percentage
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


#hormone levels for speed variables
hormone_levels = {
    0: [0.0038, 0.0021, 0.0026, 0.0048],
    1: [0.0032, 0.0019, 0.0032, 0.0063],
    2: [0.0027, 0.0017, 0.0032, 0.0063],
    3: [0.0028, 0.0018, 0.0032, 0.0063],
    4: [0.0028, 0.0018, 0.0032, 0.0063],
    5: [0.0029, 0.0018, 0.0032, 0.0063],
    6: [0.0031, 0.0019, 0.0032, 0.0063],
    7: [0.0031, 0.0019, 0.0032, 0.0063],
    8: [0.0032, 0.0019, 0.0032, 0.0058],
    9: [0.0045, 0.0020, 0.0032, 0.0053],
    10: [0.0058, 0.0020, 0.0032, 0.0048],
    11: [0.0071, 0.0020, 0.0032, 0.0043],
    12: [0.0083, 0.0021, 0.0063, 0.0070],
    13: [0.0087, 0.0021, 0.0100, 0.0100],
    14: [0.0071, 0.0026, 0.0063, 0.0070],
    15: [0.0058, 0.0034, 0.0042, 0.0043],
    16: [0.0054, 0.0043, 0.0040, 0.0041],
    17: [0.0060, 0.0069, 0.0038, 0.0040],
    18: [0.0064, 0.0086, 0.0036, 0.0039],
    19: [0.0079, 0.0095, 0.0035, 0.0038],
    20: [0.0087, 0.0097, 0.0034, 0.0036],
    21: [0.0096, 0.0100, 0.0033, 0.0035],
    22: [0.0099, 0.0100, 0.0032, 0.0034],
    23: [0.0100, 0.0100, 0.0031, 0.0033],
    24: [0.0090, 0.0098, 0.0029, 0.0031],
    25: [0.0077, 0.0097, 0.0028, 0.0030],
    26: [0.0064, 0.0090, 0.0027, 0.0029],
    27: [0.0051, 0.0083, 0.0026, 0.0028],
    28: [0.0038, 0.0078, 0.0025, 0.0026],
    29: [0.0029, 0.0074, 0.0024, 0.0025]
}


# captions to display in a text box by day

slider_location = {
    0: [394.6, 403.2, 775.88, 762.24],
    1: [399.4, 405.02, 772.16, 752.94],
    2: [403.4, 406.4, 772.16, 752.94],
    3: [402.6, 405.92, 772.16, 752.94],
    4: [402.6, 405.92, 772.16, 752.94],
    5: [401.8, 405.92, 772.16, 752.94],
    6: [400.2, 404.8, 772.16, 752.94],
    7: [400.2, 404.8, 772.16, 752.94],
    8: [399.4, 404.8, 772.16, 756.04],
    9: [389.0, 404.0, 772.16, 759.14],
    10: [378.6, 404.0, 772.16, 762.24],
    11: [368.2, 404.0, 772.16, 765.34],
    12: [358.6, 403.52, 752.94, 748.6],
    13: [355.4, 403.52, 730.0, 730.0],
    14: [368.2, 399.2, 752.94, 748.6],
    15: [378.6, 392.8, 765.96, 765.34],
    16: [381.8, 386.08, 767.2, 766.58],
    17: [377.0, 366.32, 768.44, 767.2],
    18: [373.8, 352.48, 769.68, 767.82],
    19: [361.8, 345.6, 770.3, 768.44],
    20: [355.4, 342.4, 770.92, 769.68],
    21: [348.2, 340.0, 771.54, 770.3],
    22: [345.8, 340.0, 772.16, 770.12],
    23: [345.0, 340.0, 772.78, 770.74],
    24: [353.0, 341.6, 773.92, 771.78],
    25: [363.4, 342.4, 774.64, 772.4],
    26: [373.8, 348.0, 775.28, 772.94],
    27: [384.2, 355.36, 775.88, 773.64],
    28: [394.6, 357.6, 776.5, 774.88],
    29: [401.8, 360.8, 777.12, 775.5]
}
# explanations to display in a text box by day
captions = {
    5: "Follicle grows and releases estrogen.",
    10: "Follicle matures. High estrogen levels stimulate the brain to release LH and FSH.  Estrogen also causes the lining of uterus to thicken.",
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
    global estrogen_speed
    global progesterone_speed
    global lh_speed
    global fsh_speed

    estrogen_group.add(Hormone(estrogen_molecule_image, (905,631),(871, 382), .01))
    lh_group.add(Hormone(LH_molecule_image, (1044,391),(974,631), .01))
    progesterone_group.add(Hormone(progesterone_molecule_image, (923, 609), (883,353),.01))
    fsh_group.add(Hormone(FSH_molecule_image, (1021,357), (963,609),.01))

    running = True

    # Main game loop
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
        if day in slider_location.keys() :
            window.blit(progesterone_slider_image, (972, slider_location[day][3]))
            window.blit(LH_slider_image, (920, slider_location[day][0]))
            window.blit(FSH_slider_image, (972, slider_location[day][1]))
            window.blit(estrogen_slider_image, (902, slider_location[day][2]))
        if day in hormone_levels.keys():
            estrogen_speed = hormone_levels[day][0]
            progesterone_speed = hormone_levels[day][1]
            lh_speed = hormone_levels[day][2]
            fsh_speed = hormone_levels[day][3]


    # time slider circle code - too mathematical for our background image
    #    window.blit(time_slider_image, (math.sin(day/28*360)*300+940,-math.cos(day/28*360)*300+532))

        slider_group.draw(window)
        slider_group.update()
        spawn_hormones()
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



