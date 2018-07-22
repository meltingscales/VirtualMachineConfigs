declare function require(name:string);

var fs = require('fs')
var path = require('path')
var yaml = require('js-yaml');

var controls = yaml.safeLoad(fs.readFileSync('data/controls.yml', 'utf8'));

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
var block;
var facing = 'left';
var BUTTON_JUMP;
var BUTTON_LEFT;
var BUTTON_RIGHT;
var BUTTON_UP;
var BUTTON_DOWN;

function preload() {
    game.load.spritesheet('dude', 'assets/dude.png', 32, 48);
    game.load.image('stone', 'assets/stone.png');
}

function create() {

    game.world.setBounds(0, 0, 500, 500)
    game.physics.startSystem(Phaser.Physics.ARCADE);
    game.time.desiredFps = 60;
    game.physics.arcade.gravity.y = 250;

    player = game.add.sprite(game.world.bounds.width - 100, game.world.bounds.height - 200, 'dude');
    game.physics.enable(player, Phaser.Physics.ARCADE);
    game.camera.follow(player);

    block = game.add.sprite(game.world.bounds.width - 100, game.world.bounds.height - 75, 'stone');

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

    BUTTON_JUMP = game.input.keyboard.addKey(Phaser.Keyboard[controls['JUMP']]);

    BUTTON_LEFT = game.input.keyboard.addKey(Phaser.Keyboard[controls['LEFT']]);
    BUTTON_RIGHT = game.input.keyboard.addKey(Phaser.Keyboard[controls['RIGHT']]);
    BUTTON_UP = game.input.keyboard.addKey(Phaser.Keyboard[controls['UP']]);
    BUTTON_DOWN = game.input.keyboard.addKey(Phaser.Keyboard[controls['DOWN']]);

}

function collisionHandler(obj1, obj2) {

    game.debug.text("collision!", 32, 48);

}

function update() {

    // game.physics.arcade.collide(player, layer);

    game.physics.arcade.collide(player, block, collisionHandler, null, this);


    player.body.velocity.x = 0;

    if (BUTTON_LEFT.isDown) {
        player.body.velocity.x = -150;

        if (facing != 'left') {
            player.animations.play('left');
            facing = 'left';
        }
    }
    else if (BUTTON_RIGHT.isDown) {
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

    if (BUTTON_JUMP.isDown &&
        (player.body.onFloor() || player.body.touching.down)) {

        player.body.velocity.y = -250;
    }

}


function render() {

    game.debug.text(game.time.suggestedFps.toString(), 32, 32);

}