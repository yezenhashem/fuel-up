@namespace
class SpriteKind:
    Gas = SpriteKind.create()

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            3 3 3 3 3 3 3 3 
                    3 . . . . . . 3 
                    3 . 3 3 3 3 . 3 
                    3 . 3 . . 3 . 3 
                    3 . 3 . . 3 . 3 
                    3 . 3 3 3 3 . 3 
                    3 . . . . . . 3 
                    3 3 3 3 3 3 3 3
        """),
        mySprite,
        0,
        -70)
    projectile.start_effect(effects.ashes)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    statusbar.value = 100
    otherSprite.destroy()
sprites.on_overlap(SpriteKind.player, SpriteKind.Gas, on_on_overlap)

def on_on_zero(status):
    game.over(False)
statusbars.on_zero(StatusBarKind.energy, on_on_zero)

def on_on_overlap2(sprite, otherSprite):
    sprite.destroy(effects.bubbles, 500)
    otherSprite.destroy(effects.smiles, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    info.change_life_by(-1)
    otherSprite.destroy(effects.disintegrate, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

myEnemy: Sprite = None
myFuel: Sprite = None
projectile: Sprite = None
statusbar: StatusBarSprite = None
mySprite: Sprite = None
effects.star_field.start_screen_effect()
mySprite = sprites.create(img("""
        . . . . . . . 9 9 . . . . . . . 
            . . . . . . 9 . . 9 . . . . . . 
            . . . . . . 9 . . 9 . . . . . . 
            . . . . . 9 . 9 9 . 9 . . . . . 
            . . . . . 9 . 9 9 . 9 . . . . . 
            . . . . 9 . 9 9 9 9 . 9 . . . . 
            . . . . 9 . 9 9 9 9 . 9 . . . . 
            . . . 9 . 9 9 9 9 9 9 . 9 . . . 
            . . . 9 . 9 . . . . 9 . 9 . . . 
            . . 9 . 9 9 . 9 9 . 9 9 . 9 . . 
            . . 9 . 9 9 . . . . 9 9 . 9 . . 
            . 9 . 9 9 9 . 9 9 9 9 9 9 . 9 . 
            . 9 . 9 9 9 . 9 9 9 9 9 9 . 9 . 
            9 . 9 9 9 9 9 9 9 9 9 9 9 9 . 9 
            9 . . . . . . . . . . . . . . 9 
            9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
statusbar = statusbars.create(20, 4, StatusBarKind.energy)
statusbar.attach_to_sprite(mySprite, -25, 0)

def on_update_interval():
    global myFuel
    myFuel = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . b b b . . . 
                    . . . . . . . . b e e 3 3 b . . 
                    . . . . . . b b e 3 2 e 3 a . . 
                    . . . . b b 3 3 e 2 2 e 3 3 a . 
                    . . b b 3 3 3 3 3 e e 3 3 3 a . 
                    b b 3 3 3 3 3 3 3 3 3 3 3 3 3 a 
                    b 3 3 3 d d d d 3 3 3 3 3 d d a 
                    b b b b b b b 3 d d d d d d 3 a 
                    b d 5 5 5 5 d b b b a a a a a a 
                    b 3 d d 5 5 5 5 5 5 5 d d d d a 
                    b 3 3 3 3 3 3 d 5 5 5 d d d d a 
                    b 3 d 5 5 5 3 3 3 3 3 3 b b b a 
                    b b b 3 d 5 5 5 5 5 5 5 d d b a 
                    . . . b b b 3 d 5 5 5 5 d d 3 a 
                    . . . . . . b b b b 3 d d d b a 
                    . . . . . . . . . . b b b a a .
        """),
        0,
        50)
    myFuel.x = randint(5, 155)
    myFuel.set_kind(SpriteKind.Gas)
game.on_update_interval(500, on_update_interval)

def on_update_interval2():
    global myEnemy
    myEnemy = sprites.create_projectile_from_side(img("""
            2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 
                    2 . . . . . . . . . . . . . . 2 
                    2 . 2 2 2 2 2 2 2 2 2 2 2 2 . 2 
                    . 2 . 2 2 2 . . . . 2 2 2 . 2 . 
                    . 2 . 2 2 2 . 2 2 2 2 2 2 . 2 . 
                    . . 2 . 2 2 . . . 2 2 2 . 2 . . 
                    . . 2 . 2 2 . 2 2 2 2 2 . 2 . . 
                    . . . 2 . 2 . . . . 2 . 2 . . . 
                    . . . 2 . 2 2 2 2 2 2 . 2 . . . 
                    . . . . 2 . 2 2 2 2 . 2 . . . . 
                    . . . . 2 . 2 2 2 2 . 2 . . . . 
                    . . . . . 2 . 2 2 . 2 . . . . . 
                    . . . . . 2 . 2 2 . 2 . . . . . 
                    . . . . . . 2 . . 2 . . . . . . 
                    . . . . . . 2 . . 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . .
        """),
        0,
        50)
    myEnemy.x = randint(5, 155)
    myEnemy.set_kind(SpriteKind.enemy)
game.on_update_interval(500, on_update_interval2)

def on_update_interval3():
    statusbar.value += -1
game.on_update_interval(300, on_update_interval3)
