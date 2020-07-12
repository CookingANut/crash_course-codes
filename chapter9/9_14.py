from random import randint

class Dice():
    """定义一个几面的骰子"""
    
    def __init__(self,side=6):
        """初始化一个骰子的面数"""
        self.side = side
    
    def roll_dice(self,roll_times):
        """掷几次骰子就写几次"""
        for roll_time in range(roll_times):
             print(randint(1,self.side))

#dice_6sides = Dice()
#dice_6sides.roll_dice(10)

#dice_10sides = Dice(10)
#dice_10sides.roll_dice(10)

#dice_20sides = Dice(20)
#dice_20sides.roll_dice(10)

lulu =Dice(7)
lulu.roll_dice(10)



