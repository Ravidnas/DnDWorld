from PIL import Image, ImageTk
from random import randrange


import Map_Build

MapAtt= Map_Build.MapAttributes
water =  0, 0, 255, 255
grass = 0, 255, 0, 255
brown = 218, 165, 32, 255
forest = 0, 100, 0, 255
rock =   169, 169, 169, 255

def build():
    map_im = Image.new("RGBA", (int(MapAtt.Xsize), int(MapAtt.Ysize)), color=(0, 255, 0, 255))
    Map = map_im.load()
    amountWater = (int(MapAtt.AmountWater)/100)*MapAtt.TotalPixels
    amountDirt = (int(MapAtt.AmountDirt)/100)*MapAtt.TotalPixels
    amountForest = (int(MapAtt.AmountForest)/100)*MapAtt.TotalPixels
    amountRock = (int(MapAtt.AmountRock)/100)*MapAtt.TotalPixels
    LakeBuild(amountDirt, MapAtt.NumOfDeserts, Map, brown)
    LakeBuild(amountForest, MapAtt.NumOfForests, Map, forest)
    LakeBuild(amountWater, MapAtt.NumOfLakes, Map, water)
    LakeBuild(amountRock, MapAtt.NumOfRocks, Map, rock)

    '''
    amountDirt = (int(MapAtt.AmountDirt)/100)*MapAtt.TotalPixels
    DirtBuild(amountDirt, int(MapAtt.NumOfDeserts), Map)

    for y in (0, int(MapAtt.Ysize)-1):
        for x in (0, int(MapAtt.Xsize)-1):
            print(Map[x,y])
'''
    map_im.save("Map.bmp")

    #Map[int(MapAtt.Xsize)/2,int(MapAtt.Ysize)/2] = 0, 0, 255

def LakeBuild(AmountWater, NumOfLakes, Map, Color):

    for y in range(0, NumOfLakes):
        if y < NumOfLakes -1 < AmountWater:
            LakeSize = int(AmountWater)/(randrange(1, NumOfLakes))
            AmountWater = AmountWater - LakeSize
        else:
            LakeSize = AmountWater

        #Picks Random Spot on map
        wy = randrange(0, int(MapAtt.Ysize) - 1)
        wx = randrange(0, int(MapAtt.Xsize) - 1)

        while Map[wx, wy] == Color:
            wy = randrange(0, int(MapAtt.Ysize) - 1)
            wx = randrange(0, int(MapAtt.Xsize) - 1)

        #List of SPOTS on the map that can be turned to Color
        PotentialLake = []

        for x in range(0, int(LakeSize)):
            #Set spot i'm at = to Color
            Map[wx, wy] = Color
            #Do I need to delete from list?

            #confirmed working? Probably, Checks for edge cases, and how to deal with them. and adds more to list
            if   (wx + 1 < int(MapAtt.Xsize)) and (wy + 1 < int(MapAtt.Ysize)) and (wy - 1 >= 0) and (wx - 1 >= 0):
                if (Map[wx - 1, wy - 1] != Color):
                    PotentialLake.append([wx - 1, wy-1])
                if (Map[wx - 1, wy ] != Color):
                    PotentialLake.append([wx - 1, wy])
                if (Map[wx - 1, wy + 1] != Color):
                    PotentialLake.append([wx - 1, wy + 1])
                if (Map[wx, wy - 1] != Color):
                    PotentialLake.append([wx, wy-1])
                if (Map[wx, wy + 1] != Color):
                    PotentialLake.append([wx, wy + 1])
                if (Map[wx + 1, wy - 1] != Color):
                    PotentialLake.append([wx + 1, wy - 1])
                if (Map[wx + 1, wy ] != Color):
                    PotentialLake.append([wx + 1, wy])
                if (Map[wx + 1, wy + 1] != Color):
                    PotentialLake.append([wx + 1, wy + 1])
            elif (wx + 1 >= int(MapAtt.Xsize)) and (wy + 1 < int(MapAtt.Ysize)) and (wy - 1 >= 0):
                if (Map[wx - 1, wy - 1] != Color):
                    PotentialLake.append([wx - 1, wy - 1])
                if (Map[wx - 1, wy] != Color):
                    PotentialLake.append([wx - 1, wy])
                if (Map[wx - 1, wy + 1] != Color):
                    PotentialLake.append([wx - 1, wy + 1])
                if (Map[wx, wy - 1] != Color):
                    PotentialLake.append([wx, wy - 1])
                if (Map[wx, wy + 1] != Color):
                    PotentialLake.append([wx, wy + 1])
            elif (wx - 1 < 0) and (wy + 1 < int(MapAtt.Ysize)) and (wy - 1 >= 0):
                if (Map[wx, wy - 1] != Color):
                    PotentialLake.append([wx, wy-1])
                if (Map[wx, wy + 1] != Color):
                    PotentialLake.append([wx, wy + 1])
                if (Map[wx + 1, wy - 1] != Color):
                    PotentialLake.append([wx + 1, wy - 1])
                if (Map[wx + 1, wy ] != Color):
                    PotentialLake.append([wx + 1, wy])
                if (Map[wx + 1, wy + 1] != Color):
                    PotentialLake.append([wx + 1, wy + 1])
            elif (wy + 1 >= int(MapAtt.Ysize)) and (wx + 1 < int(MapAtt.Xsize)) and (wx - 1 >= 0):
                if (Map[wx - 1, wy - 1] != Color):
                    PotentialLake.append([wx - 1, wy - 1])
                if (Map[wx, wy - 1] != Color):
                    PotentialLake.append([wx, wy - 1])
                if (Map[wx + 1, wy - 1] != Color):
                    PotentialLake.append([wx + 1, wy - 1])
                if (Map[wx - 1, wy] != Color):
                    PotentialLake.append([wx - 1, wy])
                if (Map[wx + 1, wy] != Color):
                    PotentialLake.append([wx + 1, wy])
            elif (wy - 1 < 0) and (wx + 1 < int(MapAtt.Xsize)) and (wx - 1 >= 0):
                if (Map[wx - 1, wy] != Color):
                    PotentialLake.append([wx - 1, wy])
                if (Map[wx + 1, wy ] != Color):
                    PotentialLake.append([wx + 1, wy])
                if (Map[wx - 1, wy + 1] != Color):
                    PotentialLake.append([wx - 1, wy + 1])
                if (Map[wx, wy + 1] != Color):
                    PotentialLake.append([wx, wy + 1])
                if (Map[wx + 1, wy + 1 ] != Color):
                    PotentialLake.append([wx + 1, wy + 1])
            elif (wx - 1 < 0) and (wy - 1 < 0):
                if (Map[wx, wy + 1] != Color):
                    PotentialLake.append([wx, wy + 1])
                if (Map[wx + 1, wy] != Color):
                    PotentialLake.append([wx + 1, wy])
                if (Map[wx + 1, wy + 1] != Color):
                    PotentialLake.append([wx + 1, wy + 1])
            elif (wx - 1 < 0) and (wy + 1 >= int(MapAtt.Ysize)):
                if (Map[wx, wy - 1] != Color):
                    PotentialLake.append([wx, wy - 1])
                if (Map[wx + 1, wy - 1] != Color):
                    PotentialLake.append([wx + 1, wy - 1])
                if (Map[wx + 1, wy ] != Color):
                    PotentialLake.append([wx + 1, wy])
            elif (wx + 1 >= int(MapAtt.Xsize)) and (wy - 1 < 0):
                if (Map[wx - 1, wy] != Color):
                    PotentialLake.append([wx - 1, wy ])
                if (Map[wx - 1, wy + 1] != Color):
                    PotentialLake.append([wx - 1 , wy + 1 ])
                if (Map[wx, wy + 1 ] != Color):
                    PotentialLake.append([wx , wy + 1])
            elif (wx + 1 >= int(MapAtt.Xsize)) and (wy + 1 >= int(MapAtt.Ysize)):
                if (Map[wx - 1, wy - 1] != Color):
                    PotentialLake.append([wx - 1, wy - 1])
                if (Map[wx - 1, wy] != Color):
                    PotentialLake.append([wx - 1, wy])
                if (Map[wx, wy - 1] != Color):
                    PotentialLake.append([wx, wy - 1])

            #While our spot is equal to Color keep picking a new spot
            while Map[wx, wy] == Color:

                while len(PotentialLake) == 0:
                    wy = randrange(0, int(MapAtt.Ysize) - 1)
                    wx = randrange(0, int(MapAtt.Xsize) - 1)
                    PotentialLake.append([wx, wy])

                next = randrange(0, len(PotentialLake))
                XY = PotentialLake[int(next)]
                #XY[0] is the X coordinate newly picked
                wx = XY[0]
                #XY[1] is the Y coordinate newly picked
                wy = XY[1]

                del PotentialLake[next]

            if len(PotentialLake) > int(LakeSize)/4:
                PotentialLake = PotentialLake[0::2]
                PotentialLake = [(wx, wy)]

def DirtBuild(AmountDirt, NumOfDeserts, Map):
    #How many deserts? check that for loop iteration if problems ensue
    for z in range(0, NumOfDeserts):
        amountDirt = AmountDirt/(randrange(2, 8))
        AmountDirt = AmountDirt - amountDirt
        dx1 = randrange(0, int(MapAtt.Xsize) - 1)
        dy1 = randrange(0, int(MapAtt.Ysize) - 1)
        dx2 = randrange(0, int(MapAtt.Xsize) - 1)
        dy2 = randrange(0, int(MapAtt.Ysize) - 1)
        if dx1 > dx2:
            dxt = dx1
            dx1 = dx2
            dx2 = dxt
        if dy1 > dy2:
            dyt = dy1
            dy1 = dy2
            dy2 = dyt

        DList = []

        while dx2 > dx1 or dy2 > dy1:
            DList.append([dx1, dy1])
            DList.append([dx2, dy2])
            if dx1 + 1 < int(MapAtt.Xsize):
                dx1 = dx1 + 1
            if dy1 + 1 < int(MapAtt.Ysize):
                dy1 = dy1 + 1
            if dx2 - 1 >= 0:
                dx2 = dx2 - 1
            if dy2 - 1 >= 0:
                dy2 = dy2 - 1
            if   (dx1 + 1 < int(MapAtt.Xsize)) and \
                    (dy1 + 1 < int(MapAtt.Ysize)) and\
                    (dy1 - 1 >= 0) and \
                    (dx1 - 1 >= 0) and \
                    (dx2 + 1 < int(MapAtt.Xsize)) and \
                    (dy2 + 1 < int(MapAtt.Ysize)) and\
                    (dy2 - 1 >= 0) and \
                    (dx2 - 1 >= 0):
                    DList.append([dx1 - 1, dy1-1])
                    DList.append([dx1 - 1, dy1])
                    DList.append([dx1 - 1, dy1 + 1])
                    DList.append([dx1, dy1-1])
                    DList.append([dx1, dy1 + 1])
                    DList.append([dx1 + 1, dy1 - 1])
                    DList.append([dx1 + 1, dy1])
                    DList.append([dx1 + 1, dy1 + 1])
                    DList.append([dx2 - 1, dy2 - 1])
                    DList.append([dx2 - 1, dy2])
                    DList.append([dx2 - 1, dy2 + 1])
                    DList.append([dx2, dy2 - 1])
                    DList.append([dx2, dy2 + 1])
                    DList.append([dx2 + 1, dy2 - 1])
                    DList.append([dx2 + 1, dy2])
                    DList.append([dx2 + 1, dy2 + 1])

        for x in range(0, len(DList)):
            Spot = DList[x]
            Map[Spot[0],Spot[1]] = brown




"""
    wy = randrange(0, int(MapAtt.Ysize) - 1)
    wx = randrange(0, int(MapAtt.Xsize) - 1)
#Make a Lake Start of attempt
    JustMoved = True
    for x in range(0, int(AmountWater)):
        Map[wx, wy] = Color
        #amountWater = amountWater - 1
        if JustMoved and wy+1 < int(MapAtt.Ysize) and Map[wx, wy+1] != Color:
            wy = wy + 1
            Map[wx, wy] = Color
            JustMoved = False
        if wx+1 < int(MapAtt.Xsize) and wy - 1 >= 0\
                and Map[wx, wy - 1] == Color and Map[wx + 1, wy] == green:
            wx = wx+1
        elif wx - 1 >= 0 and wy-1 >= 0\
                and Map[wx, wy - 1] == green and Map[wx - 1, wy] == Color :
            wy = wy-1
        elif wx - 1 >= 0 and wy+1 < int(MapAtt.Ysize)\
                and Map[wx - 1, wy] == green and Map[wx, wy + 1] == Color:
            wx = wx-1
        elif wx + 1 < int(MapAtt.Xsize)and wy+1 < int(MapAtt.Ysize)\
                and Map[wx, wy + 1] == green and Map[wx + 1, wy] == Color:
            wy = wy + 1
        else:
            wy = randrange(0, int(MapAtt.Ysize) - 1)
            wx = randrange(0, int(MapAtt.Xsize) - 1)
            JustMoved = True

   """


