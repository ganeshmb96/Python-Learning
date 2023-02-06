#This is a learning tutorial on how the OOP concepts work in python
# Instance = class()

class snake():
    def __init__(self, name):       #Self should always be the first argument to be passed to the parameters
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name

python = snake('python')
anaconda = snake('anaconda')

print(python.name)
print(anaconda.name)

anaconda.change_name('anacondas')
print(anaconda.name)

#Code for the main class method
class rocket():
    def __init__(self, rname, rdistance):
        self.rname = rname
        self.rdistance = rdistance

    def launch(self):
        return "%s has reached %s" %(self.rname, self.rdistance)

class mars_rover():       #Inheriting from the baseclass
    def __init__(self, rname, rdistance, maker):
        rocket.__init__(self, rname, rdistance)
        self.maker = maker

    def get_maker(self):
        return "%s launched by %s" %(self.rname, self.maker)

if __name__ == "__main__":
    x = rocket('simple rocket', 'stratosphere')
    y = mars_rover('mars_rover', 'till mars', 'ISRO')
    print(x.launch())
    #print(y.launch())
    print(y.get_maker())