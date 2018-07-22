/// <reference path="../defs/phaser.d.ts" /> 
// world.ts

class World {
    game: Phaser.Game;
    grid: Array<Array<Block>>;

    constructor(g: Phaser.Game, width: number, height: number) {
        this.game = g;

        this.grid = [];

    }


    drawline(block: Block, x: number, y: number) {
        
    }
}