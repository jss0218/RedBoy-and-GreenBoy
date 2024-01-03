# Name and ID:
# Yafet Getachew - dxw2ds
# Jasraj Sidhu - yez9pj


# Description - Basically a Fire boy and water girl remastered, a cooperative puzzle game
# where players control two characters with opposite elemental powers fire and water.
# RedBoy is immune to fire but vulnerable to Greenfire, while GreenBoy is the opposite.
# Players navigate through the level, solving puzzles and avoiding hazards by leveraging each
# character's strengths. The goal is to collect gems and reach the exit door by working together,
# coordinating movements, and using elemental immunities strategically.

# Use of 3 Basic Features
# 1. User Input - WASD for RedBoy and Arrow Keys for GreenBoy

# 2. Game Over - Game is over if GreenBoy steps in red lava or if RedBoy steps in green lava
# or if either step in goo

# 3. Graphics/Images - Background of dungeon, walls are stone, lava is red,
# water is blue, goo is green



# List of 4 Additional Features
# 1. Two Players simultaneously - GreenBoy and RedBoy work together during the level

# 2. Sprite Animation - Both players will have multiple sprite animations for walking
# and we'll decide to see if we'll decide if we want to add animations to anything else

# 3. Collectibles - Gems they collect along the way and key to open door

# 4. Restart from Game Over - We'll make it so that the user is able to restart the level
# from the game over screen






import uvage

camera = uvage.Camera(800, 600)
background = uvage.from_image(400, 300, 'background.png')
background.scale_by(1.8)
GreenBoy_images = uvage.load_sprite_sheet('GreenBoy.png', 1, 4)
RedBoy_images = uvage.load_sprite_sheet('RedBoy.png', 1, 4)


Grass = uvage.from_image(276, 293, 'floor.png')
Grass2 = uvage.from_image(50, 293, 'floor.png')
Grass3 = uvage.from_image(163, 293, 'floor.png')
Grass4 = uvage.from_image(389, 293, 'floor.png')
Grass5 = uvage.from_image(502, 293, 'floor.png')
Grass6 = uvage.from_image(615, 293, 'floor.png')
Grass7 = uvage.from_image(643, 293, 'floor.png')
Grass.scale_by(0.12)
Grass2.scale_by(0.12)
Grass3.scale_by(0.12)
Grass4.scale_by(0.12)
Grass5.scale_by(0.12)
Grass6.scale_by(0.12)
Grass7.scale_by(0.12)

Grass8 = uvage.from_image(50, 94, 'floor.png')
Grass9 = uvage.from_image(163, 94,'floor.png')
Grass10 = uvage.from_image(276,94, 'floor.png')
Grass11 = uvage.from_image(389,94, 'floor.png')
Grass12 = uvage.from_image(443,94, 'floor.png')
Grass8.scale_by(0.12)
Grass9.scale_by(0.12)
Grass10.scale_by(0.12)
Grass11.scale_by(0.12)
Grass12.scale_by(0.12)


Grass13 = uvage.from_image(610,194, 'floor.png')
Grass14 = uvage.from_image(723,194, 'floor.png')
Grass19 = uvage.from_image(770,194, 'floor.png')
Grass15 = uvage.from_image(158,194, 'floor.png')
Grass16 = uvage.from_image(271,194, 'floor.png')
Grass17 = uvage.from_image(384,194, 'floor.png')
Grass18 = uvage.from_image(497,194, 'floor.png')
Grass13.scale_by(0.12)
Grass14.scale_by(0.12)
Grass15.scale_by(0.12)
Grass16.scale_by(0.12)
Grass17.scale_by(0.12)
Grass18.scale_by(0.12)
Grass19.scale_by(0.12)

Grass20 = uvage.from_image(780,410, 'floor.png')
Grass21 = uvage.from_image(640,498, 'floor.png')
Grass22 = uvage.from_image(449,455, 'floor.png')
Grass23 = uvage.from_image(255,495, 'floor.png')
Grass24 = uvage.from_image(130,384, 'floor.png')
Grass25 = uvage.from_image(-80,600, 'floor.png')
Grass20.scale_by(0.08)
Grass21.scale_by(0.08)
Grass22.scale_by(0.08)
Grass23.scale_by(0.08)
Grass24.scale_by(0.09)
Grass25.scale_by(0.5)


GreenOpenDoor = uvage.from_image(30, 53, 'opendoor.png')
GreenOpenDoor.scale_by(0.115)
GreenClosedDoor = uvage.from_image(30, 53, 'greencloseddoor.png')
GreenClosedDoor.scale_by(0.115)
RedOpenDoor = uvage.from_image(100, 53, 'opendoor.png')
RedOpenDoor.scale_by(0.115)
RedClosedDoor = uvage.from_image(100, 53, 'redcloseddoor.png')
RedClosedDoor.scale_by(0.115)


GreenButton = uvage.from_image(300, 288, 'GreenButton.png')
GreenButton.scale_by(0.09)
RedButton = uvage.from_image(300, 288, 'RedButton.png')
RedButton.scale_by(0.09)

GreenButton2 = uvage.from_image(770, 188, 'GreenButton.png')
GreenButton2.scale_by(0.09)
RedButton2 = uvage.from_image(770, 188, 'RedButton.png')
RedButton2.scale_by(0.09)

GreenBoy = uvage.from_image(30, 500, GreenBoy_images[1])
GreenBoy.scale_by(0.35)
RedBoy = uvage.from_image(100, 500, RedBoy_images[1])
RedBoy.scale_by(0.25)

GreenBoy_frame = 0
GreenBoy_right = False
GreenBoy_on_ground = True

RedBoy_frame = 0
RedBoy_right = True
RedBoy_on_ground = True

bluefire_images = uvage.load_sprite_sheet('BlueFire.png', 1, 4)

bluefire1 = uvage.from_image(287, 571, bluefire_images[0])
bluefire1.scale_by(0.9)
bluefire2 = uvage.from_image(430, 571, bluefire_images[0])
bluefire3 = uvage.from_image(570, 571, bluefire_images[0])
bluefire4 = uvage.from_image(690, 571, bluefire_images[0])

bluefire_frame1 = 0
bluefire_frame2 = 0
bluefire_frame3 = 0
bluefire_frame4 = 0


floors = [
    uvage.from_color(0, 590, "black", 310, 50),
    uvage.from_color(130, 390, "black", 73, 20),
    uvage.from_color(255, 498, "black", 73, 20),
    uvage.from_color(449, 457, "black", 73, 20),
    uvage.from_color(640, 500, "black", 73, 20),
    uvage.from_color(780, 412, "black", 73, 20),
    uvage.from_color(350, 300, "black", 700, 20),
    uvage.from_color(450, 200, "black", 700, 20),
    uvage.from_color(150, 100, "black", 700, 20),
]
obstacle = uvage.from_color(110, 247, "black", 20, 75)

greencoin_images = uvage.load_sprite_sheet('GreenCoin.png', 1, 4)
GreenCoin = uvage.from_image(300, 255, greencoin_images[0])
GreenCoin.scale_by(0.25)
GreenCoin2 = uvage.from_image(255, 465, greencoin_images[0])
GreenCoin2.scale_by(0.25)
GreenCoin3 = uvage.from_image(120, 163, greencoin_images[0])
GreenCoin3.scale_by(0.25)
greencoin_frame = 0
GreenPoints = 0
redcoin_images = uvage.load_sprite_sheet('RedCoin.png', 1, 5)
RedCoin = uvage.from_image(450, 418, redcoin_images[0])
RedCoin.scale_by(0.25)
RedCoin2 = uvage.from_image(770, 130, redcoin_images[0])
RedCoin2.scale_by(0.25)
RedCoin3 = uvage.from_image(130, 353, redcoin_images[0])
RedCoin3.scale_by(0.25)
redcoin_frame = 0
RedPoints = 0

game_on = False
game_lose = False
won_game = False

pressing_button1 = False
pressing_button2 = False

def drawfloors():
    x = [Grass, Grass2, Grass3, Grass4, Grass5, Grass6, Grass7, Grass8, Grass9,
         Grass10, Grass11, Grass12, Grass13, Grass14, Grass15, Grass16, Grass17, Grass18, Grass19,
         Grass20, Grass21, Grass22, Grass23, Grass24, Grass25]
    for i in x:
        camera.draw(i)

def collect():
    global GreenPoints
    global RedPoints
    if GreenBoy.touches(GreenCoin):
        GreenCoin.x = 800
        GreenCoin.y = 1000
        GreenPoints += 1
    if GreenBoy.touches(GreenCoin2):
        GreenCoin2.x = 800
        GreenCoin2.y = 1000
        GreenPoints += 1
    if GreenBoy.touches(GreenCoin3):
        GreenCoin3.x = 800
        GreenCoin3.y = 1000
        GreenPoints += 1
    if RedBoy.touches(RedCoin):
        RedCoin.x = 800
        RedCoin.y = 1000
        RedPoints += 1
    if RedBoy.touches(RedCoin2):
        RedCoin2.x = 80
        RedCoin2.y = 1000
        RedPoints += 1
    if RedBoy.touches(RedCoin3):
        RedCoin3.x = 800
        RedCoin3.y = 1000
        RedPoints += 1



    camera.draw(uvage.from_text(78, 10, "GreenBoy Points: " + str(GreenPoints), 25, 'Green', bold=True))
    camera.draw(uvage.from_text(722, 10, "RedBoy Points: " + str(RedPoints), 25, 'Red', bold=True))
def greencoin_making():
    global game_on
    global greencoin_frame
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        greencoin_frame += 0.3
        if greencoin_frame >= 4:
            greencoin_frame = 0
        GreenCoin.image = greencoin_images[int(greencoin_frame)]
        camera.draw(GreenCoin)
        GreenCoin2.image = greencoin_images[int(greencoin_frame)]
        camera.draw(GreenCoin2)
        GreenCoin3.image = greencoin_images[int(greencoin_frame)]
        camera.draw(GreenCoin3)

def redcoin_making():
    global game_on
    global redcoin_frame
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        redcoin_frame += 0.3
        if redcoin_frame >= 5:
            redcoin_frame = 0
        RedCoin.image = redcoin_images[int(redcoin_frame)]
        camera.draw(RedCoin)
        RedCoin2.image = redcoin_images[int(redcoin_frame)]
        camera.draw(RedCoin2)
        RedCoin3.image = redcoin_images[int(redcoin_frame)]
        camera.draw(RedCoin3)


def floors_making():
    for i in floors:
        camera.draw(i)
    camera.draw(obstacle)

def blue_fire():
    global game_on
    global bluefire_frame1
    global bluefire_frame2
    global bluefire_frame3
    global bluefire_frame4
    camera.draw(bluefire1)
    camera.draw(bluefire2)
    camera.draw(bluefire3)
    camera.draw(bluefire4)
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        bluefire_frame1 += 0.5
        if bluefire_frame1 >= 4:
            bluefire_frame1 = 0
        bluefire1.image = bluefire_images[int(bluefire_frame1)]

        bluefire_frame2 += 0.5
        if bluefire_frame2 >= 4:
            bluefire_frame2 = 0
        bluefire2.image = bluefire_images[int(bluefire_frame2)]

        bluefire_frame3 += 0.5
        if bluefire_frame3 >= 4:
            bluefire_frame3 = 0
        bluefire3.image = bluefire_images[int(bluefire_frame3)]

        bluefire_frame4 += 0.5
        if bluefire_frame4 >= 4:
            bluefire_frame4 = 0
        bluefire4.image = bluefire_images[int(bluefire_frame4)]


def GreenBoy_gravity():
    global game_on
    global GreenBoy_on_ground
    global GreenBoy_on_floor
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        GreenBoy.speedy += 1
        GreenBoy.move_speed()
        if GreenBoy.y > 550:
            GreenBoy.y = 550
            GreenBoy_on_ground = True
        for i in floors:
            if uvage.is_pressing('up arrow') and ((GreenBoy_on_ground) or (GreenBoy.touches(i))):
                GreenBoy.speedy = -15
                GreenBoy_on_ground = False
                GreenBoy_on_floor = False
            if i.top_touches(GreenBoy) and GreenBoy.bottom_touches(i) :
                GreenBoy.y = i.y + (i.height/2)*-1 - 30
                GreenBoy_on_ground = True
        for each in floors:
            GreenBoy.move_to_stop_overlapping(each)
            if each.bottom_touches(GreenBoy) and GreenBoy.speedy < 0:
                each.move_to_stop_overlapping(GreenBoy)


def RedBoy_gravity():
    global game_on
    global RedBoy_on_ground
    global RedBoy_on_floor
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        RedBoy.speedy += 1
        RedBoy.move_speed()
        if RedBoy.y > 550:
            RedBoy.y = 550
            RedBoy_on_ground = True
        for i in floors:
            if uvage.is_pressing('w') and ((RedBoy_on_ground) or (RedBoy.touches(i))):
                RedBoy.speedy = -15
                RedBoy_on_ground = False
                RedBoy_on_floor = False
            if i.top_touches(RedBoy) and RedBoy.bottom_touches(i) :
                RedBoy.y = i.y + (i.height/2)*-1 - 30
                RedBoy_on_ground = True
        for each in floors:
            RedBoy.move_to_stop_overlapping(each)
            if each.bottom_touches(RedBoy) and RedBoy.speedy < 0:
                each.move_to_stop_overlapping(RedBoy)
def move_GreenBoy_x():
    global game_on
    global GreenBoy_frame
    global GreenBoy_right
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        is_walking_GreenBoy = False
        if uvage.is_pressing('left arrow'):
            GreenBoy.x -= 5
            is_walking_GreenBoy = True
            if GreenBoy_right:
                GreenBoy.flip()
                GreenBoy_right = False
        if uvage.is_pressing('right arrow'):
            GreenBoy.x += 5
            is_walking_GreenBoy = True
            if not GreenBoy_right:
                GreenBoy.flip()
                GreenBoy_right = True
        if GreenBoy.x > 790:
            GreenBoy.x = 790
        if GreenBoy.x < 10:
            GreenBoy.x = 10
        if GreenBoy.y < -7:
            GreenBoy.y = -7

        if is_walking_GreenBoy:
            GreenBoy_frame += 0.3
            if GreenBoy_frame >= 4:
                GreenBoy_frame = 0
            GreenBoy.image = GreenBoy_images[int(GreenBoy_frame)]
        camera.draw(GreenBoy)



def gameover():
    global game_on
    global game_lose
    global GreenPoints
    global RedPoints
    if (GreenBoy.touches(bluefire1) or GreenBoy.touches(bluefire2) or GreenBoy.touches(bluefire3) or GreenBoy.touches(bluefire4)) or (RedBoy.touches(bluefire1) or RedBoy.touches(bluefire2) or RedBoy.touches(bluefire3) or RedBoy.touches(bluefire4)):
        game_lose = True
        game_on = False
        camera.draw(uvage.from_text(400, 150, "You Lost, Click Space to Play Again!", 50, "Red", bold=True))
        if uvage.is_pressing("space"):
            game_on = True
            GreenBoy.x = 30
            GreenBoy.y = 500
            RedBoy.x = 100
            RedBoy.y = 500
            GreenPoints = 0
            RedPoints = 0
            GreenCoin.x = 300
            GreenCoin.y = 255
            GreenCoin2.x = 255
            GreenCoin2.y = 465
            GreenCoin3.x = 120
            GreenCoin3.y = 163
            RedCoin.x = 450
            RedCoin.y = 418
            RedCoin2.x = 770
            RedCoin2.y = 130
            RedCoin3.x = 130
            RedCoin3.y = 353

def move_RedBoy_x():
    global game_on
    global RedBoy_frame
    global RedBoy_right
    if uvage.is_pressing("space"):
        game_on = True
    if game_on:
        is_walking_RedBoy = False
        if uvage.is_pressing('a'):
            RedBoy.x -= 5
            is_walking_RedBoy = True
            if RedBoy_right:
                RedBoy.flip()
                RedBoy_right = False
        if uvage.is_pressing('d'):
            RedBoy.x += 5
            is_walking_RedBoy = True
            if not RedBoy_right:
                RedBoy.flip()
                RedBoy_right = True
        if RedBoy.x > 790:
            RedBoy.x = 790
        if RedBoy.x < 10:
            RedBoy.x = 10
        if RedBoy.y < -7:
            RedBoy.y = -7
        if is_walking_RedBoy and RedBoy_on_ground:
            RedBoy_frame += 0.278
            if RedBoy_frame >= 4:
                RedBoy_frame = 0
            RedBoy.image = RedBoy_images[int(RedBoy_frame)]
        camera.draw(RedBoy)


def buttonclicker():
    global obstacle
    camera.draw(RedButton)
    camera.draw(RedButton2)
    if GreenBoy.touches(RedButton) or RedBoy.touches(RedButton):
        camera.draw(GreenButton)
        obstacle.x = 5000
    elif GreenBoy.touches(RedButton2) or RedBoy.touches(RedButton2):
        camera.draw(GreenButton2)
        obstacle.x = 5000
    else:
        obstacle.x = 110
    if GreenBoy.touches(obstacle):
        GreenBoy.move_to_stop_overlapping(obstacle)
    if RedBoy.touches(obstacle):
        RedBoy.move_to_stop_overlapping(obstacle)

def win():
    global won_game
    global game_on
    global GreenPoints
    global RedPoints
    if GreenBoy.touches(GreenClosedDoor) and GreenPoints == 3:
        camera.draw(GreenOpenDoor)
    if RedBoy.touches(RedClosedDoor) and RedPoints == 3:
        camera.draw(RedOpenDoor)
    if GreenBoy.touches(GreenClosedDoor) and RedBoy.touches(RedClosedDoor) and GreenPoints == 3 and RedPoints == 3:
        won_game = True
        game_on = False
        camera.draw(uvage.from_text(400, 150, "You Won! Click Space to Play Again", 50, "Green", bold=True))
        if uvage.is_pressing("space"):
            game_on = True
            GreenBoy.x = 30
            GreenBoy.y = 500
            RedBoy.x = 100
            RedBoy.y = 500
            camera.draw(GreenClosedDoor)
            camera.draw(RedClosedDoor)
            GreenPoints = 0
            RedPoints = 0
            GreenCoin.x = 300
            GreenCoin.y = 255
            GreenCoin2.x = 255
            GreenCoin2.y = 465
            GreenCoin3.x = 120
            GreenCoin3.y = 163
            RedCoin.x = 450
            RedCoin.y = 418
            RedCoin2.x = 770
            RedCoin2.y = 130
            RedCoin3.x = 130
            RedCoin3.y = 353



def tick():
    camera.clear('black')
    camera.draw(background)
    collect()
    camera.draw(GreenClosedDoor)
    camera.draw(RedClosedDoor)
    win()
    move_GreenBoy_x()
    GreenBoy_gravity()
    move_RedBoy_x()
    RedBoy_gravity()
    floors_making()
    drawfloors()
    buttonclicker()
    blue_fire()
    greencoin_making()
    redcoin_making()
    if not game_on and not game_lose:
        camera.draw(uvage.from_text(400, 250, "Click Space to Play!", 70, "Green", bold=True))
    gameover()
    camera.display()

uvage.timer_loop(30, tick)