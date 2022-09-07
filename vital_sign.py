import serial

ser=serial.Serial(port="COM", baudrate=115200, bytesize=8, parity='N' )  
ser1=serial.Serial(port="COM", baudrate=115200)  

nibp = []
ecg = []
nibp_temp = [] #menyimpan data sementara nibp dalam array
spo2_temp = [] 

def wave(): 
    ecg_temp = []
    if (address_low == b'\00'):
        address_high = ser.read()
        
        #Gelombang ECG
        if (address_high == b'\01'):
            for i in range(0,7):
                EKGwave = ser.read()
                EKGwave_int = int.from_bytes(EKGwave, "big")
                ecg_temp.append(EKGwave_int)
            ecg.append(ecg_temp)
            ecg_temp = []
            lead1 = ecg [-1][0]
            lead2 = ecg [-1][1]
            lead3 = ecg [-1][2]
            #print(lead1)
            show = ('ST<{"cmd_code":"set_value","type":"line_series","widget":"line_series_ecg1","mode":"push","value":'+str(lead1)+'}>ET')
            show1 = ('ST<{"cmd_code":"set_value","type":"line_series","widget":"line_series_ecg2","mode":"push","value":'+str(lead2)+'}>ET')
            ser1.write(show.encode())
            ser1.write(show1.encode())
            
        
        #Gelombang SPO2
        elif (address_high == b'\02'):
            for i in range (0, 1):
                SPO2wave = ser.read()
                SPO2wave_int = int.from_bytes(SPO2wave, "big")
                show=('ST<{"cmd_code":"set_value","type":"line_series","widget":"line_series_spo2","mode":"push","value":'+str(SPO2wave_int)+'}>ET')
                ser1.write(show.encode())
       
def num():
    #Untuk membaca HR dan persen SPO2 pasien
    if (address_low == b'\01'):
        address_high = ser.read()
        
        #Untuk mengirim data HR
        if (address_high == b'\01'):
            for i in range (0, 1):
                EKGnum = ser.read()
                EKGnum_int = int.from_bytes(EKGnum, "big")
                show=('ST<{"cmd_code":"set_value","type":"image_value","widget":"hr_value","value":'+str(EKGnum_int)+'}>ET')
                ser1.write(show.encode())
                print(EKGnum_int)
        
        #Untuk mengirim data SPO2
        elif (address_high == b'\02'):
            #SPO2num_int= []
            for i in range (0, 2):
                SPO2num = ser.read()
                SPO2num_int = int.from_bytes(SPO2num, "big")
                #SPO2num_int.append (int.from_bytes(SPO2num, "big"))
                #print(SPO2num_int)        
                spo2_temp.append(SPO2num_int)
            result = float(f"{spo2_temp[-2]}.{spo2_temp[-1]}") #SpO2 data
            show=('ST<{"cmd_code":"set_value","type":"image_value","widget":"spo2_value","value":'+str(result)+'}>ET')
            ser1.write(show.encode())
            


def nibp_read ():
#Untuk membaca tekanan darah dengan NIBP
    if (nib == b'\x11'):
        address_high = ser.read()
        if (address_high == b'\x02'):
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

def temperatur ():
    if (address_low == b'\x20'):
        address_high = ser.read()
        if (address_high == b'\x02'):
            temperatur1 = ser.read()
            temperatur2 = ser.read()
            temperatur_int1 = int.from_bytes(temperatur1, "big")
            temperatur_int2 = int.from_bytes(temperatur2, "big")
            temperatur_add = temperatur_int1 + temperatur_int2
            temperatur_div = temperatur_add / 10
            temperatur_ok = temperatur_div + 25.5   
            show=('ST<{"cmd_code":"set_value","type":"image_value","widget":"temp_value","value":'+str(temperatur_ok)+'}>ET')
            ser1.write(show.encode())
            #print(temperatur_ok)
                    
                    
def NIBstart():
    ser.write(b'\x02')
    ser.write(b'\xA3')
    ser.write(b'\x02')
    ser.write(b'\x03')
    ser.write(b'\x4E')
    ser.write(b'\x53')
    ser.write(b'\x31')
    ser.write(b'\x73')
    ser.write(b'\x03')
    
    

while True:
        header = ser.read()
        if (header == b'\02'):
            bytecount = ser.read()
            if (bytecount != b'\ff'):
                address_low = ser.read()
                wave()
                num()
                temperatur()
