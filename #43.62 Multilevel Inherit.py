# Multilevel Inheritance.

class dad:
    Hobby = "Very Good at Playing BasketBall."
    BasketBall_Score = 12

class son(dad):
    Hobby = "Very Good at Playing Video Games."
    Game_Score = 15
    def printscore(self):
        print(f"My Score in Video Games is {self.Game_Score}")

class grandson(son):
    Hobby = "Very Good at Playing BasketBall and Video Games."
    BasketBall_Score = 13
    Game_Score = 16

    def printscore(self):
        print(f"My scores are :- \nBasketBall : {self.BasketBall_Score}\nVideo Game : {self.Game_Score} ")

darry = dad()
larry = son()
harry = grandson()

print(f"{darry.Hobby}\n{darry.BasketBall_Score}")
print(f"{larry.Hobby}\nBasketBall : {larry.BasketBall_Score}\nVideo Games : {larry.Game_Score}")
larry.printscore()
print(f"{harry.Hobby}\nBasketBall : {harry.BasketBall_Score}\nVideo Games : {harry.Game_Score}")
harry.printscore()




