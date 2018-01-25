#include <wiringPi.h>
#include <stdio.h>

#define TrackSensorPin 0
#define LedPin 1

int main(void){

	//when initialize wiring failed, print message to the screen
	if (wiringPiSetup() == -1){
		printf("setup wiring Pi failed!");
		return 1;
	}

	//when initialize wiring successful, print message to screen
//	printf("Linker Ledpin: GPIO %d(wiringPipin)/n",LedPin); 

	pinMode(TrackSensorPin, INPUT);
	pinMode(LedPin, OUTPUT);

	while(1){
		if(digitalRead(TrackSensorPin)== LOW) {
			printf("Black line is detected\n");
			digitalWrite(LedPin, LOW);
			delay(100);
			digitalWrite(LedPin, HIGH);
			
		}
		else{
			printf("White line is detected\n");
			delay(100);
		}
	}

	return 0;

}

