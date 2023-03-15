class Animal:
  def __init__(self, name, age, run, fly):
    self.name = name
    self.age = age
    self.run = run
    self.fly = fly
  def myfunc(self):
    print("Animal name is  " + self.name)

animal1 = Animal("Tiger", 3, 175, "don't fly") 
animal1.age=3
print("Age: ", animal1.age)
animal1.run=175
print("Speed: ", animal1.run)
animal1.fly="don't fly"
print("Tiger: ",animal1.fly)
animal1.myfunc()