#define OUTPUT_VOLTAGE A0
#define SOLAR_PANEL_VOLTAGE A1
#define BATTERY_VOTAGE A2
#define CAPACITOR_VOTAGE A3

#define VCC_VOLTAGE_MV 4990.0

void setup() {
  Serial.begin(9600);
}

double countsToMilliVolts(int counts) {
  return counts * (VCC_VOLTAGE_MV / 1023.0);
}

double readAverage(int pin) {
  double s = 0;
  for (int i = 0; i < 3; i++) {
    s += analogRead(pin);
    delay(1);
  }
  return s / 3.0;
}

void loop() {
  double outVoltage = countsToMilliVolts(readAverage(OUTPUT_VOLTAGE));
  double solarVoltage = countsToMilliVolts(readAverage(SOLAR_PANEL_VOLTAGE));
  double batteryVoltage = countsToMilliVolts(readAverage(BATTERY_VOTAGE));
  Serial.println(String(outVoltage) + ',' + solarVoltage + ',' + batteryVoltage);
  delay(50);
}
