# classes are like blueprints to objects
#example class
class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
# init - this initialises the class, "self" is the first variable passed into it. but also counts as "itself" when creating sub variables like in powershell
  def __init__(self)
# scopes
  # Global - can be used everywqhere
  # member variable - only usable within a class
  # instance variable - only usable within a particualar instance of a class
# functions within a class - these are called methods
# creating a method
  class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print self.name
    print self.age
    
hippo = Animal("Anderson", 36)
hippo.description()
#inheritance - classes can call other classes
  class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
      self.customer_id = customer_id

    def display_cart(self):
      print "I'm a string that stands in for the contents of your shopping cart!"

  class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
      print "I'm a string that stands in for your order history!"

  monty_python = ReturningCustomer("ID: 12345")
  monty_python.display_cart()
  monty_python.display_order_history()
# small scale example - DerivedClass is the new class you are making and BaseClass is the class from which that new class inherits
  class DerivedClass(BaseClass):
# overriding inheritence - cimply call it but then re-do the function itself
  class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee):
  
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12
# super call - if you have overwritten something but you really need to use the origional you can use a super call
  class Derived(Base):
    def m(self):
      return super(Derived, self).m() # where m is the method from the base class
# repr method - shows how to represent the object if printed etc
  class Point3D(object):
    def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z
    
    def __repr__(self):
      return "(%d, %d, %d)" % (self.x, self.y, self.z)
    
    
  my_point = Point3D(1,2,3)
  print my_point