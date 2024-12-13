print("Sinh vien:Nguyen Ba Linh")
print("MSSV:205752020710008")
#########
import turtle,random
colors = ['red','green','blue','oranger','purple','pink','yellow']
painter = turtle.Turtle()
painter.pensize(3)
for i in range(12):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.right(30)
    painter.left(60)
painter.setposition(0, 0)
    
