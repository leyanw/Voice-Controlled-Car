import processing.serial.*;
CarControl car;
Serial myport;
Serial voiceport;
PFont myFont;//the display Font

String inString;//input for msg from voice command

void setup() {
  size(200,200);
  //Fonts need to create font tool
  //myFont = loadFont("ArialMS-18.vlw");
  //textFont(myFont,18);
  noLoop();
  car = new CarControl();
  myport = new Serial(this, Serial.list()[1], 115200);
  voiceport = new Serial(this, "/dev/pts/2", 115200);//receive port data from voice command
  voiceport.bufferUntil(10);
}
  int x = 0;
  int y = 0;
  int z = 0;
  boolean loop = false;
  boolean loopflag = false;
void draw() {
  background(0);
  //println("received: " + inString);
  
  translate(width/2, height/2);
  
  //x = (int)map(mouseX, 0, width, -50, 50);
  //y = (int)map(mouseY, 0, height, 50, -50);
  z = (int)map(mouseX, 0, width, -50, 50);
  //println(y);
  car.move(x,y,z); //<>//
  //car.stop();
  
}

void mousePressed(){
  if(loopflag == false){
    loop();
    loopflag = true;
  }
  else{
    noLoop();
    loopflag = false;
    car.stop();
  }
}

void serialEvent(Serial p){
  inString = p.readString();
  println(inString);
}