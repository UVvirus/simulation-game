import random
class creature:
    def __init__(self,name):
        self.name=name
        self.hunger=0
        self.boredom=0
        self.tiredness=0
        self.dirtiness=0
        self.food=2
        self.is_sleeping=False
        self.is_alive=True
    def eat(self):
        if self.food > 0:
            self.food -= 1
            self.hunger=random.randint(1,4)
            print(self.name+" ate great meal")
        else:
            print(self.name+" has no food")
            if self.hunger < 0:
                self.hunger=0
    def play(self):
        random_number=random.randint(0,2)
        print(self.name+" wants to play a game")
        print(self.name+" is guessing a number\nguess that number :(0-2)")
        user_input=int(input("Enter a number:"))
        if user_input == random_number:
            print("Your guess is correct")
            self.boredom -= 3
        else:
            print("Your guess is wrong")
            self.boredom -= 1
            if self.boredom < 0:
                self.boredom=0
    def sleep(self):
        self.is_sleeping=True
        self.tiredness -= 3
        self.boredom -= 2
        print("it is sleeping")
        if self.tiredness < 0:
            self.tiredness =0
        if self.boredom < 0:
            self.boredom = 0
    def awake(self):
        random_number=random.randint(0,2)
        if random_number ==0:
            print(self.name+" just woke up")
            self.is_sleeping=False
            self.boredom -= 0
        else:
            print("it is sleeping")
    def clean(self):
        self.dirtiness =0
        print(self.name +" taking a bath")
    def forage(self):
        food_found=random.randint(0,4)
        self.food += food_found
        self.dirtiness += 2
        print("the creature found food:"+str(food_found))
    def show_values(self):
        print("Name:"+self.name+"\n hunger:"+str(self.hunger)+"\n boredom:" +str(self.boredom))
        print("Tiredness:"+str(self.tiredness)+"\n dirtiness:"+str(self.dirtiness)+"\n food inventry:"+str(self.food))

    def increment_values(self,difficulty):
        #user_input=int(input("Enter the difficulty level:(1-5)"))
        self.hunger = random.randint(0,dificulty)
        if self.is_sleeping == False:
            self.boredom += random.randint(0,dificulty)
            self.tiredness +=random.randint(0,dificulty)
            self.dirtiness += random.randint(0,dificulty)
    def kill(self):
        if self.hunger >=10:
            print(self.name+" is starved to  death")
            self.is_alive=False
        elif self.dirtiness >= 10:
            print(self.name+" is suffered from infection")
            self.is_alive=False
        elif self.boredom >= 10:
            self.boredom=10
            print(self.name+" is bored and sleeping")
            self.is_sleeping=True
        elif self.tiredness >= 10:
            self.tiredness=10
            print(self.name+" is feeling sleepy")
            self.is_sleeping=True
def show_menu(creature):
    if creature.is_sleeping:
        choice=input("Enter (6) to wake up")
        choice='6'
        creature.awake()
    else:
        print("The creature is not sleeping\n")
        print("1)eat\n2)play\n3)sleep\n4)bath\n5)forage for food")
        choice=input("Enter your choice:")
        return choice
def call_action(creature,choice):
    if choice == '1':
        creature.eat()
    elif choice =='2':
        creature.play()
    elif choice =='3':
        creature.sleep()
    elif choice =='4':
        creature.clean()
    elif choice == '5':
        creature.forage()
    elif choice =='6':
        creature.awake()
    else:
        print("Enter a valid choice")

dificulty=int(input("Enter dificulty level:(1-5)"))
if dificulty > 5:
    dificulty = 5
if dificulty < 0:
    dificulty = 1
running = True
while running:
    user_input=input("Enter the player name:")
    player=creature(user_input)
    rounds = 1
    while player.is_alive:
        print("current round:"+str(rounds))
        player.show_values()
        round_move=show_menu(player)
        call_action(player,round_move)
        print("stating the round summary."+str(rounds))
        player.show_values()
        input("press Enter to continue:")
        player.increment_values(dificulty)
        player.kill()
        rounds += 1
        print("R.I.P")
        print(player.name+" survived a total of"+str(rounds-1)+" rounds")
        choice=input("Would you like to play again:(Y/N)").lower()
        if choice !='y':
            print("Thank you")
            running =False
