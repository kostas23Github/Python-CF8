class Temperature:
  def __init__(self, celcius):
    self.__celcius = celcius

  def get_celcius(self):
    return self.__celcius
  
  def set_celcius(self, value):
    if value < -273.15:
      raise ValueError("Below absolute zero")
    self.__celcius = value

  # deleter
  def del_celcius(self):
    del self.__celcius

  # Full property attributes (for presentation only - Do not use it!)
  # Old school way!
  celcius = property(
    fget=get_celcius,
    fset=set_celcius,
    fdel=del_celcius,
    doc="Temperature in Celcius"
  )

def main():
  t = Temperature(25)
  print(t.get_celcius())  # t.celcius
  t.celcius = 100
  print(t.celcius)

if __name__ == "__main__":
  main()