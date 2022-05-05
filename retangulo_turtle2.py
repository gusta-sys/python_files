# python_files
import turtle

t = turtle.Turtle()
#t.speed(5)
a= 100
b=25

for i in range(4):
  if (i  % 2 == 0):
    t.forward(a)
    t.left(90)
  else:
    t.forward(b)
    t.left(90)

turtle.mainloop()
