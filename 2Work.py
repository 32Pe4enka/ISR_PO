year = int(input("Введите желаемый год: \n"))
array = [0, 0, 0, 
0, 0, 0,
0, 0, 0, 
0, 0, 0]
##array1 = ["Январь", "Февраль", "Март", 
# "Апрель", "Май", "Июнь", 
# "Июль", "Август", "Сентябрь", 
# "Октябрь", "Ноябрь", "Декабрь"] 

int = month_chet = 168
int = ne_chet_month = 172
int = viskos = 165
int = No_viskos = 154

for x in range(12):
    if (x)%2 == 0:
        print(array[x] + ne_chet_month)
    else:
        if x == 1:
            if (year % 4 == 0):
                print(array[x] + viskos)
            else:
                print(array[x] + No_viskos)
        else:
            print(array[x] + month_chet)
if(year % 4 == 0):
    print(month_chet * 5 + ne_chet_month * 6 + viskos)
else:
    print((month_chet * 5 + ne_chet_month * 6 + No_viskos))