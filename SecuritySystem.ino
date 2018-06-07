
void setup() {
  // put your setup code here, to run once:
  pinMode(8, OUTPUT);
  pinMode(7, INPUT);
  Serial.begin(9600);
  Serial.println("test");
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(8, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(200);                       // wait for a second
  //Serial.println("ON");
  digitalWrite(8, LOW);    // turn the LED off by making the voltage LOW
  delay(200);
  //Serial.println("OFF");
  
  //int val = digitalRead(7);   // read the input pin
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);

}
