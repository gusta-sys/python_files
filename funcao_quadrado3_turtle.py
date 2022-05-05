# python_files
import turtle
t = turtle.Turtle()
t.speed(10)
def desenhar (a):
  for i in range (4):
    t.forward(a)
    t.left(90)

desenhar(100)
desenhar(110)
desenhar(120)
desenhar(130)
desenhar(140)
desenhar(150)

turtle.mainloop()
