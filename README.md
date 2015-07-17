# Python-Perlin-Based-Terrain
Generates bitmap terrain using perlin noise and voronoi regions.


INSTALLATION:
	Prerequisites - 
		Python 2.7 32bit
		Python Imaging Library (PIL)
	Extract "Terrain Generator.zip" to your preferred loccation (Hard Drive or Solid State Storage reccommended)
	The PIL can be installed by moving the folder named "PIL" to "<location of pyton installation>/Lib/site-packages/"
	
PROGRAM USAGE:
	To start the program - open the file "tkui.py" in the Python interpreter
	
	Enter desired settings, Or click the "Defaults" button in the UI then click the "Show Map" button to generate and view the map.
		The program will appear unresponsive while the map generates - do not close it.
	Click the "Save Map" button to open a save-dialogue to save the map image.

PROGRAM OPTIONS:
	Option: INPUT TYPE range : explaination : Implication

	Detail-Level: INTEGER 1<=value<=4096 : Amount of Biome-areas : High perfomance cost, High quality effect.
	Width,Height: INTEGER 1<=value<=1024 : Resolution of Map Image: High performance cost, High quality effect, diminishing returns after 512x512.
	Elevation Base-Frequency: REAL NUMBER 0<Value<=2048 : Detail of map-elevation : No performance cost, Affects variety of elevation
	Octaves: INTEGER 1<=value<=8 : Number of Increments of elevation-level generation : Large performance cost; low effect on quality. Affects variation of elevation.
	Lacunarity: REAL NUMBER 0<value<16: The factor which detail increases on each increment of elevation-level generation : No effect on performance. Affects variation of elevation.
	Persistence: REAL NUMBER 0<value<16: The factor which each increment's of elevation-generation's effect increases: No effect on performance : Affects how noticible elevation-detail is.
	Mountain-Level: INTEGER 0<=value<=255 : The level at which a biome is a mountain : Affects amount of "MOUNTAIN","ICY PEAKS", "HIGHLANDS" and "MESA" biomes.
	Sea-Level: INTEGER 0<=value<=255 : The level at which a biome is land. : Affects amound of land/ocean.
	
	Interpolation Mode: LINEAR,COSINE or HERMITE : Sets the interpolation method : More noticible effect at higher detail levels. Linear is faster than cosine which is faster than hermite.
	
	Biome Seed:          |
	HeightMap Seed      |
	TemperatureMap Seed |
	MoistureMap Seed    |: See Seeds info;  REAL NUMBER -65535<=value<=65535

SEEDS INFO:
	The seeds effect the program's random number generator results.
	Entering the same seeds with the same map settings will generate the same map.
	
	The biome seed affects the placement of the biome sites.
	The heightMap seed affects the elevation levels on the map.
	The temperatureMap seed affects the temperatures on the map.
	The moistureMap seed affects the moisture-levels on the map.

BIOMES:
	See BiomeLegend.html

TROUBLESHOOTING INFO:
	If there is an error upon clicking "Show Map", check that your input values for Lacunarity, Persistence, octaves, mountain level, sea level, interpolation mode, biome seed, heightmap seed, temperatureMap seed and moistureMap seed are valid.
	The program will become unresponsive when teh map is being generated, and may stay that way for a very long time for higher Width,Height, Octaves and Detail Levels; you just have to wait for the image to generate.
	When saving an image, make sure not to type a file extension otehr than .bmp in the image name (only .bmp is supported)
