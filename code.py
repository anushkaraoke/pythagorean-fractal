import turtle
import math

def block(sq, sq_side_len, col_index): #, col_index
    sq.color(colors[col_index])
    sq.begin_fill()
    for i in range(0,4):
        sq.fd(sq_side_len)
        sq.lt(90)
        i+=1
    sq.end_fill()

def generate_h_list(vert_levels):
    if vert_levels>1:
        if (vert_levels==2):
            h_nums = [1]
        elif (vert_levels==3):
            h_nums = [1, 2]
        else:
            h_nums = [1, 2]
            for k in range(0, vert_levels-3):
                for i in range(0, len(h_nums)-1):
                    h_nums.append(h_nums[i])
                    i+=1
                h_nums.append(h_nums[int(len(h_nums)/2)]+1)
                k+=1
    else:
        h_nums=[0]
    return h_nums    
    
def gototop(sq, sq_side_len):   
    sq.lt(90)
    sq.fd(sq_side_len)
    sq.rt(90)
    sq.lt(lang)
    
def gotort(sq, sq_side_len):    
    sq.rt(lang)
    sq.fd(sq_side_len)
    sq.rt(90)
    sq.fd(sq_side_len)

def gotobot(sq, sq_side_len, h_list, h_index, col_index):   
    right_side_len=sq_side_len*r_fac/l_fac
    sq.fd(right_side_len)
    for i in range(0,h_list[h_index]):
        sq.rt(lang)
        col_index=col_index-1
        sq.color(colors[col_index])
        right_side_len=right_side_len/r_fac
        sq.fd(right_side_len)
        sq.lt(90)
        i+=1
    sq.rt(90)
    
def generate_blocks(sq, sq_side_len, sq_min_len, col_index, h_i):
    #reposition the turtle
    turtle.Screen().bgcolor(background)
    sq.color(background)
    sq.bk(sq_size)
    sq.lt(90)
    sq.bk(sq_size+80)
    sq.rt(90)
    
    if sq_side_len/sq_min_len<1:
        print("Square edge length must be larger than 10.")
    elif ((sq_side_len/sq_min_len)>=1 and 
             (sq_side_len/sq_min_len)<2):
        block(sq, sq_side_len, col_index)
    else:   
        for h_i in range(0, len(h_list)):
            while col_index<=max(h_list):
                block(sq, sq_side_len, col_index)
                gototop(sq, sq_side_len)
                sq_side_len=sq_side_len*l_fac
                col_index=col_index+1
                new_sq_side_len=sq_side_len/l_fac
                new_col_index=col_index-1
            gotort(sq, new_sq_side_len)
            block(sq, new_sq_side_len*r_fac/l_fac, new_col_index)
            gotobot(sq, new_sq_side_len, h_list, h_i, 
                    new_col_index)
            col_index=max(h_list)-h_list[h_i]
            sq_side_len=new_sq_side_len*(r_fac**(2-h_list[h_i]))/(
                    l_fac**2)
            h_i+=1    


sq = turtle.Turtle()
#change color list
size = turtle.numinput('Image size', 'What should be the output image size? \nEnter "1" for Small \nEnter "2" for Medium \nEnter "3" for Large')
if size==1:
    sq_min_len = 10
elif size==3:
    sq_min_len = 20
else:
    sq_min_len = 15

col_index=0
lang = math.degrees(math.asin(4/5))
l_fac = 3/5
r_fac = 4/5

levels = turtle.numinput('Levels', 'Enter the number of colours to display (between 1 and 11):')
h_list = generate_h_list(int(levels))  
h_index=0

color_scheme = turtle.numinput('Colour scheme', 'Choose a colour scheme and enter the corresponding number: \n1 - autumn \n2 - bright \n3 - calm \n4 - winter')
if color_scheme==1:
    colors = ['maroon', 'gold', 'chocolate', 'olive', 
              'saddle brown', 'brown', 'dark olive green',  
              'goldenrod', 'dark khaki', 'sandy brown', 'dark red']
    background = 'pale goldenrod'
elif color_scheme==3:
    colors = ['powder blue', 'misty rose', 'pale green', 'wheat', 
              'pale turquoise', 'plum', 'light salmon', 'burlywood',  
              'peach puff', 'silver', 'medium slate blue']
    background = 'light slate gray'
elif color_scheme==4:
    colors = ['light gray', 'silver', 'dark gray', 'silver', 
              'dark gray', 'gray', 'dark gray', 'gray', 
              'dim gray', 'gray', 'dim gray']
    background = 'white'
else:
    colors = ['firebrick', 'red', 'orange', 'yellow', 
          'green yellow', 'green', 'deep sky blue', 
          'dodger blue', 'navy', 'purple', 'pink']
    background = 'white'


sq.speed('fastest') #fastest(0), fast, normal, slow, slowest (10-1)
sq_size=sq_min_len*levels
x=sq_size*5
y=1.5*(sq_size+(int(levels)*sq_size/2))
turtle.screensize(x,y)
generate_blocks(sq, sq_size, sq_min_len, col_index, h_index)
sq.hideturtle()
turtle.done()
