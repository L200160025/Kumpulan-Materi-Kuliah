
class Foo(object):

    """
    Basic Class with __init__
    Require param: `name`
    """

    def __init__(self, name):
        self._name = name

    def whoami(self):
        return self._name


foo = Foo('Danias')
print foo.whoami()

##
##print "-" * 50
##
##
##class Bar(object):
##
##    """
##    Common methods in the Class.
##    """
##
##    _name = 'Im not John'
##
##    def __init__(self):
##        self._name = 'John'
##
##    @property
##    def _getname(self):
##        return self._name
##
##    @classmethod
##    def greeting(cls, say):
##        return "{0}, {1}".format(
##            say, cls()._getname
##        )
##
##    @staticmethod
##    def find_animal(animal):
##        return ("You catch %s" % animal)
##
##
### Difference between a variable declared inside a class,
### and a variable declared inside an __init__ function
##print Bar._name   # inside class
##print Bar()._name # __init__
##
##
### Getting the `@property`
##print Bar()._getname
##
##
### How about `@classmethod` ?
### With classmethods, the class of the object instance.
##print Bar().greeting('Hello')
##print dir(Bar().greeting)
##
##print Bar().greeting.__class__.__name__
##
##
### `@staticmethod` similiar with `@classmethod`
##print Bar.find_animal('Penguin')
##
##
##print "-" * 50
##
##
##class Baz:
##
##    """
##    I'm a MOM.
##    This basic class inheritance between `Baz()` and `Baz2()`.
##    """
##
##    @staticmethod
##    def helloworld():
##        return "Hello World! Im in Baz()"
##
##    def find_me(self, name):
##        return ("Hello %s, you catch Baz()!" % name)
##
##
##class Baz2(Baz):
##
##    """
##    I'm a Childern.
##    Im inherited from `Baz()`.
##    """
##
##    @staticmethod
##    def magic():
##        return "This magic(), Im in Baz2()"
##
##
##print help(Baz2)
##print Baz().helloworld()     # Default method to return function in the MOM class.
##print Baz2.helloworld()      # or Baz2().helloworld()
##print Baz2.magic()           # or Baz2().magic()
##print Baz2().find_me('John') # if use the `Baz2.find_me('John')` it would be have an error `unbound method`
##
##
##
##
##
##
##
