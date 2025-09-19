int portaled = 2;     
int portaLDR = A0;     
int estado;

void setup() {
  pinMode(portaled, OUTPUT);
  pinMode(portaLDR, INPUT);
}

void loop() {
   if (estado < 0) {                 
    digitalWrite(portaled, HIGH);     
  } else {
    digitalWrite(portaled, LOW);      
  }
}