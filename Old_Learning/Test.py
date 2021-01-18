import pygame
import TileMap

tiles = [
            [GRASS, COAL, DIRT, GRASS, DIRT, DIRT],
            [WATER, WATER, GRASS, GRASS, WATER, DIRT],
            [COAL, GRASS, WATER, WATER, WATER, DIRT],
            [GRASS, WATER, DIRT, GRASS, WATER, DIRT],
            [COAL, GRASS, WATER, WATER, WATER, DIRT],
            [GRASS, WATER, DIRT, GRASS, WATER, GRASS],
            [GRASS, WATER, DIRT, GRASS, WATER, GRASS]
        ] 

map = TileMap.Map()
tilemap = map.loadMap(tiles)

print(tilemap)