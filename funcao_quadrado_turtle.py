# python_files
import turtle
t = turtle.Turtle()

def desenhar (a):
  for i in range (4):
    t.forward(a)
    t.left(90)

desenhar(50)

turtle.mainloop()
