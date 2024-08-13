# Create a base class Bird with a method fly. Create derived classes Eagle and Penguin. Override the fly method in Penguin to indicate that penguins cannot fly
class Bird:
    raise NotImplementedError("Subclass must implement abstract method.")


class Eagle(Bird):
    def fly(self):
        return "The eagle soars high in the sky!"


class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly."


eagle = Eagle()
penguin = Penguin()

print("Eagle: ", eagle.fly())
print("Penguin: ", penguin.fly())