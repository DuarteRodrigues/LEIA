#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DS1302RTC.h>
#include <Time.h>
#include <TimeLib.h>
#include <string.h>

#define LCD_ADDR 0x3f
#define LCD_COLUMNS 16
#define LCD_ROWS 2

#define RTC_RST 4
#define RTC_DAT 3
#define RTC_CLK 2

// Init the DS1302
// Set pins:  RST, DAT, CLK
DS1302RTC RTC(RTC_RST, RTC_DAT, RTC_CLK);

// Init the LCD
LiquidCrystal_I2C lcd(LCD_ADDR, LCD_COLUMNS, LCD_ROWS);

const static char* WeekDays[] =
{
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thrusday",
  "Friday",
  "Saturday",
  "Sunday"
};

void setup() {
  lcd.init();       // initialize the lcd
  lcd.backlight();  // open the backlight

  // Clock runing? If not set time.
  //  RTC.haltRTC(true); true - running
  if (RTC.haltRTC()) {
    lcd.print("Clock stopped!");
    //setTime(22, 29, 00, 02, 03, 2019);
    //setTime(hour,minute,second,day,month,year);
    RTC.set(now());

    // Automatically sets the time when the code is compiled
    AutoSetBuildTime();
    RTC.haltRTC(false);
  } else
    lcd.print("Clock working.");

  delay(500);

  lcd.setCursor(0, 1);
  if (RTC.writeEN())
    lcd.print("Write allowed.");
  else
    lcd.print("Write protected.");

  delay(2000);

  // Setup time library
  lcd.clear();
  lcd.print("RTC Sync");
  setSyncProvider(RTC.get);  // the function to get the time from the RTC

  if (timeStatus() == timeSet)
    lcd.print(" Ok!");
  else
    lcd.print(" FAIL!");

  delay(2000);

  lcd.clear();
}

void loop() {
  static int sday = 0;  // Saved day number for change check

  // Display time centered on the upper line
  lcd.setCursor(0, 1);
  print2digits(hour());
  lcd.print(":");
  print2digits(minute());


  if (sday != day()) {
    // Display abbreviated Day-of-Week in the lower left corner
    lcd.setCursor(0, 0);
    lcd.print(weekday());

    // Display date in the lower right corner
    lcd.setCursor(5, 1);
    lcd.print(" ");
    print2digits(day());
    lcd.print("/");
    print2digits(month());
    lcd.print("/");
    lcd.print(year());
  }
  // Warning!
  if (timeStatus() != timeSet) {
    lcd.setCursor(0, 1);
    lcd.print(F("RTC ERROR: SYNC!"));
  }

  // Save day number
  sday = day();

  // Wait small time before repeating :)
  delay(100);
}


// Automatically sets the time when the code is compiled //
void AutoSetBuildTime() {
  char input[] = __TIME__ " " __DATE__;  //Input
  String H, M, S, D, N, Y;               // Output
  const char del[] = " :,";              //Delimiters
  char *token;
  int i = 0;
  char *array[6];  // Number of variables to save
  int Hi, Mi, Si, Di, Ni, Yi;

  token = strtok(input, del);
  while (token != NULL)  //splitted
  {
    array[i++] = token;
    token = strtok(NULL, del);
  }
  H = array[0];
  Hi = H.toInt();
  M = array[1];
  Mi = M.toInt();
  S = array[2];
  Si = S.toInt();
  D = array[4];
  Di = D.toInt();
  N = array[3];  // month to number
  if (N == "Jan")
    Ni = 1;
  else if (N == "Feb")
    Ni = 2;
  else if (N == "Mar")
    Ni = 3;
  else if (N == "Apr")
    Ni = 4;
  else if (N == "May")
    Ni = 5;
  else if (N == "Jun")
    Ni = 6;
  else if (N == "Jul")
    Ni = 7;
  else if (N == "Aug")
    Ni = 8;
  else if (N == "Sep")
    Ni = 9;
  else if (N == "Oct")
    Ni = 10;
  else if (N == "Nov")
    Ni = 11;
  else if (N = "Dec")
    Ni = 12;
  Y = array[5];
  Yi = Y.toInt();
  setTime(Hi, Mi, Si, Di, Ni, Yi);
  RTC.set(now());
}


//Prints alway two digits to display (00)
void print2digits(int number) {
  if (number >= 0 && number < 10) {
    lcd.write('0');
  }
  lcd.print(number);
}