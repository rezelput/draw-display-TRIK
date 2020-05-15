import sys
import time
import random
import math

class Program():
  __interpretation_started_timestamp__ = time.time() * 1000

  pi = 3.141592653589793 //TRIK variable
  x = None

  def execMain(self):

    
    self.x = -100
    while True:
      brick.display().drawEllipse(self.x + 100, self.x + 100, 50, 50, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 85, self.x + 115, 15, 15, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 115, self.x + 115, 15, 15, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 100, self.x + 95, 10, 10, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 80, self.x + 80, 5, 15, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 115, self.x + 80, 5, 15, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 80, self.x + 80, 0, 5, False)
      brick.display().redraw()
      
      brick.display().drawEllipse(self.x + 115, self.x + 80, 0, 5, False)
      brick.display().redraw()
      
      brick.display().drawLine(self.x + 70, self.x + 60, self.x + 55, self.x + 40)
      brick.display().redraw()
      
      brick.display().drawLine(self.x + 55, self.x + 40, self.x + 55, self.x + 75)
      brick.display().redraw()
      
      brick.display().drawLine(self.x + 140, self.x + 35, self.x + 115, self.x + 65)
      brick.display().redraw()
      
      brick.display().drawLine(self.x + 140, self.x + 45, self.x + 140, self.x + 75)
      brick.display().redraw()
      
      script.wait(1000)
      
      self.x = self.x + 10
      if self.x > 30:
        script.wait(1000000)
        
        brick.stop()
        return
        break
      brick.display().clear()
      brick.display().redraw()
      

def main():
  program = Program()
  program.execMain()

if __name__ == '__main__':
  main()
