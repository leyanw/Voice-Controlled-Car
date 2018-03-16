import processing.serial.*;


class CarControl {

  //variables for car directions;
  byte directx;//x direction
  byte directy;//y directon
  byte directz;//z direction
  byte direct; // direction of each motor,[2]=x,[1]=y,[0]=z,set 0=normal,1=reverse
               
  
  //range from 0 to 100
  //map the value from 0-100 to 0-255
  void move(int x,int y,int z) {
    //limitations
    x = (x<-100)?-100:(x>100)? 100:x;
    y = (y<0-100)?-100:(y>100)? 100:y;
    z = (z<-100)?-100:(z>100)? 100:z;
     
    if(x>=0){
      x = (int)map(x, 0, 100, 0, 127);
      directx = (byte)x;
      //directx = directx &= 0xFF;
      direct &= ~0x04;
    }
    else{
      x = -x;//make it positive
      x = (int)map(x, 0, 100, 0, 127);
      directx = (byte)x;
      //directx = directx &= 0x5F;//limit the max speed of the car to 0x5F
      direct |= 0x04;
    }

    if(y>=0){
      y = (int)map(y, 0, 100, 0, 127);
      directy = (byte)y;
      //directy = directy &= 0x5F;
      direct &= ~0x02;
    }
    else{
      y = -y;
      y = (int)map(y, 0, 100, 0, 127);
      directy = (byte)y;
      //directy = directy &= 0x5F;
      direct |= 0x02;
    }
    if(z>=0){
      z = (int)map(z, 0, 100, 0, 127);
      directz = (byte)z;
      //directz = directz &= 0x5F;
      direct &= ~0x01;
    }
    else{
      z = -z;
      z = (int)map(z, 0, 100, 0, 127);
      directz = (byte)z;
      //directz = directz &= 0x5F;
      direct |= 0x01;
    }  
    send();
  }
  
  void stop(){ 
    directx = 0x00;
    directy = 0x00;
    directz = 0x00;
    direct = 0x00;
    send();
  }
  
  void send(){
      byte[] packet = new byte[10];
      packet[0] = (byte)0xFF;   // Header1
      packet[1] = (byte)0xFE;   // Header2
      packet[2] = (byte)0x01;   // Control Mode
      packet[3] = (byte)0x00;   // Direction x high byte
      packet[4] = (byte)directx;// Direction x low byte
      packet[5] = (byte)0x00;   // Direction y high byte
      packet[6] = (byte)directy;// Direction y low byte
      packet[7] = (byte)0x00;   // Direction z high byte
      packet[8] = (byte)directz;// Direction z low byte
      packet[9] = (byte)direct; // Direction of each motor
      
      //println(packet[6]);
      myport.write(packet);
  }
  
  
  
  
}