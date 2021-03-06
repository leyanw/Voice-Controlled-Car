import serial
import time

#Initializing Serial Port
ser = serial.Serial(

	port='/dev/ttyS0',
	baudrate = 115200,
        #baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout= 1,
	xonxoff=False,
	rtscts=False,
	dsrdtr=False,
	writeTimeout=100
)
#Byte 4 and 5 X axis speed (Change byte 5 last four bits only)
#Byte 6 and 7 Y axis speed (Change byte 7 last four bits only)
#Byte 8 and 9 Z axis speed (Change byte 7 last four bits only)
#Byte 10 controls direction (Chnage only last three bits: 0 is positive 1 is negative)
#Last three bits X, Y, Z

def straight():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x22,0x00,0x00,0x01]))
    time.sleep(2)
    #ser.flushOutput()
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #led.set_state(aiy.voicehat.LED.BLINK)
    #ser.flushOutput()
    
def back():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x22,0x00,0x00,0x02]))
    #led.set_state(aiy.voicehat.LED.BLINK)
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()
    
def right():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x22,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()
    
def left():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x22,0x00,0x00,0x00,0x00,0x04]))
    #time.sleep(3)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()
    
def top_Left():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x22,0x00,0x22,0x00,0x00,0x04]))
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()

def top_Right():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x22,0x00,0x22,0x00,0x00,0x00]))
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()

def bottom_Left():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x22,0x00,0x22,0x00,0x00,0x06]))
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()

def bottom_Right():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x22,0x00,0x22,0x00,0x00,0x02]))
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #time.sleep(1)
    #ser.flushOutput()
def leftcircle():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x22,0x01]))
    #led.set_state(aiy.voicehat.LED.BLINK)
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x04,0x00,0x00,0x00,0x00]))
    #ser.flushOutput()

def rightcircle():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x04,0x00,0x00,0x00,0x22,0x04]))
    #time.sleep(2)
    #ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
    #led.set_state(aiy.voicehat.LED.BLINK)
    #ser.flushOutput()

def stop():
    ser.write(serial.to_bytes([0xFF,0xFE,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00]))
