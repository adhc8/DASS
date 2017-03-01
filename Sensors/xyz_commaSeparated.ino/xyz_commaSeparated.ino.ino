#include <SPI.h>
#include <Pixy.h>

Pixy pixy;


float pulse_width;


void setup() {
 Serial.begin(9600);

 pixy.init();

 pinMode(2, OUTPUT); // Set pin 2 as trigger pin
  pinMode(3, INPUT); // Set pin 3 as monitor pin
  digitalWrite(2, LOW); // Set trigger LOW for continuous read

}

void loop() 
{
 if(pixy.getBlocks())
 {
   
    if(pixy.blocks[0].signature == 1);
      {
       // Serial.print("X-axis:");
       // Serial.print("\t");
        Serial.print(pixy.blocks[0].x);
        Serial.print(",");
       
       //Serial.print("\t");
       // Serial.print(" Y-axis:");
     
       
       // Serial.print("\t");
        Serial.print(pixy.blocks[0].y);
         Serial.print(",");
      }
            else
      {
        Serial.print(" , ,");
      }}
       
  
      
  //if(pulse_width != 0){ // If we get a reading that isn't zero, let's print it
      //  pulse_width = pulse_width/1000; // 10usec = 1 cm of distance for LIDAR-Lite //JUST CHANGED THIS NOW THE OUTPUT IS IN METERS, BEOFRE VALUE WAS pulse_widt/10
  //delay(20);
  // Serial.println(pulse_width,3); // Print the distance
  //}
  
  
 }
 pulse_width = pulseIn(3, HIGH); // Count how long the pulse is high in microseconds
 if(pulse_width != 0){ // If we get a reading that isn't zero, let's print it
        pulse_width = pulse_width/1000; // 10usec = 1 cm of distance for LIDAR-Lite //JUST CHANGED THIS NOW THE OUTPUT IS IN METERS, BEOFRE VALUE WAS pulse_widt/10
  //delay(20)
  Serial.print(pulse_width,3); // Print the distance
        }
if(pixy.getBlocks())
{
        if(pixy.blocks[0].signature == 1);
   {
         Serial.print(",");
          Serial.print(pixy.blocks[0].width);
           Serial.print(",");
          Serial.println(pixy.blocks[0].height);
    
       // Serial.println("\t");

       
      }
      else
      {
        Serial.println(" , ,");
      }}
        delay(1000); //Delay so we don't overload the serial port
//
}
