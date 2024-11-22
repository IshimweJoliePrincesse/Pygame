int ledPin = 13;  // Pin connected to the LED

void setup() {
  // Initialize serial communication at 9600 baud
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT); // Set LED pin as output
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the incoming data

    if (command == '1') {
      digitalWrite(ledPin, HIGH); // Turn the LED on
    } else if (command == '0') {
      digitalWrite(ledPin, LOW);  // Turn the LED off
    }
  }
}
