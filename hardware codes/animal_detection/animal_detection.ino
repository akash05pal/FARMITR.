int ledPin = 5;                            //LED PIN.
int buzzerPin = 6;                          //BUZZER INPUT PIN.
int pirPin = 7;                            //MOTION SENSOR INPUT PIN.
int sensorValue = LOW;    
int relayPin = 2;                  //DEFAULT SENSOR STATE.

void setup() {                              //INITIAL SETTINGS/ASSIGNMETN.
  pinMode(buzzerPin, OUTPUT);               //SET BUZZER AS OUTPUT.
  pinMode(ledPin, OUTPUT);                  //SET LED AS OUTPUT.
  pinMode(pirPin, INPUT); 
  pinMode(relayPin, OUTPUT);     
  Serial.begin(9600);             //SET PIR AS INPUT.
}
void loop() {                               //COMMAND TO BE REPEATED.
  sensorValue = digitalRead(pirPin);  
  Serial.println(sensorValue);
  digitalWrite(relayPin, LOW);

        //READ PIR INPUT PIN.
  if ( sensorValue == HIGH) {  
    digitalWrite(relayPin, HIGH);             //IF MOTION IS DETECTED.
    tone(buzzerPin, 1200);                  //BUZZ THE BUZZER. 
    digitalWrite(ledPin, HIGH);             //ON LED.
    delay(50);                             //TIME DIFFERENCE BETWEEN HIGH(ON)& LOW(OFF).                      .
    digitalWrite(ledPin, LOW);              //OFF LED.
    delay(50);   
                          //TIME DIFFERENCE BETWEEN HIGH(ON)& LOW(OFF).
  }
  else {                                    //IF NO MOTION IS DETECTED.
    noTone(buzzerPin);                      //SILENT THE BUZZER.
    digitalWrite(ledPin, LOW);              //OFF LED.
  }
  
}
