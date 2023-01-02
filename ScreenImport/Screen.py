from math import floor
from numpy import array
import PIL.Image
def imgPrint(file,pre=False):
  pixelsarray =array(PIL.Image.open("./" + file)).tolist()
  height,width,total = len(pixelsarray),len(pixelsarray[0]),[]
  for a in range(floor(height/2)):
    string_temp = ""
    for b in range(width):
      clr = [0,0,0,0,0,0]
      for c in range(6): clr[c] = pixelsarray[floor(a*2)+(floor((5-c)/3))][floor(b)][c%3]
      string_temp += f"\033[38;2;{clr[0]};{clr[1]};{clr[2]}m\033[48;2;{clr[3]};{clr[4]};{clr[5]}m▄\033[0m"
    if pre == False: print(string_temp)
    else: total.append(string_temp)
  if pre: return total
