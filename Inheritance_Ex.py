class Parent():

    def parent_method(self):
        print("Code from the parent class")


class Child(Parent):

    def child_method(self):
        print("Code from the child class")


chd= Child()
chd.parent_method()
chd.child_method()