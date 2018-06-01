# classes and Objects

class Dog:
    def __init__(self,name): #acts as constructor
        self.name=name
    def respond_to_command(self, command): # calls other method speak()
        if command == self.name: self.speak()
    def speak(self):
        print "bark mothafucka!!"
        

#Actually constructing the class and calling methods (similar to java)

fido = Dog("fido")
fido.respond_to_command("spot")
fido.respond_to_command("fido")


    