Author: Jonathan Franche

This project is for a four-wheeled rover powered by a raspberry pi controlled over LAN by any device that can access a web page. 

The python file uses the bottle module to serve an HTML file where inputs can be received from the user. The specific inputs the user sends determines the direction in which the rover will move (Forward, Left, Right, Stop, Reverse). This program also uses the PiMotor module from SB components who are teh manufacturer of the motor shield to interface with the four motors.

Special thanks to Simon Monk who's book, Programming the Raspberry Pi: 2nd Edition, was heavily referenced in order to complete this project. 
