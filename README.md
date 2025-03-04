# 🥎 Free Fall Balls

Simulation of free fall of two balls

## 🎯 Objective

Two bodies begin a free fall, starting from rest and at the same height, but with a time interval of 1 second apart. How long after the first body begins to fall will they be separated by a distance of 10 meters?

![FreeFallBalls_explanation](https://github.com/user-attachments/assets/be3f0edd-8566-437e-912d-510073675f3e)


### Working project demo

(Start of iteration)
<img width="450" alt="FreeFallBalls_calculationStart" src="https://github.com/user-attachments/assets/46a8d6b9-8c45-4f80-a2a7-b2b2826be6f8" />

(End of iteration)
<img width="450" alt="FreeFallBalls_calculationEnd" src="https://github.com/user-attachments/assets/ba56b649-963d-458d-9a0e-c328e73ae0c8" />

Balls position graph
<img width="700" alt="FreeFallBalls_Graph" src="https://github.com/user-attachments/assets/cd9afa3e-7229-4ae9-aefd-32ca586b1a9c" />

## 🙌 Project Personal Milestones

- Understood the relationship between time, the y component of the velocity vector

## 💡 Inspiration for creating this project

This program was required as a homework for proving the accuracy of the problem mathematical solution provided at my Mechanics class. 

## 👀 About the project

The program calculates the time at which the balls are at a distance of 10 meters between each other by calculating both ball’s positions every 0.01 seconds, which was calculated by:

$V_{y} = V_{0y} - |g|t^2$

Where:

$V_{y}$: The y component of the velocity vector [$\frac{m}{s}$]

$V_{0y}$: The starting velocity of the y component [$\frac{m}{s}$]

$g$: Gravity = 9.81 [$\frac{m}{s^{2}}$]

$t$: Time [s]

$y = y_{0} + V_{0y}t - \frac{1}{2}|g|t^2$

Where:

$y$: The ball’s current position [m]

$y_{0}$: The ball’s starting position [m]

$V_{0y}$: The starting velocity of the y component [$\frac{m}{s}$

$t$: Time [s]

$g$: Gravity = 9.81 [$\frac{m}{s^{2}}$]
