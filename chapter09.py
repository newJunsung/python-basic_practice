class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        # print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}".format(self.hp))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
# marine1 = Unit("마린", 40, 5) # self를 제외한 init에 있는 매개변수가 모두 들어가야 한다.
# marine1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 외부에서 변수를 추가할 수 있음. wraith1은 쓸 수 없음.
# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# # -------------------------------------------------------------------------------------

# # 메소드
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
        
#     def attack(self, location): 
#         print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# # -------------------------------------------------------------------------------------

# # 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location): 
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# # -------------------------------------------------------------------------------------

# # 다중상속, 연산자 오버로딩
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌쳐", 80, 10, 20)
# vulture.move("11시")
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")

# # -------------------------------------------------------------------------------------

# # pass, super
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, location)
        self.location = location
        # pass # 아무것도 안하고 일단 넘어감(완성된 것처럼 보이기)
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("게임을 시작합니다")
# def game_over():
#     pass
# game_start()
# game_over()

# # -------------------------------------------------------------------------------------

# # Quiz
class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

k = House("강남", "아파트", "매매", "10억", "2010년")
m = House("마포", "오피스텔", "전세", "5억", "2007년")
s = House("송파", "빌라", "월세", "500/50", "2000년")
realEstate = []
realEstate.append(k)
realEstate.append(m)
realEstate.append(s)

print("총 {0}대의 매물이 있습니다.".format(len(realEstate)))
for show in realEstate:
    show.show_detail()