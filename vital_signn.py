import time
import serial
ser=serial.Serial(port="COM7", baudrate=115200, bytesize=8, parity='N' )  


def wave():    
    if (address_low == b'\00'):
        address_high = ser.read()
        #print(address_high)
        if (address_high == b'\01'):
            for i in range (0, bytecount_int):
                EKGwave = ser.read()
                EKGwave_int = int.from_bytes(EKGwave, "big")
                #print(EKGwave_int)
                
        elif (address_high == b'\02'):
            for i in range (0, bytecount_int):
                SPO2wave = ser.read()
                SPO2wave_int = int.from_bytes(SPO2wave, "big")
                #print(SPO2wave_int)
          

def num():
    if (address_low == b'\01'):
        address_high = ser.read()
        # print(data3)
        if (address_high == b'\01'):
            for i in range (0, bytecount_int):
                EKGnum = ser.read()
                EKGnum_int = int.from_bytes(EKGnum, "big")
                #print(EKGnum_int)

        elif (address_high == b'\02'):
            #SPO2num_int= []
            for i in range (0, bytecount_int):
                SPO2num = ser.read()
                SPO2num_int = int.from_bytes(SPO2num, "big")
                #SPO2num_int.append (int.from_bytes(SPO2num, "big"))
                #print(SPO2num_int)


def NIB():
    ser.write(b'\x02')
    ser.write(b'\xA3')
    ser.write(b'\x02')
    ser.write(b'\x03')
    ser.write(b'\x4E')
    ser.write(b'\x53')
    ser.write(b'\x31')
    ser.write(b'\x73')
    ser.write(b'\x03')
    
    
NIB() 


while True:
        header = ser.read()
        
        if (header == b'\xA7'):
            #print ("OKE")
            ya = ser.read()
            #print (ya)
            if (ya == b'\x11'):
                ye = ser.read()
                #print (ye)
                if (ye == b'\x02'):
                    #yo = ser.read()
                    for i in range (0,7):
                        data = ser.read()
                        data_int = int.from_bytes(data, "big")
                        print (data_int)

"""

        int_v = int.from_bytes(header, "big")
        if (header == b'\02'):
            bytecount = ser.read()
            bytecount_str = str(bytecount)
            print (bytecount)
            #bytecount_int = (int(bytecount_str[5]))
            if (bytecount != b'\ff'):
                address_low = ser.read()
                #print(address_low)
                if (address_low == b'\x11'):
                    address_high = ser.read()
                    #print(address_high)
                    if (address_high == b'\x03'):
                        for i in range (0, 7):
                            inb = ser.read()
                            inb_int = int.from_bytes(inb, "big")
                            #print(inb_int)
   """ 
  

#while True: 
        #NIB()               
        #header = ser.read()
        #print (header)
        #int_v = int.from_bytes(header, "big")
        #if (header == b'\02'):
           # bytecount = ser.read()
            #bytecount_str = str(bytecount)
            #bytecount_int = (int(bytecount_str[5]))
           # if (bytecount != b'\ff'):
               # address_low = ser.read()
                #print(address_low)
                #wave()
                #num()

            
            






        
        
      
    
