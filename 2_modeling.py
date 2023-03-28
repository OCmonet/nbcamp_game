import time
import random

# 주인공 속성 고르기 시작
while True:
    slimetype = input(
        "\n\n\n\n\n\n\n\n당신은 슬라임으로 다시 태어났습니다. \n어떤 슬라임이 되시겠습니까? \n\n1.불 2.얼음 3.독 \n\n위 세가지 속성 중에 고르세요. \n\n\n\n\n 답변: ")

    if slimetype == "불" or slimetype == "1.불" or slimetype == "1":
        print("\n\n\n잘 하셨습니다!! \n당신은 이제부터 불 속성 슬라임 입니다!!")
        slimetype = "불"
        time.sleep(3)
        break
    elif slimetype == "얼음" or slimetype == "2.얼음" or slimetype == "2":
        print("\n\n\n잘 하셨습니다!! \n당신은 이제부터 얼음 속성 슬라임 입니다!!")
        slimetype = "얼음"
        time.sleep(3)
        break
    elif slimetype == "독" or slimetype == "3.독" or slimetype == "3":
        print("\n\n\n잘 하셨습니다!! \n당신은 이제부터 독 속성 슬라임 입니다!!")
        slimetype = "독"
        time.sleep(3)
        break
    else:
        print("\n잘못 골랐습니다. ^^ㅋ\n3초 후 다시 묻겠습니다.")
        time.sleep(3)

while True:
    user_name = input("\n\n\n\n\n\n\n\n이번엔 당신의 닉네임을 적어주세요\n\n\n\n\n 답변: ")

    if user_name:
        print(
            f"\n\n\n잘 하셨습니다!! 이제부터 당신의 이름은 {user_name}입니다.\n{slimetype}속성의 슬라임 {user_name}님! 건승을 빕니다!\n\n\n\n\n")
        time.sleep(3)
        break
    else:
        print("\n이름을 다시 제대로 써 주세요.\n3초 후 다시 묻겠습니다.")
        time.sleep(3)
# 주인공 속성 고르기 끝


# 캐릭터 모델링 시작
class Character:

    # 표준스테이터스함수
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        # 공통으로가질 것: name, max_hp, hp,             power
        # 주인공만 가질것: name, max_hp, hp, max_mp, mp, power, slimetype
        # 몬스터가 가질것: name, max_hp, hp,             power

    # 표준공격함수: 주인공은 normal_attack, skill_attack_1, skill_attack_2 로 총 3가지 만들 것
    def normal_attack(self, target):
        damage = random.randint(self.power - 3, self.power + 3)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 현기증을 느끼며 쓰러졌습니다.")

    # 상태확인함수
    def show_status(self):
        print(f"현재{self.name}의\n남아있는 HP는 : {self.hp}   /{self.max_hp}\n 남아있는 MP는 : {self.mp}   /{self.max_mp} 입니다.")


# 주인공 슬라임
class UserSlime(Character):
    def __init__(self, name, hp, mp, power):
        super().__init__(self, name, hp, power)
        self.name = user_name
        self.max_mp = mp
        self.mp = mp

    def normal_attack(self, target):
        damage = random.randint(self.power - 3, self.power + 3)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.name}의 물리공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 비 오는 날 먼지나도록 두들겨 맞고 쓰러졌습니다.")

    def skill_attack_1(self, target):
        damage = random.randint(self.power + 30, self.power + 35)
        target.hp = max(target.hp - damage, 0)
        self.mp = max(self.mp - 10, 0)
        print(f"{self.name}의 불꽃발사!!!\n화려한 불꽃이{target.name}을 감싸며 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 불꽃을 맞고 홀라당 불타버렸습니다.")
        if self.mp == 0:
            print(
                f"푸쉬쉬시... 손가락 끝에서 원소가 사그러듭니다. \n {self.name}의 마력이 바닥났습니다. 물리공격으로 공격하세요.")

    def skill_attack_2(self, target):
        damage = random.randint(self.power + 70, self.power + 100)
        target.hp = max(target.hp - damage, 0)
        self.mp = max(self.mp - 30, 0)
        print(
            f"{self.name}의 지옥불 메테오!!!\n하늘에서 내려오는 거대한 불덩어리가 {target.name}에게 명중해서 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 메테오를 맞고 숯검댕이 되었습니다.")
        if self.mp == 0:
            print(
                f"푸쉬쉬시... 손가락 끝에서 원소가 사그러듭니다. \n {self.name}의 마력이 바닥났습니다. 물리공격으로 공격하세요.")

    # 상태확인함수
    def show_status(self):
        print(f"현재{self.name}의\n남아있는 HP는 : {self.hp}   /{self.max_hp}\n 남아있는 MP는 : {self.mp}   /{self.max_mp} 입니다.")


# 졸병몬스터
class Monster(Character):
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def bite_attack(self, target):
        damage = random.randint(self.power - 10, self.power + 10)
        target.hp = max(target.hp - damage, 0)
        print(f"{self.name}의 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 모든 것을 체념하고 쓰러졌습니다.ㅠㅠ")

    def show_status(self):
        print(f"현재{self.name}의\n남아있는 HP는 : {self.hp}   /{self.max_hp}\n 남아있는 MP는 : {self.mp}   /{self.max_mp} 입니다.")

# 캐릭터 모델링 끝
