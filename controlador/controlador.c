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

void pressNumber(char layout, int num, bool tocar){
  if(layout == 'A'){
    switch(num){
      case 0:
        right.write(137);
        bottom.write(65);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 1:
        right.write(143);
        bottom.write(100);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 2:
        right.write(147);
        bottom.write(80);
        if(tocar)
          left.write(67);
        else
          left.write(80);
        break;
      case 3:
        right.write(145);
        bottom.write(60);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 4:
        right.write(140);
        bottom.write(100);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 5:
        right.write(142);
        bottom.write(80);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 6:
        right.write(140);
        bottom.write(65);
        if(tocar)
          left.write(68);
        else
          left.write(80);
        break;
      case 7:
        right.write(135);
        bottom.write(100);
        if(tocar)
          left.write(68);
        else
          left.write(80);
        break;
      case 8:
        right.write(135);
        bottom.write(85);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 9:
        right.write(137);
        bottom.write(77);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
    }
  }
  else if(layout == 'B'){
    switch(num){
      case 0:
        right.write(130);
        bottom.write(65);
        if(tocar)
          left.write(75);
        else
          left.write(65);
        break;
      case 1:
        right.write(142);
        bottom.write(100);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 2:
        right.write(145);
        bottom.write(80);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 3:
        right.write(147);
        bottom.write(60);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 4:
        right.write(135);
        bottom.write(100);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 5:
        right.write(137);
        bottom.write(80);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 6:
        right.write(137);
        bottom.write(65);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 7:
        right.write(128);
        bottom.write(100);
        if(tocar)
          left.write(60);
        else
          left.write(70);
        break;
      case 8:
        right.write(133);
        bottom.write(85);
        if(tocar)
          left.write(60);
        else
          left.write(70);
        break;
      case 9:
        right.write(133);
        bottom.write(75);
        if(tocar)
          left.write(60);
        else
          left.write(75);
        break;
    }
  }
  else if(layout == 'C'){
    switch(num){
      case 0:
        right.write(127);
        bottom.write(67);
        if(tocar)
          left.write(58);
        else
          left.write(70);
        break;
      case 1:
        right.write(142);
        bottom.write(100);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 2:
        right.write(145);
        bottom.write(80);
        if(tocar)
          left.write(70);
        else
          left.write(80);
        break;
      case 3:
        right.write(145);
        bottom.write(60);
        if(tocar)
          left.write(65);
        else
          left.write(80);
        break;
      case 4:
        right.write(135);
        bottom.write(100);
        if(tocar)
          left.write(65);
        else
          left.write(80);
        break;
      case 5:
        right.write(137);
        bottom.write(80);
        if(tocar)
          left.write(62);
        else
          left.write(80);
        break;
      case 6:
        right.write(135);
        bottom.write(65);
        if(tocar)
          left.write(61);
        else
          left.write(75);
        break;
      case 7:
        right.write(125);
        bottom.write(97);
        if(tocar)
          left.write(58);
        else
          left.write(70);
        break;
      case 8:
        right.write(127);
        bottom.write(85);
        if(tocar)
          left.write(56);
        else
          left.write(70);
        break;
      case 9:
        right.write(130);
        bottom.write(75);
        if(tocar)
          left.write(60);
        else
          left.write(70);
        break;
    }
  }  
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
    in = Serial.read();
    touch = Serial.read();
    incomingByte = Serial.parseInt();


    if (touch == 'T'){
      pressNumber(in, incomingByte, true);
    }
    else if (touch == 'F'){
      pressNumber(in, incomingByte, false);
    }
  }
  delay(25);
}
