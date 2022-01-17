import cv2
import numpy as np
import os

color = (143, 136, 63)

# Add display
def display(im, box, it):
    nbox = box[it]
    for i in range(len(nbox)):
        cv2.line(im, (int(nbox[i][0]), int(nbox[i][1])), (int(nbox[(i + 1) % len(nbox)][0]), int(nbox[(i + 1) % len(nbox)][1])), color, 6)

# Receives binary input  
def processInput(req, res):
    r""""
    Receives binary input (a path of the image to analyze)
    Returns if any qr was found
    Retur am array of the qr data
    Returns path of the analyzed image
    """
    input = decodeInput(req)
    possible ,results, path = getQRs(input)
    res['possible'] = possible
    res['results'] = results
    res['path'] = path

def getQRs(name):
    if(os.path.isfile(name) is False):
        print("asdl")
        return False, [], name

    inputImage = cv2.imread('{}'.format(name))
    decoder = cv2.QRCodeDetector()
    data, data1, data2, data3 = decoder.detectAndDecodeMulti(inputImage)
    if(data):
        for i in range(len(data2)):
            display(inputImage, data2, i)
        cv2.imwrite('analizado/{}'.format(name), inputImage)
        return data, data1, 'analizado/{}'.format(name)
    else:
        return data, data1, name




def decodeInput(input):
    r""""
    Receives encoded utf-8.
    it should be a single string, the relative path of the image to process
    """ 
    input = input.decode("utf-8")
    return input

