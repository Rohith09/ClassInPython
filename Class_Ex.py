class PartyAnimal:  #Creating a Class
    x = 0
    name="Rohith09"  #Creating a variables.

    def party(self):            #Declaring a function.Using Self is mandatory in order to access the variables

        self.x = self.x + 1
        print(self.name)
        print("So Far ", self.x)


an = PartyAnimal()  #Creating an instance of the class "Party Animal".
an.party()
an.party()
