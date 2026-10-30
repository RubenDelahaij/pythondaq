import pyvisa
import time 
import numpy as np
from matplotlib import pyplot as plt

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n"
)
identification = device.query("*IDN?")
print(identification)
device.query(f"OUT:CH0 0")
def measure_1():
    return(float(device.query(f"MEAS:CH1?")))
def measure_2():
    return(float(device.query(f"MEAS:CH2?")))
def DAC(i):
    return((float(i) / 1023)*3.3)
def ADC(i):
    return((float(i)/3.3)*1023)

# for i in range(1000):
#     device.query(f"OUT:CH0 {i}")
#     print(measure_1())
#     print(measure_2())

def measure_lampje():
    U1 = []
    U2 = []
    U_lamp = []
    I = []
    for i in np.arange(0, 1023):
        device.query(f"OUT:CH0 {i}")
        #print(f"Lampje(ruw): {measure_1()} \n Lampje(V): {DAC(measure_1()):.2f} \n Weerstand(ruw): {measure_2()} \n Weerstand(V): {DAC(measure_2()):.2f} ")
        U1.append(measure_1())
        U2.append(measure_2())
        U_lamp.append(DAC(measure_1()- measure_2()))
        I.append(float(DAC(measure_2())) / 220)
        time.sleep(0.001)
    return U_lamp, I

# for i in range(1):
#     Measurement = measure_lampje()
#     plt.errorbar(Measurement[0], Measurement[1], yerr=0.00000733, xerr=(3.3/(1023*2)), fmt = '.')
# plt.show()

def Middelen(n):
    metingen_voltage = []
    metingen_stroom = []
    for i in range (n):
        metingen_voltage.append(measure_lampje()[0])
        metingen_stroom.append(measure_lampje()[1])
        print(i)

    meting_voltage_array = np.array(metingen_voltage)
    meting_stroom_array = np.array(metingen_stroom)

    average_volt = np.mean(meting_voltage_array, axis = 0)
    average_current = np.mean(meting_stroom_array, axis = 0)

    STD_Volt = np.std(metingen_voltage, axis = 0)
    STD_Current = np.std(metingen_stroom, axis = 0)

    print(meting_voltage_array)
    print(average_current)
    print(average_volt)

    plt.errorbar(average_volt, average_current, xerr = STD_Volt, yerr= STD_Current, fmt = '.')
    plt.show()

Middelen(10)




        





















time.sleep(2)
device.query(f"OUT:CH0 0")
