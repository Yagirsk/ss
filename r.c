#define LR 4 // AIN2
#define LF 7 // AIN1
#define RF 9 // BIN1
#define RR 8 // BIN2
#define LS 5 // PWMA
#define RS 6 // PWMB
#define RLS A3 // R
#define CLS A2 // C
#define LLS A1 // L
#define RSS 90 // right motor standart speed
#define LSS 100 // left motor standart speed
int LT = 0; // left transmition
int RT = 0; // right transmition
unsigned long myTime;
unsigned long myTime1;
int coL=0;
int coR=0;
void setup() {
  myTime = millis();
  pinMode(LS, OUTPUT);
  pinMode(RS, OUTPUT);
  pinMode(LF, OUTPUT);
  pinMode(LR, OUTPUT);
  pinMode(RF, OUTPUT);
  pinMode(RR, OUTPUT);
  pinMode(CLS, INPUT);
  pinMode(RLS, INPUT);
  pinMode(LLS, INPUT);
}
void breakM()
{
  digitalWrite(LF, LOW);
  digitalWrite(LR, LOW);
  digitalWrite(RR, LOW);
  digitalWrite(RF, LOW);
  analogWrite(RS, 0);
  analogWrite(LS, 0);
  RT = 0;
  LT = 0;
}
void reverse()
{
  digitalWrite(LF, LOW);
  digitalWrite(LR, HIGH);
  digitalWrite(RR, HIGH);
  digitalWrite(RF, LOW);
  analogWrite(RS, 200);
  analogWrite(LS, 210);
  delay(500);
  analogWrite(RS, 0);
  analogWrite(LS, 0);
  if(rand()%2 == 1)
  {
    for(int i = 0; i < 250; i++)
    {
      if(digitalRead(LLS)==HIGH){
        digitalWrite(LR, HIGH);
        digitalWrite(LF, LOW);
        analogWrite(LS, 160);
        digitalWrite(RR, LOW);
        digitalWrite(RF, HIGH);
        analogWrite(RS, 150);
        delay(1);
      }
      else
      {
        digitalWrite(LR, LOW);
        digitalWrite(LF, HIGH);
        analogWrite(LS, 160);
        digitalWrite(RR, HIGH);
        digitalWrite(RF, LOW);
        analogWrite(RS, 150);
        delay(450);
        break;
      }
    }
  }
  else
  {
    for(int i = 0; i < 250; i++)
    {
      if(digitalRead(RLS)==HIGH){
        digitalWrite(LR, LOW);
        digitalWrite(LF, HIGH);
        analogWrite(LS, 160);
        digitalWrite(RR, HIGH);
        digitalWrite(RF, LOW);
        analogWrite(RS, 150);
        delay(1);
      }
      else
      {
        digitalWrite(LR, HIGH);
        digitalWrite(LF, LOW);
        analogWrite(LS, 160);
        digitalWrite(RR, LOW);
        digitalWrite(RF, HIGH);
        analogWrite(RS, 150);
        delay(450);
        break;
      }
    }
  }
}
void L_reverse()
{
  digitalWrite(LF, LOW);
  digitalWrite(LR, HIGH);
  digitalWrite(RR, HIGH);
  digitalWrite(RF, LOW);
  analogWrite(RS, 200);
  analogWrite(LS, 210);
  delay(500);
  analogWrite(RS, 0);
  analogWrite(LS, 0);
  for(int i = 0; i < 250; i++)
    {
      if(digitalRead(LLS)==HIGH){
        digitalWrite(LR, HIGH);
        digitalWrite(LF, LOW);
        analogWrite(LS, 160);
        digitalWrite(RR, LOW);
        digitalWrite(RF, HIGH);
        analogWrite(RS, 150);
        delay(1);
      }
      else
      {
        digitalWrite(LR, LOW);
        digitalWrite(LF, HIGH);
        analogWrite(LS, 160);
        digitalWrite(RR, HIGH);
        digitalWrite(RF, LOW);
        analogWrite(RS, 150);
        delay(450);
        break;
      }
    }
}
void R_reverse()
{
  digitalWrite(LF, LOW);
  digitalWrite(LR, HIGH);
  digitalWrite(RR, HIGH);
  digitalWrite(RF, LOW);
  analogWrite(RS, 200);
  analogWrite(LS, 210);
  delay(500);
  analogWrite(RS, 0);
  analogWrite(LS, 0);
  for(int i = 0; i < 250; i++)
    {
      if(digitalRead(RLS)==HIGH){
        digitalWrite(LR, LOW);
        digitalWrite(LF, HIGH);
        analogWrite(LS, 160);
        digitalWrite(RR, HIGH);
        digitalWrite(RF, LOW);
        analogWrite(RS, 150);
        delay(1);
      }
      else
      {
        digitalWrite(LR, HIGH);
        digitalWrite(LF, LOW);
        analogWrite(LS, 160);
        digitalWrite(RR, LOW);
        digitalWrite(RF, HIGH);
        analogWrite(RS, 150);
        delay(450);
        break;
      }
    }
}
void loop() {
  myTime1 = millis();
  if(digitalRead(CLS)==HIGH)
  {
    if(digitalRead(RLS)==HIGH && digitalRead(LLS)==HIGH)
    {
      if(LT>=RT)
      {
        RT = LT;
      }
      else
      {
        LT=RT;
      }
    }
    digitalWrite(LF, HIGH);
    digitalWrite(LR, LOW);
    digitalWrite(RR, LOW);
    digitalWrite(RF, HIGH);
    analogWrite(LS, LSS+20*LT);
    analogWrite(RS, RSS+20*RT);
    if(myTime1 - myTime >300 && RT < 7 && LT < 7 && digitalRead(RLS)==HIGH && digitalRead(LLS)==HIGH && digitalRead(CLS)==HIGH)
    {
      myTime = myTime1;
      RT++;
      LT++;
    }
  }
  else if (digitalRead(RLS)==LOW && digitalRead(LLS)==LOW && digitalRead(CLS)==LOW)
  {
    breakM();
    reverse();
  }
  else if (digitalRead(RLS)==HIGH && digitalRead(LLS)==LOW && digitalRead(CLS)==LOW)
  {
    breakM();
    R_reverse();
  }
  else if (digitalRead(RLS)==LOW && digitalRead(LLS)==HIGH && digitalRead(CLS)==LOW)
  {
    breakM();
    L_reverse();
  }
  else if (digitalRead(RLS)==LOW && digitalRead(LLS)==LOW && digitalRead(CLS)==HIGH)
  {
    breakM();
    reverse();
  }
  else if (digitalRead(RLS)==HIGH && digitalRead(LLS)==HIGH && digitalRead(CLS)==LOW)
  {
    breakM();
    reverse();
  }
  if (digitalRead(RLS)==LOW)
  {
    if(LT == 0 && RT < 7)
    {
      RT++;
      LT--;
    }
    else if (LT >=1 && RT < 7)
    {
      RT++;
      LT--;
    }
    else if (LT == 7 && RT == 7)
    {
      LT-=5;
    }
  }
  if (digitalRead(LLS)==LOW)
  {
    if(RT == 0 && LT < 7)
    {
      LT++;
      RT--;
    }
    else if (RT >=1 && LT < 7)
    {
      LT++;
      RT--;
    }
    else if (LT == 7 && RT == 7)
    {
      RT-=5;
    }
  }
}
