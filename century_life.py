class CenturyLifeDevice:
    def __init__(self):
        self.age = 0.0
        self.stage = 'Neonate'
    def tick(self, dt=1.0):
        self.age += dt
        return {'age': self.age, 'stage': self.stage}
