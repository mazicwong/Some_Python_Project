class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name
    # Instance method (实例方法)
    def greet(self, loud = False):
        if loud:
            print('Hello, %s !' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')
g.greet()
g.greet(loud=True)
