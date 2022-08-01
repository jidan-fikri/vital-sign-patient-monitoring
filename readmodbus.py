import minimalmodbus
import serial
import time

# Set to true to edit values
WRITE = False

instrument = minimalmodbus.Instrument(
    "COM6", 1
)  # port name, slave address (in decimal)

instrument.serial.baudrate = 115200  # Baud
instrument.serial.bytesize = 8
instrument.serial.parity = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 0.2  # seconds

instrument.mode = minimalmodbus.MODE_RTU  # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True

PV_VOLTAGE = 0x30001



while (True) :
    

    # Print panel info
    pv_voltage = instrument.read_register(
        PV_VOLTAGE, 2, 4, False
    )  # Registernumber, number of decimals
    print("Panel voltage:\t" + str(pv_voltage) + "V")

    time.sleep(1)

