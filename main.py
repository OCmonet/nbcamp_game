import time
import random

# # 게임 오프닝 시작
# ask_skip = input(
#     "\n\n\n\n\n\n\n\n\n게임이 시작됩니다. 오프닝을 보시겠습니까?\n(y/n)\n\n\n\n\n\n 답변: ")

# if ask_skip == "y" or ask_skip == "yes" or ask_skip == "Y":
#     time.sleep(2)
#     print("\n\n\n\n\n\n\n\n-아빠!!\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n-아빠!!!!!\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n초등학교 앞.\n\n\n\n\n\n")
#     time.sleep(1)
#     print("\n\n\n\n\n\n\n\n학교가 끝난 어린이들이 왁자지끌 떠드는 소리로 북적거린다.\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n...\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n문득 오른 손에 느껴지는 작고 따뜻하고 말랑한 감촉.\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n무언가가 내 오른손을 잡아당긴다. 고개를 돌려본다.\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n말랑한 것의 정체는 바로\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n내 일곱 살 짜리 아들의 고사리 같은 손!!\n\n\n\n\n\n")
#     time.sleep(5)
#     print("\n\n\n\n\n\n\n\n-아빠!! 모해!! 빨랑!!\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n아들이 내 손을 바삐 잡아 끌며, 빠르게 인파 속을 헤집고 들어간다.\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n나는 어디로 향하는 지도 모르는 채...\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n거대한 초딩들의 파도 속으로 딸려들어 가고 있다...\n\n\n\n\n\n")
#     time.sleep(5)
#     print("\n\n\n\n\n\n\n. . .\n\n\n\n\n\n")
#     time.sleep(5)
#     print("\n\n\n\n\n\n\n-아빠! 다 왔어!!!\n\n\n\n\n\n")
#     time.sleep(5)
#     print("\n\n\n-이것 좀 봐봐!! 빨리!!!\n\n\n\n\n\n")
#     time.sleep(5)
#     print("\n\n\n\n\n\n\n\n아들의 손가락이 가리키는 곳에는. . .\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n그것이 있었다. . .\n\n\n\n\n\n")
#     time.sleep(2.5)
#     print("\n\n\n\n\n\n\n\n바로. . .\n\n\n\n\n\n")
#     time.sleep(3.5)
#     print("\n\n\n\n\n\n\n\n병아리!!\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n으윽....!!!!!!!!!!!!\n\n\n\n\n\n")
#     time.sleep(1)
#     print("\n\n\n\n\n\n\n\n병아리를 본 나는\n\n\n\n\n\n")
#     time.sleep(1)
#     print("\n\n\n\n\n\n\n\n일순간 너무 귀엽다고 느껴버렸고\n\n\n\n\n\n")
#     time.sleep(1.5)
#     print("\n\n\n\n\n\n\n\n무언가 가슴 속이 엄청 조여오면서\n\n\n\n\n\n")
#     time.sleep(2)
#     print("\n\n\n\n\n\n\n\n그대로 눈 앞이 흐려져 버렸다.\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n의사의 진단차트에는 이렇게 적혔다.\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\na 환자의 사인은...\n\n\n\n\n\n")
#     time.sleep(3)
#     print("\n\n\n\n\n\n\n\n 심쿵사♥ \n\n\n\n\n\n")
#     time.sleep(5)
#     # 주인공 속성 고르기 코딩으로 넘어가야함


# else:
#     print("\n\n\n\n\n\n\n\n오프닝이 스킵되었습니다.\n곧바로 본 게임이 시작됩니다.\n\n\n\n\n")
#     time.sleep(5)
#     # 주인공 속성 고르기 코딩으로 넘어가야함
# # 게임 오프닝 끝


# 주인공 속성 고르기 시작
while True:
    slimetype = input(
        "\n\n\n\n\n\n\n\n당신은 슬라임으로 다시 태어났습니다. \n어떤 슬라임이 되시겠습니까? \n\n1.불 2.얼음 3.독 \n\n위 세가지 속성 중에 고르세요. \n\n\n\n\n 답변: ")

    if slimetype == "불" or slimetype == "1.불" or slimetype == "1":
        print("\n\n\n잘 하셨습니다!! \n당신은 이제부터 불 속성 슬라임 입니다!!")
        slimetype = "불"
        time.sleep(1)
        break
    elif slimetype == "얼음" or slimetype == "2.얼음" or slimetype == "2":
        print("\n\n\n잘 하셨습니다!! \n당신은 이제부터 얼음 속성 슬라임 입니다!!")
        slimetype = "얼음"
        time.sleep(1)
        break
    elif slimetype == "독" or slimetype == "3.독" or slimetype == "3":
        print("\n\n\n잘 하셨습니다!! \n당신은 이제부터 독 속성 슬라임 입니다!!")
        slimetype = "독"
        time.sleep(1)
        break
    else:
        print("\n잘못 골랐습니다. ^^ㅋ\n3초 후 다시 묻겠습니다.")
        time.sleep(1)

while True:
    user_name = input("\n\n\n\n\n\n\n\n이번엔 당신의 닉네임을 적어주세요\n\n\n\n\n 답변: ")

    if user_name:
        print(
            f"\n\n\n잘 하셨습니다!! 이제부터 당신의 이름은 {user_name}입니다.\n{slimetype}속성의 슬라임 {user_name}님! 건승을 빕니다!\n\n\n\n\n")
        time.sleep(1)
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
    def __init__(self, hp, mp, power):
        self.name = user_name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.power = power

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
        print(f"{self.name}의 하찮은 공격! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 모든 것을 체념하고 쓰러졌습니다.ㅠㅠ")

    def show_status(self):
        print(f"현재{self.name}의\n남아있는 HP는 : {self.hp}   /{self.max_hp}\n 남아있는 MP는 : {self.mp}   /{self.max_mp} 입니다.")

# 캐릭터 모델링 끝


# 배틀!
UserSlime(500, 200, 50)  # 유저슬라임 스테이터스 지정
Monster("공룡몬", 500, 50)  # 몬스터 스테이터스 지정

while True:
    # 싸움 시작하기 전에 주인공슬라임과 몬스터 상태 정보 출력
    UserSlime.show_status()
    Monster.show_status()

    action = input(
        "\n\n\n\n\n\n새로운 야생의 몬스터가 나타났다! 1.물리공격 2.도망간다\n\n\n\n\n답변: \n\n")

    if action == 1:
        UserSlime.normal_attack(Monster)
        Monster.show_status()

        if UserSlime.hp < 0:
            print("주인공이 사망하였습니다. 게임 오버!")
            break

        if Monster.hp < 0:
            print("몬스터를 처치하였습니다!")
            continue
