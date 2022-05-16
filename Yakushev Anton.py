zs="Овен/Телец/Близнецы/Рак/Лев/Дева/Скорпион/Стрелец/Козерог/Водолей/Рыбы".split("/")

class ZNAK:
    def __init__(self,surname,name,sign,date):
        self.surname=surname
        self.name=name
        self.sign=sign
        self.date=date

def get():
    print("Введите данные для 8 человек")
    mass=[]
    n=8
    for i in range(n):
        mas=input("Введите Фамилию и имя:").split()
        mas.append(input("Знак зодиака(Овен/Телец/Близнецы/Рак/Лев/Дева/Скорпион/Стрелец/Козерог/Водолей/Рыбы):"))
        mas.append(input("Введите дату рождения(через точку):").split("."))
        
        if len(mas)!=4:
            print("Неправильно введены имя или фамилия")
            mas=get()
        if mas[2] not in zs:
            print("Неправильно введен знак зодиака")
            mas=get()
        if len(mas[3])!=3:
            print("Неправильно введена дата рождения")
            mas=get()
        try:mas[3]=[int(mas[3][0]),int(mas[3][1]),int(mas[3][2])]
        except:
            print("Неправильно введена дата рождения")
            mas=get()
        mass.append(ZNAK(mas[0],mas[1],mas[2],mas[3]))
    k=0
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if zs.index(mass[j].sign)<zs.index(mass[k].sign):
                k=j
        if k!=i:
            mas=mass[i]
            mass[i]=mass[k]
            mass[k]=mas
    return mass
def input_month():
    month=input("Введите номер месяца:")
    try:month=int(month)
    except:
        print("Неправильно введен месяц")
        month=input_month()
    return month
def output(mass,month):
    for i in range(len(mass)):
        if (mass[i].date[1]==month):
            print(mass[i].surname,mass[i].name,mass[i].sign,mass[i].date)
def main():
    mass=get()
    month=input_month()
    output(mass,month)
    





    
if __name__=="__main__":
    main()
