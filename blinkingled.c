
#include <wiringPi.h>
#include <stdio.h>
#define LedPin 0

int main(void){

	//when initialize wiring failed, print message to the screen
	if (wiringPiSetup() == -1){
		printf("setup wiring Pi failed!");
		return 1;
	}

	//when initialize wiring successful, print message to screen
	printf("Linker Ledpin: GPIO %d(wiringPipin)/n",LedPin); 

	pinMode(LedPin, OUTPUT);
	while(1){
		digitalWrite(LedPin, LOW); //led on
		delay(500);
		digitalWrite(LedPin, HIGH); //led off
		delay (500);
	}

	return 0;

}

