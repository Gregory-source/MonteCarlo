# The car is controlled by artificial intelligence. Suddenly, the control system failed
# and the car randomly selects the driving direction at each crossroad
# The car starts at point (0,0) and drives through a certain predetermined number of crossroads
# What is the most expected distance from the end point to the start point (Euclidean)?
import turtle
import os
# dodajemy obrazki aut ustawionych w roznych kierunkach:
car_left = r"./images/car_left.gif"
car_right = r"./images/car_right.gif"
car_up = r"./images/car_up.gif"
car_down = r"./images/car_down.gif"

# tworzymy slownik kierunkow
car_direction = {0: car_right, 90: car_up, 180: car_left,
                 270: car_down}  # 0stopni - w prawo, 90 - do gory, 180 -lewo, 270 - w dol
win = turtle.Screen()
for car in car_direction:
    win.addshape(car_direction[car])  # dodajemy nowe ksztalty do turtle.Screen()

class Simulation:
    def __init__(self,trasy):
        self.jednostka = 100  # wymiary pojedynczego kwadratowego pola kraty
        self.car_direction = car_direction
        self.rysuj_ulice()
        self.trasy = trasy
        self.bladz()

    def rysuj_ulice(self):
        s = turtle.Turtle()  # rysuje ulice miasta
        s.color("green")
        s.width(2)
        s.penup()
        s.speed(12)
        a = round(400 / self.jednostka)
        for i in range(-a, a + 1):  # rysujemy ulice wschód - zachód 1600 x 800 wymiary miasta
            s.goto(-800, self.jednostka * i)
            s.pendown()
            s.forward(1600)
            s.penup()

        s.right(90)  # zmieniamy kierunek na pionowy
        a = round(800 / self.jednostka)
        for i in range(-a, a + 1):  # rysujemy ulice północ - południe
            s.goto(self.jednostka * i, 400)
            s.pendown()
            s.forward(1600)
            s.penup()

        s.goto(0, 0)  # rysujemy srodek ukladu wspolrzednych
        s.color("#008800")
        s.shape("circle")
        s.width(3)

    def rysuj_zasieg(self, oczekiwana):
        t = turtle.Turtle()
        t.penup()
        t.color("#880000")
        t.width(3)
        promien = oczekiwana * self.jednostka
        t.pendown()
        t.goto(0,-promien)
        t.circle(promien)
        t.speed(5)

    def ustaw_auto(self, kierunek):
        t = turtle.Turtle()
        t.penup()
        t.goto(0, 0)
        t.color("")
        t.shape(self.car_direction[kierunek])
        t.speed(9)
        return t

    def bladz(self):  # realizuje bladzenie zgodnie z lista tras wylosowanych przez model
        for trasa in self.trasy:
            t = self.ustaw_auto(trasa[0])
            t.pendown()
            kat = 0
            for kierunek in trasa:  # kierowca przejezdza w sposob losowy przez kolejne skrzyzowania
                kat = (kat + kierunek) % 360
                t.shape(self.car_direction[kat])
                t.setheading(kat)
                t.forward(self.jednostka)