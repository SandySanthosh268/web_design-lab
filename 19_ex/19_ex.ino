
const int trigPin = 9;
const int echoPin = 10;


const int ledPin = 13;


const int distanceThreshold = 10;

void setup() {
  
  Serial.begin(9600);

 
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
 
  long duration;
  int distance;

 
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  
  duration = pulseIn(echoPin, HIGH);

 
  distance = duration * 0.034 / 2;

  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  
  if (distance <= distanceThreshold) {
    digitalWrite(ledPin, HIGH); 
    delay(500);                
    digitalWrite(ledPin, LOW);  
    delay(500);                
  } else {
    digitalWrite(ledPin, LOW); 
  }

  delay(100); 
}
