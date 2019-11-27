void setup() {
	Serial.begin(115200);
}

void loop() {
	int analog0 = analogRead(A0);
	int analog1 = analogRead(A1);
	int analog2 = analogRead(A2);
	int analog3 = analogRead(A3);
	int analog4 = analogRead(A4);
	int analog5 = analogRead(A5);
	Serial.print(analog0);Serial.print(",");
	Serial.print(analog1);Serial.print(",");
	Serial.print(analog2);Serial.print(",");
	Serial.print(analog3);Serial.print(",");
	Serial.print(analog4);Serial.print(",");
	Serial.println();
}
