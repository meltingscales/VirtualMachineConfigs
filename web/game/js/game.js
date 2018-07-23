var fs = require('fs');
var path = require('path');
var yaml = require('js-yaml');
var block;
var SimpleGame = /** @class */ (function () {
    function SimpleGame() {
        this.game = new Phaser.Game(500, 500, Phaser.AUTO, 'phaser-example', {
            preload: this.preload,
            create: this.create,
            update: this.update,
            render: this.render,
        });
    }
    SimpleGame.prototype.preload = function () {
        this.game.load.spritesheet('dude', 'assets/dude.png', 32, 48);
        this.game.load.image('stone', 'assets/stone.png');
        this.controls = yaml.safeLoad(fs.readFileSync('data/controls.yml', 'utf8'));
        this.buttons = {};
        console.log(this.controls);
        this.buttons['JUMP'] = this.game.input.keyboard.addKey(Phaser.KeyCode[this.controls['JUMP']]);
        this.buttons['LEFT'] = this.game.input.keyboard.addKey(Phaser.KeyCode[this.controls['LEFT']]);
        this.buttons['RIGHT'] = this.game.input.keyboard.addKey(Phaser.KeyCode[this.controls['RIGHT']]);
        this.buttons['UP'] = this.game.input.keyboard.addKey(Phaser.KeyCode[this.controls['UP']]);
        this.buttons['DOWN'] = this.game.input.keyboard.addKey(Phaser.KeyCode[this.controls['DOWN']]);
    };
    SimpleGame.prototype.create = function () {
        this.game.world.setBounds(0, 0, 500, 500);
        this.game.physics.startSystem(Phaser.Physics.ARCADE);
        this.game.time.desiredFps = 60;
        this.game.physics.arcade.gravity.y = 250;
        this.player = this.game.add.sprite(this.game.world.bounds.width - 100, this.game.world.bounds.height - 200, 'dude');
        this.game.physics.enable(this.player, Phaser.Physics.ARCADE);
        this.game.camera.follow(this.player);
        block = this.game.add.sprite(this.game.world.bounds.width - 100, this.game.world.bounds.height - 75, 'stone');
        this.game.physics.enable(block, Phaser.Physics.ARCADE);
        block.body.allowGravity = false;
        block.body.immovable = true;
        block.body.allowDrag = false;
        this.player.body.bounce.y = 0.2;
        this.player.body.collideWorldBounds = true;
        this.player.body.setSize(20, 32, 5, 16);
        this.player.animations.add('left', [0, 1, 2, 3], 10, true);
        this.player.animations.add('turn', [4], 20, true);
        this.player.animations.add('right', [5, 6, 7, 8], 10, true);
    };
    SimpleGame.prototype.collisionHandler = function (obj1, obj2) {
        console.log(obj1);
        console.log(obj2);
    };
    SimpleGame.prototype.render = function () {
        this.game.debug.text(this.game.time.suggestedFps.toString(), 32, 32);
    };
    SimpleGame.prototype.update = function () {
        // game.physics.arcade.collide(player, layer);
        var _this = this;
        this.game.physics.arcade.collide(this.player, block, function (o1, o2) {
            _this.game.debug.text("collision!", 32, 48);
        }, null, this);
        this.player.body.velocity.x = 0;
        if (this.buttons['LEFT'].isDown) {
            this.player.body.velocity.x = -150;
            if (this.facing != 'left') {
                this.player.animations.play('left');
                this.facing = 'left';
            }
        }
        else if (this.buttons['RIGHT'].isDown) {
            this.player.body.velocity.x = 150;
            if (this.facing != 'right') {
                this.player.animations.play('right');
                this.facing = 'right';
            }
        }
        else {
            if (this.facing != 'idle') {
                this.player.animations.stop();
                if (this.facing == 'left') {
                    this.player.frame = 0;
                }
                else {
                    this.player.frame = 5;
                }
                this.facing = 'idle';
            }
        }
        if (this.buttons['JUMP'].isDown &&
            (this.player.body.onFloor() || this.player.body.touching.down)) {
            this.player.body.velocity.y = -250;
        }
    };
    return SimpleGame;
}());
var game = new SimpleGame();
