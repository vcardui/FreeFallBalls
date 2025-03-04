# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2024, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: March 3rd, 2025
# | Last update..: March 3rd, 2025
# | WhatIs.......: FreeFallBalls - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# List comprehension for decimal step value for range(): https://stackoverflow.com/a/477513

# ------------------------- Libraries -------------------------
from turtle import Turtle, Screen # Turtle GUI

# ------------------------- Variables -------------------------
screen = Screen()
screen.setup(width=1000, height=1000)

STEP = 0.01 # s
GRAVITY = 9.81 # m/s (Earth)

deltaDistance = 0
separationTime = 0
separationDistance = 0

# -------------------------- Classes --------------------------
class Ball:
    def __init__(self, ballName):
        self.state = "🟡on baseline"
        self.name = ballName

        self.y_velocity = 0 # m/s
        self.y_distance = 0 # m -> distance from baseline
        self.time = 0 # s -> time elapsed since it was thrown

        self.initial_y = 0 # m
        self.initial_Vy = 0 # m/s

    def status(self):
        self.updateStatus()

        print(f"""{self.name}: {self.state}
     Vy = {round(self.y_velocity, 4)} m/s
      y = {round(self.y_distance, 4)} m
      t = {round(self.time, 4)} s""")

    def throw(self):
        self.state = "🟢falling"

    def updateStatus(self):
        self.y_velocity = self.initial_Vy - (abs(GRAVITY) * self.time)
        self.y_distance = self.initial_y + (self.initial_Vy * self.time) - (0.5 * abs(GRAVITY) * (self.time**2))

# ------------------------- Functions -------------------------

# -------------------------- Objects --------------------------
ball1 = Ball("Ball 1")
ball2 = Ball("Ball 2")

# --------------------------- Code ----------------------------
# Set plotter
plotter = Turtle()
plotter.hideturtle()

timeLapse = (x * STEP for x in range(0, 500))
for t in timeLapse:
    print(f"\n----- t = {round(t, 4)} -----")
    if ball1.state == "🟢falling":
        ball1.time += STEP

    if ball2.state == "🟢falling":
        ball2.time += STEP

    if t == 0:
        ball1.throw()
    elif t == 1:
        ball2.throw()

    ball1.status()
    ball2.status()

    deltaDistance = round(abs(ball1.y_distance) - abs(ball2.y_distance), 4)
    print(f"ΔDistance: {deltaDistance} m")

    if deltaDistance >= 10 and separationDistance == 0:
        print("------> Separation distance reached <------")
        separationTime = round(t, 4)
        separationDistance = deltaDistance
        break

    # Plot the coordinates
    plotter.penup()
    # Ball 1
    plotter.setposition(x=-50, y=((ball1.y_distance * 50) + 450))
    plotter.dot(5, "LightSeaGreen")
    # Ball 2
    plotter.setposition(x=50, y=((ball2.y_distance * 50) + 450))
    plotter.dot(5, "DarkOrchid")
    plotter.pendown()

print(
    f"""
    +------------------------------+---------------+
    | Required time for the bodies | t = {separationTime} s    |
    | to be at a distance of 10 m  | d = {separationDistance} m |
    +------------------------------+---------------+
    """
)

# Stop window from exiting
screen.mainloop()