# Codrone-Motion-Control
Using an MPU6050 gyroscope connected to a Raspberry assembled on a glove to control a Codrone quadrocopter

<img src="schematic.png" width="400">

The schematic for the electronics with the MPU6050.  
SCL (Serial Clock) is used for the clock pulse in the I2C connection.  
SDA is for the data connection.  

<img src="Early Prototype.jpg" width="400">

An early protoype with the MPU6050 taped to the top of the back of the hand, with the bluetooth board wrapped around and dangling off the Raspberry Pi.

<img src="Final product.jpg" width="400">

The final product showing various improvements, not least of which is an actual glove, easy acces to the takeoff/land button on the side, and a more compact design with the bluetooth board on top of the Raspberry Pi.

<img src="dronevideo.gif" width="400">

The drone in action. The throttle is limited to protect the drone from collisions.
