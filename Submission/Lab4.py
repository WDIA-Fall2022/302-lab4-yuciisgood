from sense_emu import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo(G = green,
    Y = yellow,
    B = blue,
    O = nothing):
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo (G = green,
    R = red,
    O = nothing):
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus(W = white,
    O = nothing):
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals(W = white,
    O = nothing):
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart(P = pink,
    O = nothing):
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def elephant(o = (0,0,0),c2 = (255,255,255),c1 = (220,220,220),green = (0,255,0),red = (255,0,0),nothing = (0,0,0)):
    logo = [
    o, o, c1, c1, o, o, o, o,
    o, c1, c1, c1, c1, c1, c1, o,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, c1, c1, c1, c1, c1, c1, c1,
    c1, c2, c2, c1, c1, c1, c1, c1,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, o, c1, c1, o, c1, c1, o,
    c1, o, c2, c1, o, c2, c1, o,
    ]
    return logo
def getUserChoice():
    while 1==1:
        try:
            option = int(input("What do you want to display (0. to exit):\n1. Logo\n2. Plus sign\n3. Equals sign\n4. Raspberry\n5. Heart\n6. Elephant\n0. Exit:"))
        except:
            print("it is not a valid integer")
        else:
            break
    return option

images = [trinket_logo, plus, equals, raspi_logo, heart, elephant]
while True:
    option = getUserChoice()-1
    if option == 0:
        break
    if option > 6 or option < 0:
        print("it is out of the range")
        continue
    s.set_pixels(images[option]())



# images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
# count = 0
# while True: 
#     s.set_pixels(images[option]())
#     time.sleep(.75)
#     count += 1