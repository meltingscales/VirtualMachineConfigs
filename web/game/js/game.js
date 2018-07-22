var fs = require('fs')
var path = require('path')

var game = new Phaser.Game(
    500, 500,
    Phaser.AUTO,
    'phaser-example',
    {
        preload: preload,
        create: create,
        update: update,
        render: render,
    },
);

var player;
var facing = 'left';
var jumpTimer = 0;
var cursors;
var jumpButton;

function preload() {
    game.load.spritesheet('dude', 'assets/dude.png', 32, 48);
    game.load.image('stone', 'assets/stone.png');
}

function create() {
    
    game.physics.startSystem(Phaser.Physics.ARCADE);

    game.time.desiredFps = 60;

    game.physics.arcade.gravity.y = 250;

    player = game.add.sprite(32, 32, 'dude');
    game.physics.enable(player, Phaser.Physics.ARCADE);

    block = game.add.sprite(40, 400, 'stone');

    game.physics.enable(block, Phaser.Physics.ARCADE);
    block.body.allowGravity = false;
    block.body.immovable = true;
    block.body.allowDrag = false;

    player.body.bounce.y = 0.2;
    player.body.collideWorldBounds = true;
    player.body.setSize(20, 32, 5, 16);

    player.animations.add('left', [0, 1, 2, 3], 10, true);
    player.animations.add('turn', [4], 20, true);
    player.animations.add('right', [5, 6, 7, 8], 10, true);

    cursors = game.input.keyboard.createCursorKeys();
    jumpButton = game.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);

}

function collisionHandler(obj1, obj2) {

    game.debug.text("collision!", 32, 48);

}

function update() {

    // game.physics.arcade.collide(player, layer);

    game.physics.arcade.collide(player, block, collisionHandler, null, this);


    player.body.velocity.x = 0;

    if (cursors.left.isDown) {
        player.body.velocity.x = -150;

        if (facing != 'left') {
            player.animations.play('left');
            facing = 'left';
        }
    }
    else if (cursors.right.isDown) {
        player.body.velocity.x = 150;

        if (facing != 'right') {
            player.animations.play('right');
            facing = 'right';
        }
    }
    else {
        if (facing != 'idle') {
            player.animations.stop();

            if (facing == 'left') {
                player.frame = 0;
            }
            else {
                player.frame = 5;
            }

            facing = 'idle';
        }
    }

    if (jumpButton.isDown &&
        player.body.onFloor()
        && game.time.now > jumpTimer) {

        player.body.velocity.y = -250;
        jumpTimer = game.time.now + 750;
    }

}


function render() {

    game.debug.text(game.time.suggestedFps, 32, 32);

}