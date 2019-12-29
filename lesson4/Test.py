class Car:
    name = 'None'
    height = 1000
    speed = 200.00

    def set(self, name, height, speed):
        self.name = name
        self.height = height
        self.speed = speed

audi = Car()

audi.set('Audi', 1450, 320.0)

print(audi.name)