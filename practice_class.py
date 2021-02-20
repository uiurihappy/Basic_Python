class Unit:
    def __init__(self):
        print("unit 생성자")
class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        super().__init__() # 순서상에 맨 마지막에 상속받는 클래스에서만 init 호출
        Unit.__init__(self)
        Flyable.__init__(self)

#드랍쉽
dropship = FlyableUnit()