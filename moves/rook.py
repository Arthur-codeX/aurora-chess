no_letters=['A','B','C','D','E','F','G','H']
letters_no={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def rook(co):
    l=co[0]
    n=co[1]
    x0=letters_no[l]
    y0=int(n)-1
    print(f"X0=>{x0} Y0=>{y0}")
    new_co=[]
    up(new_co,x0,y0)
    down(new_co,x0,y0)
    right(new_co,x0,y0)
    left(new_co,x0,y0)
    print(new_co)

def up(arr,x0,y0):
    for i in range(1,8):
       n_x= x0
       n_y=y0+i
       if n_x>=0 and n_x<=7 and n_y>=0 and n_y<=7:
         n_x_l=no_letters[n_x]
         arr.append(f"{n_x_l}{n_y}")

def down(arr,x0,y0):
    for i in range(1,8):
       n_x= x0
       n_y=y0-i
       if n_x>=0 and n_x<=7 and n_y>=0 and n_y<=7:
         n_x_l=no_letters[n_x]
         arr.append(f"{n_x_l}{n_y}")

def right(arr,x0,y0):
    for i in range(1,8):
       n_x= x0+i
       n_y=y0
       if n_x>=0 and n_x<=7 and n_y>=0 and n_y<=7:
         n_x_l=no_letters[n_x]
         arr.append(f"{n_x_l}{n_y}")

def left(arr,x0,y0):
    for i in range(1,8):
       n_x= x0-i
       n_y=y0
       print(f"left: x=${n_x} y=${n_y}")
       if n_x>=0 and n_x<=7 and n_y>=0 and n_y<=7:
         n_x_l=no_letters[n_x]
         arr.append(f"{n_x_l}{n_y}")
rook("H8")
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#ABCDEFGHIJKLMNOPQRSTUVWXYZ
