#include <LiquidCrystal_I2C.h>
#include <Wire.h>

#define LCD_ADD 0x27
#define LCD_COL 16
#define LCD_ROW 2

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
  lcd.clear();
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Hello");
  delay(1000);
}
