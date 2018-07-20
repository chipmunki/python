__Authour__ = 'Сумароков Евгений Владимирович'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
class figure:
    def __init__(self,A,B,C):
        self.A = (int(A.split(',')[0]), int(A.split(',')[1]))
        self.B = (int(B.split(',')[0]), int(B.split(',')[1]))
        self.C = (int(C.split(',')[0]), int(C.split(',')[1]))        
    def side(self,P,Q):
        PQ = sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)
        return PQ
    
class triangle(figure):
    def __init__(self,A,B,C):
        figure.__init__(self,A,B,C)
        
    def square (self):
        S = 1/2*((self.A[0]-self.C[0])*(self.B[1]-self.C[1])-(self.B[0]-self.C[0])*(self.A[1]-self.C[1]))
        return abs(S)
    def perimeter (self):
        P = super().side(self.A,self.B)+super().side(self.B,self.C)+super().side(self.A,self.C)
        return P
    def altitude (self):
        l = input('Введите сторону, к которjй хотите найти высоту ')
        if l == 'AB' or l == 'BA':
            H = 2*self.square()/super().side(self.A,self.B)
        if l == 'BC' or l == 'CB':
            H = 2*self.square()/super().side(self.B,self.C)
        if l == 'CA' or l == 'AC':
            H = 2*self.square()/super().side(self.A,self.C)
        return H
A = input('Введите координаты точки А через запятую. A  ')
B = input('Введите координаты точки B через запятую. B  ')
C = input('Введите координаты точки C через запятую. C  ')
tr = triangle(A, B, C)
print('S = ', tr.square())
print('P = ', tr.perimeter())
print('H = ', tr.altitude())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class quadrangle(figure):
    def __init__(self,A,B,C,D):
        figure.__init__(self,A,B,C)
        self.D = (int(D.split(',')[0]), int(D.split(',')[1]))
    def perimeter (self):
        P = super().side(self.A,self.B)+super().side(self.B,self.C)+super().side(self.D,self.C)+super().side(self.D,self.A)
        return P
    def square(self):
        S = 1/2*(self.A[0]*self.B[1]+self.B[0]*self.C[1]+self.C[0]*self.D[1]-
                 self.B[0]*self.A[1]-self.C[0]*self.B[1]-self.D[0]*self.C[1]-self.A[0]*self.D[1])
        return abs(S)
    def proverka(self):
        if super().side(self.B,self.D)==super().side(self.A,self.C) and (super().side(self.A,self.B) != super().side(self.C,self.B) or 
                                                                         super().side(self.A,self.B) != super().side(self.C,self.D) or 
                                                                         super().side(self.A,self.B) != super().side(self.A,self.D)):
            print('Фигура - равнобедренная трапеция')
        else:
            print('Фигура - неравнобедренная трапеция')
            pass

        
A = input('Введите координаты точки А через запятую. A  ')
B = input('Введите координаты точки B через запятую. B  ')
C = input('Введите координаты точки C через запятую. C  ')
D = input('Введите координаты точки C через запятую. D  ')
qd = quadrangle(A, B, C,D)
print('S = ', qd.square())
print('P = ', qd.perimeter())
qd.proverka()
l = input('Введите сторону, которую хотите найти  ')
if l == 'AB' or l == 'BA':
    print('AB = ',qd.side(qd.A,qd.B))
if l == 'BC' or l == 'CB':
    print('BC = ',qd.side(qd.B,qd.C))
if l == 'CD' or l == 'DC':
    print('CD = ',qd.side(qd.D,qd.C))
if l == 'AD' or l == 'DA':
    print('AD = ',qd.side(qd.D,qd.A))    
        
    
