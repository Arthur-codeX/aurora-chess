all_cordinate=[
    {'x':-1,'y':2},
    {'x':1,'y':2},
    {'x':2,'y':1},
    {'x':2,'y':-1},
    {'x':1,'y':-2},
    {'x':-1,'y':-2},
    {'x':-2,'y':-1},
    {'x':-2,'y':1},
               ]

no_letters=['A','B','C','D','E','F','G','H']
letters_no={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

#E5
def night(co):
    l=co[0]
    n=co[1]
    x0=letters_no[l]
    y0=int(n)-1
    print(f"X0=>{x0} Y0=>{y0}")
    new_co=[]
    for piece_co in all_cordinate:
        # print(piece_co)
        n_x=x0+piece_co['x']
        n_y=y0+piece_co['y']
        if n_x>=0 and n_x<=7 and n_y>=0 and n_y<=7:
            n_x_l=no_letters[n_x]
            new_co.append(f"{n_x_l}{n_y}")
    print(new_co)

    # Strp convert cordinates to numbers

night("A1")