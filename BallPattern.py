from PIL import Image 

pathBackground = "/home/nima/Desktop/2019-12-01_12-16/200.jpg"
pathBallPattern = "/home/nima/Desktop/ballPattern/patterns/hiclipart.com.png"
pathFinal = "/home/nima/Desktop/result60.jpg"


def changeJpgToTxt(path):
    path = path.strip('.jpg')
    path = path + ".txt"
    return path

def readTxt(path):
    with open(path) as fp:
        data = [list(map(int, line.strip().split(' '))) for line in fp]
        return data


def paste(background, transparent, coorX, coorY, ballSizeX, ballSizeY, saveDir):

    Image1 = Image.open(background) 
    
    Image1copy = Image1.copy() 
    Image2 = Image.open(transparent) 

    Image2 = Image2.resize((ballSizeX, ballSizeY), Image.BILINEAR)

    Image1copy.paste(Image2, (coorX- (ballSizeX*int(0.1)), coorY-(ballSizeY*int(0.1))), Image2.convert('RGBA'))

    Image1copy.save(saveDir, 'JPEG', quality=100) 
    # print(changeJpgToTxt(pathBackground))
    # print(readTxt(changeJpgToTxt(pathBackground)))

pos = readTxt(changeJpgToTxt(pathBackground))
print(pos)
paste(pathBackground, pathBallPattern, (pos[0][1] - ((pos[0][3])/2)), (pos[0][2] - ((pos[0][4])/2)), pos[0][3], pos[0][4], pathFinal)
if len(pos) >= 2:
    paste(pathFinal, pathBallPattern, (pos[1][1] - ((pos[1][3])/2)), (pos[1][2] - ((pos[1][4])/2)), pos[1][3], pos[1][4], pathFinal)