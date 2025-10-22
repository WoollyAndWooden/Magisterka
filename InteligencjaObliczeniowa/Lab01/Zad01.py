from sys import argv
import datetime
from math import pi, sin

def biorythm_state(physical, emotional, intelectual):
    if physical > -0.5 and physical < 0.5:
        physical_state = "average"
    elif physical < -0.5:
        physical_state = "weak"
    else:
        physical_state = "ripped"
    if emotional > -0.5 and emotional < 0.5:
        emotional_state = "average"
    elif emotional < -0.5:
        emotional_state = "down"
    else:
        emotional_state = "on peak"
    if intelectual > -0.5 and intelectual < 0.5:
        intelectual_state = "average"
    elif intelectual < -0.5:
        intelectual_state = "dumb"
    else:
        intelectual_state = "genius"

    print(f"Physically, You're {physical_state}. Your mood is {emotional_state}, and on intelectual side You're {intelectual_state}")

birthday = datetime.date(int(argv[2]), int(argv[3]), int(argv[4]))
today = datetime.datetime.now()
days_passed = (datetime.date(today.year, today.month, today.day) - birthday).days
print(days_passed)

physical = lambda x : sin(((2*pi)/23)*x)
emotional = lambda x : sin(((2*pi)/28)*x)
intelectual = lambda x : sin(((2*pi)/33)*x)


print(f"Hi {argv[0]}, Today ")
biorythm_state(physical(days_passed), emotional(days_passed), intelectual(days_passed))
print("And tomorrow ")
biorythm_state(physical(days_passed+1), emotional(days_passed+1), intelectual(days_passed+1))
