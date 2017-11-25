#include <Servo.h>

Servo bottom;
Servo right;
Servo left;

int incomingByte = 0;   // for incoming serial data
char in = 'n';
char touch = 'n';


int aprintf(char *str, ...) {
  int i, j, count = 0;

  va_list argv;
  va_start(argv, str);
  for(i = 0, j = 0; str[i] != '\0'; i++) {
    if (str[i] == '%') {
      count++;

      Serial.write(reinterpret_cast<const uint8_t*>(str+j), i-j);

      switch (str[++i]) {
        case 'd': Serial.print(va_arg(argv, int));
          break;
        case 'l': Serial.print(va_arg(argv, long));
          break;
        case 'f': Serial.print(va_arg(argv, double));
          break;
        case 'c': Serial.print((char) va_arg(argv, int));
          break;
        case 's': Serial.print(va_arg(argv, char *));
          break;
        case '%': Serial.print("%");
          break;
        default:;
      };

      j = i+1;
    }
  };
  va_end(argv);

  if(i > j) {
    Serial.write(reinterpret_cast<const uint8_t*>(str+j), i-j);
  }

  return count;
}

//AF1AT1AF2AT2AF3AT3AF4AT4AF5AT5AF6AT6AF7AT7AF8AT8AF9AT9AF0AT0AF5

//BF1BT1BF2BT2BF3BT3BF4BT4BF5BT5BF6BT6BF7BT7BF8BT8BF9BT9BF0BT0BF5

//CF1CT1CF2CT2CF3CT3CF4CT4CF5CT5CF6CT6CF7CT7CF8CT8CF9CT9CF0CT0CF5

void pressNumber(int X, int Y, int Z, bool tocar){
  if (tocar==false)
    left.write(Z);
  right.write(X);
  delay(1000);
  bottom.write(Y);
  delay(1000);
  if(tocar)
      left.write(Z);   
  delay(1000);
}


void setup() {
  Serial.begin(9600);

  left.attach(9);
  bottom.attach(10);
  right.attach(11);

}

void loop() {
  if (Serial.available() > 0) {
    // read the incoming byte:
    String touch = Serial.readString();
    int X= touch.substring(2,5).toInt();
    int Y= touch.substring(6,9).toInt();
    int Z= touch.substring(10,12).toInt();
    String tocar= touch.substring(0,1);
    if (tocar == "T"){
      pressNumber( X, Y,Z, true);
    }
    else if (tocar == "F"){
      pressNumber( X, Y, Z,false);
    }
  }
  delay(25);
}
