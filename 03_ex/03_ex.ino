#define BLYNK_TEMPLATE_ID "YourTemplateID"
#define BLYNK_DEVICE_NAME "SmartLighting"
#define BLYNK_AUTH_TOKEN "YourAuthToken"

#include <BlynkSimpleEsp8266.h>


const int LDRPin = A0;
const int PIRPin = 3;
const int RelayPin = 9;
const int LEDPin = 13;

const int LightThreshold = 500;


char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "YourWiFiSSID";
char pass[] = "YourWiFiPassword";


bool lightState = false;

void setup() {
  
  Serial.begin(9600);

  
  pinMode(LDRPin, INPUT);
  pinMode(PIRPin, INPUT);
  pinMode(RelayPin, OUTPUT);
  pinMode(LEDPin, OUTPUT);


  Blynk.begin(auth, ssid, pass);
}

void loop() {

  Blynk.run();


  int lightLevel = analogRead(LDRPin);
  int motionDetected = digitalRead(PIRPin);

  Serial.print("Light Level: ");
  Serial.println(lightLevel);
  Serial.print("Motion Detected: ");
  Serial.println(motionDetected);

  if (lightLevel < LightThreshold && motionDetected == HIGH) {
    digitalWrite(RelayPin, HIGH); 
    digitalWrite(LEDPin, HIGH);  
    lightState = true;
  } else {
    digitalWrite(RelayPin, LOW); 
    digitalWrite(LEDPin, LOW);   
    lightState = false;
  }

  delay(500);
}


BLYNK_WRITE(V1) {
  int manualControl = param.asInt();
  if (manualControl) {
    digitalWrite(RelayPin, HIGH); 
    digitalWrite(LEDPin, HIGH);  
    lightState = true;
  } else {
    digitalWrite(RelayPin, LOW); 
    digitalWrite(LEDPin, LOW);  
    lightState = false;
  }
}
