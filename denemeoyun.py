import de1

screen = de1.Display.set_witdh_height(600,600)
de1.Display.set_color_screen(234,214,62)
rect1 = de1.Draws.draw_rect(0,0,100,100,125,234,124)
while True: 
    de1.Display.start_screen(234,214,62)
    if de1.Inputs.Press.w() and rect1.y > 0:
        rect1 = de1.Movements.move_rects(rect1,y=-1,w=rect1.w,h=rect1.h)
    if de1.Inputs.Press.s() and rect1.y+rect1.h < 600:
        rect1 = de1.Movements.move_rects(rect1,y=1,w=rect1.w,h=rect1.h)
    if de1.Inputs.Press.d() and rect1.x+rect1.w < 600:
        rect1 = de1.Movements.move_rects(rect1,1,w=rect1.w,h=rect1.h)
    if de1.Inputs.Press.a() and rect1.x > 0:
        rect1 = de1.Movements.move_rects(rect1,-1,w=rect1.w,h=rect1.h)
    rect1 = de1.Draws.draw_rect(rect1.x,rect1.y,rect1.w,rect1.h,125,234,124)
    de1.Display.set_fps(250)
    de1.Display.update_screen()
    
    
        

