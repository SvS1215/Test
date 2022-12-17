class Moscal:
    Alive = True
    IQ = -80
    Name = "Москаль"
    Age = "ХЗ"
    Money = 500
    def Info(self):
        print(f"Name: {self.Name}\nAge: {self.Age}\nAlive: {self.Alive}\nIQ: {self.IQ} \nMoney: {self.Money}")
    def sayHello(self):
        print("Hello")
    def Vid(self):
        print('Вас вбито!')
        self.Alive = False
    def iqBoost(self,money_added):
        print("Booooost!")
        self.Money = self.Money - money_added
    def ZSU(self):
        print('Здався ЗСУ')
        self.Name = "Чмоня"
        self.IQ = 40
        self.Age = 29
        self.Money = 0
        self.Alive = True
Moscal1 = Moscal()
Moscal1.Info()
print('-'*60)
Moscal1.Vid()
Moscal1.Info()
print('-'*60)
Moscal1.iqBoost(1000)
Moscal1.Info()
print('-'*60)
Moscal1.ZSU()
Moscal1.Info()