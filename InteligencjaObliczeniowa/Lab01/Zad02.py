from math import sin, cos, sqrt, radians, degrees
from random import randint
from numpy import linspace
import matplotlib.pyplot as plt


def draw_trajectory(shot, V0, h, g):
    Vx = V0 * cos(shot)
    Vy = V0 * sin(shot)
    T = (Vy + sqrt(Vy**2 + 2 * g * h)) / g # Time of flight

    t = linspace(0, T, 200)

    x = Vx * t
    y = h + Vy * t - 0.5 * g * t**2

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=f"alpha = {degrees(shot)}")
    plt.xlim(0, 340)
    plt.title("Jak leci kamyczek")
    plt.xlabel("O tak daleko")
    plt.ylabel("O tak wysoko")
    plt.legend()
    plt.show()

V0 = 50
h = 100
g = 10

shoot = lambda alpha : V0 * cos(alpha) * ((V0 * sin(alpha) + sqrt((V0 * sin(alpha))**2 + 2 * g * h))/g)

target = randint(50, 340)

print(f"You're trying to shoot target {target:.2f}m away")

target_hit = False
counter = 0
while not target_hit:
    counter += 1
    print("Give me an angle ")
    aim = radians(int(input()))
    shot = shoot(aim)
    if shot >= target - 5 and shot <= target + 5:
        print(f"You hit! It took {counter} tries")
        target_hit = True
        draw_trajectory(aim, V0, h, g)

    else:
        print(f"You missed, Your shot landed at {shot:.2f}m")
