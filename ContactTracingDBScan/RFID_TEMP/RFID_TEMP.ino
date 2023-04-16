#include <SPI.h>
#include <MFRC522.h>
 
#define SS_PIN 10
#define RST_PIN 9
#include <Adafruit_MLX90614.h>
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

const int GreenLED = 1;
const int RedLED = 2;
const int buzzer = 3;

Adafruit_MLX90614 mlx = Adafruit_MLX90614();
 
void setup() 
{
  Serial.begin(9600);   // Initiate a serial communication
  while (!Serial);
  pinMode(13, OUTPUT);
  
  pinMode(GreenLED, OUTPUT);
  pinMode(RedLED, OUTPUT);
  pinMode(buzzer, OUTPUT);

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
}
void loop() 
{  
  char RxedByte = 0;
  if (Serial.available() > 0){
    RxedByte = Serial.read(); 
    //Serial.print(RxedByte);
    switch(RxedByte)
      {
        case 'A':  
          temp();
          break;
        case 'B': //your code
          rfid();
          break;
      }//end of switch()

  }
  delay(1000);
} 


void rfid()
{
  String content= " ";
  delay(1000);
    // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
    content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
    content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  content.toUpperCase();
  Serial.println(content); 
}
void temp(){
  delay(1000);
  int temp = mlx.readObjectTempC();
  Serial.print(temp); Serial.println(" C");
  if (temp <= 37.5)
  {
   digitalWrite(GreenLED, HIGH); 
   delay(2000);
   digitalWrite(GreenLED, LOW); 
  }
  else
  {
   digitalWrite(RedLED, HIGH);
   delay(500);
   for (int i = 0; i <6; i ++)
   {
      tone(buzzer, 1000); // Send 1KHz sound signal...
      delay(500);        // ...for 1 sec
      noTone(buzzer);     // Stop sound...
      delay(500);        // ...for 1sec
   }
   delay(500);
   digitalWrite(RedLED, LOW); 
  }
}
