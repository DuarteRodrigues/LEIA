#include <LiquidCrystal_I2C.h>
#include <virtuabotixRTC.h>

#define LCD_ADDR 0x3f
#define LCD_COLUMNS 16
#define LCD_ROWS 2

// RTC está conectado às portas digitais 2, 3 e 4
#define RTC_RST 2
#define RTC_DAT 3
#define RTC_CLK 4

// LED está conectado à porta digital 6
#define LED_PIN 6

//TMP 36gz está conectado à porta analógica A0
const int sensorPin = A0;  

LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLUMNS, LCD_ROWS);
virtuabotixRTC myRTC(RTC_CLK, RTC_DAT, RTC_RST);

const static char* WeekDays[] =
{
  "Segunda-Feira",
  "Terca-Feira",
  "Quarta-Feira",
  "Quinta-Feira",
  "Sexta-Feira",
  "Sabado",
  "Domingo"
};

void setup() {
  // put your setup code here, to run once:
  //Inicialização do Serial(Usado para a consola em termos de testes)
  //Serial.begin(9600);

  // Se quisermos inserir os dados da data e hora manualmente
  //myRTC.setDS1302Time(0, 43, 11, 5, 28, 6, 2024);

  //Definir o LED como output
  pinMode(LED_PIN, OUTPUT);

  // Inicialização do LCD
  lcd.init();
  lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Projeto Duarte");

  delay(2000);

  lcd.clear();
  myRTC.updateTime();
  lcd.setCursor(0, 0);
  lcd.print(WeekDays[myRTC.dayofweek - 1]);
  //Serial.print("Current Date/Time:");
  //Serial.print(myRTC.dayofweek);
  //Serial.print(" ");
  lcd.setCursor(0, 1);

  if (myRTC.dayofmonth < 10) lcd.print('0');
  lcd.print(myRTC.dayofmonth);
  lcd.print("/");
  //Serial.print(myRTC.dayofmonth);
  //Serial.print("/");

  if (myRTC.month < 10) lcd.print('0');
  lcd.print(myRTC.month);
  lcd.print("/");
  //Serial.print(myRTC.month);
  //Serial.print("/");
  if ((myRTC.year - 2000)  < 10) lcd.print('0');
  lcd.print(myRTC.year - 2000);
  //Serial.print(myRTC.year);
  //Serial.print(" \n");

  lcd.print("   ");
  
  if (myRTC.hours < 10) lcd.print('0');
  lcd.print(myRTC.hours);    // 00-23
  lcd.print(':');
  //Serial.print(myRTC.hours);
  //Serial.print(":");
  
  if (myRTC.minutes < 10) lcd.print('0');
  lcd.print(myRTC.minutes);
  //Serial.print(myRTC.minutes);
  //Serial.print(":");
  //Serial.print(myRTC.seconds);
  //Serial.print("\n");

  delay(2000);

  //  Guardar o valor do sinal analógico
  int sensorValue = analogRead(sensorPin);
  //Serial.print(sensorValue);
  //Serial.print("\n");

  // Verificar se o sensor está a enviar sinal (sinal analógio é muito baixo ou muito alto)
  if (sensorValue < 150 || sensorValue > 300){
    digitalWrite(LED_PIN, HIGH); // Ligar o LED
  } else {
    digitalWrite(LED_PIN, LOW);
  }
  
  // Converter a leitura analógica em temperatura (C)
  float Temperature = (sensorValue * (5.0 / 1023.0)- 0.5) * 100.0;

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Temperatura:");
  lcd.setCursor(0, 1);
  lcd.print(Temperature);
  lcd.print("C");
  
  delay(2000);
}
