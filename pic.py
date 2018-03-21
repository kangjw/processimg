from PIL import Image
from struct import *

global outfile

def create_data_file(): 
   global outfile
   outfile = open('pic.dat','wb')


def open_pic_file():
   f = open('pic.ini','r')
   for line in f.readlines():
       process_file(line)
       print line


def process_file(file):
   global outfile
   img = Image.open(file.strip('\n').strip('\r'))
   print img.size
   width = img.size[0]
   height = img.size[1]

   #outfile = open('testrgb.dat','wb')
   if width > height :
       img_r = img.rotate(90)
       print img_r.size
       pix = img_r.load()
       width = img_r.size[0]
       height = img_r.size[1]
   else:   
   	pix = img.load()

   for y in range(0, height):
     for x in range(0, width):
       #print pix[x,y]
       r = int(pix[x,y][0])>>3
       g = int(pix[x,y][1])>>2
       b = int(pix[x,y][2])>>3
       #print r,g,b
       #data_str=pack("H",r|g<<5|b<<11)
       data_str=pack(">H",r<<11|g<<5|b)
       outfile.write(data_str)

def close_data_file():
    global outfile
    outfile.close()


if __name__=="__main__":
   print("main")
   create_data_file()
   open_pic_file()
   close_data_file()


