__authour__ = 'Сумароков Евгений Владимирович'
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    n = number*10**(ndigits)
    if  n- int(n)>=0.5:
      n = int(n)+1
    else:
      n = int(n)
    n = n*10**(- ndigits)
    n = float('{:.5f}'.format(n))
    return n

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
   a = 0
   b = 0
   if ticket_number//(10**5)==0:
       return 1==0
   for i in range(6):
       if i<=2:
           a+=ticket_number%10
           ticket_number=ticket_number//10
       else:
           b+=ticket_number%10
           ticket_number=ticket_number//10
   return a==b

print(lucky_ticket(123006))
print(lucky_ticket(42321))
print(lucky_ticket(436751))
