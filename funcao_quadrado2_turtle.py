# python_files
import turtle
t = turtle.Turtle()
#t.speed(5)

def desenhar (a):
  for i in range (4):
    t.pendown()
    t.forward(a)
    t.left(90)
    
def andar (a):
  t.penup()
  t.forward(a)

desenhar(30)
andar(90)
desenhar(30)
andar(90)
desenhar(30)

turtle.mainloop()
