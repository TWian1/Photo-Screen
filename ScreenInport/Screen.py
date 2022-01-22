import math, json, os, numpy as np
from PIL import Image
def imgPrint(auto, pixelsarray, w = 10, h = 10, file = ""):
  if file != "": pixelsarray = np.array(Image.open("./" + file)).tolist()
  if auto: h,w = len(pixelsarray),len(pixelsarray[0])
  halflen = len(pixelsarray) / 2
  for a2 in range(math.floor(h)):
    a = a2
    if h != math.floor(halflen): a = a2 * (len(pixelsarray)/(h*1))
    if a % ((len(pixelsarray)/h)*2) != 0:
      temp = ""
      for b2 in range(w):
        b,clr = b2,[0,0,0,0,0,0]
        if w != len(pixelsarray[0]): b = b2 * (len(pixelsarray[0])/w)
        try:
          for c in range(3): clr[c] = pixelsarray[math.floor(a)][math.floor(b)][c]
          for c in range(3): clr[c+3] = pixelsarray[math.floor(a)-1][math.floor(b)][c]
        except Exception: pass
        temp += f"\033[38;2;{clr[0]};{clr[1]};{clr[2]}m\033[48;2;{clr[3]};{clr[4]};{clr[5]}m▄\033[0m"
      print(temp)
