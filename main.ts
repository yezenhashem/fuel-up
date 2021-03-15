namespace SpriteKind {
    export const Gas = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
        3 3 3 3 3 3 3 3 
        3 . . . . . . 3 
        3 . 3 3 3 3 . 3 
        3 . 3 . . 3 . 3 
        3 . 3 . . 3 . 3 
        3 . 3 3 3 3 . 3 
        3 . . . . . . 3 
        3 3 3 3 3 3 3 3 
        `, mySprite, 0, -70)
    projectile.startEffect(effects.ashes)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Gas, function (sprite, otherSprite) {
    statusbar.value = 100
    otherSprite.destroy()
})
statusbars.onZero(StatusBarKind.Energy, function (status) {
    game.over(false)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy(effects.bubbles, 500)
    otherSprite.destroy(effects.smiles, 500)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy(effects.disintegrate, 500)
})
let myEnemy: Sprite = null
let myFuel: Sprite = null
let projectile: Sprite = null
let statusbar: StatusBarSprite = null
let mySprite: Sprite = null
effects.starField.startScreenEffect()
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite)
mySprite.setFlag(SpriteFlag.StayInScreen, true)
statusbar = statusbars.create(20, 4, StatusBarKind.Energy)
statusbar.attachToSprite(mySprite, -25, 0)
game.onUpdateInterval(500, function () {
    myFuel = sprites.createProjectileFromSide(img`
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
        `, 0, 50)
    myFuel.x = randint(5, 155)
    myFuel.setKind(SpriteKind.Gas)
})
game.onUpdateInterval(500, function () {
    myEnemy = sprites.createProjectileFromSide(img`
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
        `, 0, 50)
    myEnemy.x = randint(5, 155)
    myEnemy.setKind(SpriteKind.Enemy)
})
game.onUpdateInterval(300, function () {
    statusbar.value += -1
})
