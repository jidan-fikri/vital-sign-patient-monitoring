import time
import serial
import numpy as np
ser=serial.Serial(port="COM", baudrate=115200, bytesize=8, parity='N' )  

nibp = []
nibp_temp = [] #menyimpan data sementara nibp dalam array
spo2_temp = [] #menyimpan data sementara spo2 dalam array

def wave(): 
#Untuk menampilkan wave EKG dan SpO2
    int_v = int.from_bytes(header, "big")
    if (header == b'\02'):
        bytecount = ser.read()
        bytecount_str = str(bytecount)
        if (bytecount != b'\ff'):
            address_low = ser.read()
            if (address_low == b'\00'):
                address_high = ser.read()
                if (address_high == b'\01'):
                    for i in range (0, 3):
                        EKGwave = ser.read()
                        EKGwave_int = int.from_bytes(EKGwave, "big")
                        print(EKGwave_int)                
                elif (address_high == b'\02'):
                    for i in range (0, 1):
                        SPO2wave = ser.read()
                        SPO2wave_int = int.from_bytes(SPO2wave, "big")
                        print(SPO2wave_int)
          

def num():
#Untuk menampilkan nilai SpO2
    int_v = int.from_bytes(header, "big")
    if (header == b'\02'):
        bytecount = ser.read()
        bytecount_str = str(bytecount)
        if (bytecount != b'\ff'):
            address_low = ser.read()
            if (address_low == b'\01'):
                address_high = ser.read()
                if (address_high == b'\02'):
                    for i in range (0, 2):
                        SPO2num = ser.read()
                        SPO2num_int = int.from_bytes(SPO2num, "big")
                        spo2_temp.append(SPO2num_int)
                    result = float(f"{spo2_temp[-2]}.{spo2_temp[-1]}") #SpO2 data
                    print(round(result, 2)) #Menampilkan nilai spo2 dengan pembulatan 2 angka dibelakang koma


def nibp_read ():
#Untuk membaca tekanan darah dengan NIBP
    if (header == b'\xA7'):
            ya = ser.read()
            if (ya == b'\x11'):
                ye = ser.read()
                if (ye == b'\x02'):
                    for i in range (0,7):
                        data = ser.read()
                        data_int = int.from_bytes(data, "big")
                        nibp_temp.append(data_int)                        
                    nibp.append(nibp_temp)
                    sys = nibp[0][0] #systolic data
                    mapp = nibp[0][2] #map pressure data
                    dias = nibp[0][4] #diastolic data
                    pulse = nibp [0][6] #pulse/min data 
                    print("Systholic pressure: ", sys)
                    print("MAP Pressure: ", mapp)
                    print("Diastolic Pressure: ", dias)
                    print("Pulse/min: ", pulse)
                    
                    
def NIBstart():
#Untuk memulai pengukuran tekanan darah
    ser.write(b'\x02')
    ser.write(b'\xA3')
    ser.write(b'\x02')
    ser.write(b'\x03')
    ser.write(b'\x4E')
    ser.write(b'\x53')
    ser.write(b'\x31')
    ser.write(b'\x73')
    ser.write(b'\x03')
    
    
def NIBstop():




while True:
        header = ser.read()
        #drop function here

            
            






        
        
      
    
