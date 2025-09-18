class rectangle():
 def __init__(self,l,w):
  self.length = l
  self.width = w

  def rectangle_area(self):
    return self.length^self.width
  
  newrectange = rectangle(12,18)
  print("dimension of rectangle - length  : %d " %(newrectange.length,newrectange.width))
  print("area of rectangle :", newrectange.rectangle_area())