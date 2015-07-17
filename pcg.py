import noise
import geometry as geo
from vector2f import *

def bruteForceVoronoi(width,height,points):
    #Initialise empty 2Darray width*height
    voronoiMap = [[0 for j in xrange(height)]for i in xrange(width)]
    for i in xrange(width):
        for j in xrange(height):
            position = Vector2f(i,j)
            #Initialise Minimum Distance, Distance
            minDistance = float("inf")
            thisDistance = 0
            minIndex = 0
            for index,node in enumerate(points):
                thisDistance = geo.getSquaredDistance(node,position)
                if thisDistance < minDistance:
                    minDistance = thisDistance
                    minIndex = index
            #Assign BiomeIndex to pixel
            voronoiMap[i][j] = minIndex
    return voronoiMap

def getBiome(height,temperature,moisture,seaLevel,mountainLevel):
    if temperature <= 64:
        if height >= mountainLevel:
            return "ICY PEAKS"
        if moisture <= 75:
            return "TUNDRA"
        return "TAIGA"
    if temperature <= 100:
        if height >= mountainLevel:
            return "MOUNTAIN"
        if moisture <=50:
            return "TAIGA"
        return "TAIGA"
    if temperature <= 192:
        if height >= mountainLevel:
            return "MOUNTAIN"
        if height >= mountainLevel/1.25:
            return "HIGHLANDS"
        if moisture <= 50:
            return "DESERT"
        if moisture <= 128:
            return "TEMPERATE GRASSLAND"
        if moisture <= 192:
            return "FOREST"
        return "SWAMP"
    if height >= mountainLevel:
        return "MOUNTAIN"
    if height >= mountainLevel/1.25:
        return "MESA"
    if moisture <= 75:
        return "DESERT"
    if moisture <= 150:
        return "SAVANNAH"
    return "TROPICAL RAINFOREST"
            
            
def determineBiomes(mapWidth,mapHeight,biomePoints,voronoiMap,heightMap,temperatureMap,moistureMap,seaLevel,mountainLevel):
    biomes = []
    biomeMap = [[0 for j in xrange(mapHeight)]for i in xrange(mapWidth)]
    for location in biomePoints:
        x = int(location.x)
        y = int(location.y)
        height = heightMap[x][y]
        if height < seaLevel:
            biomes.append("OCEAN")
        else:
            temperature = temperatureMap[x][y]
            moisture = moistureMap[x][y]
            biome = getBiome(height,temperature,moisture,seaLevel,mountainLevel)
            biomes.append(biome)
    for i in xrange(mapWidth):
        for j in xrange(mapHeight):
            biomeMap[i][j] = biomes[voronoiMap[i][j]]
    return biomeMap
    
def generateMap(mapwidth,mapheight,nBiomes,heightMapArgs,interpolationMethod,seaLevel,mountainLevel,biomeSeed,heightSeed,tempSeed,moisSeed):
    #Generate Biome Locations
    biomePoints = noise.getRandomPoints(nBiomes,mapwidth,mapheight,biomeSeed)
    print "Sites Determined"
    #Compute voronoi-map
    voronoiMap = bruteForceVoronoi(mapwidth,mapheight,biomePoints)
    print "Voronoi-Map Computed"
    #Generate heightMap
    #heightMapArgs (startfrequency,lacunarity,persistence,octaves)
    heightMap = noise.fractionalBrownianMotion(mapwidth,mapheight,interpolationMethod,heightSeed,*heightMapArgs)
    print "Generated Height-map"
    #Generate temperatureMap
    temperatureMap = noise.perlinMap(mapwidth,mapheight,16.0,interpolationMethod,tempSeed)
    print "Generated TemperatureMap"
    #Generate moistureMap
    moistureMap = noise.perlinMap(mapwidth,mapheight,16.0,interpolationMethod,moisSeed)
    print "Generated MoistureMap"
    #Determine Biomes
    biomes = determineBiomes(mapwidth,mapheight,biomePoints,voronoiMap,heightMap,temperatureMap,moistureMap,seaLevel,mountainLevel)
    print "Determined Biomes"
    return biomes
