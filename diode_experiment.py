import pyvisa
import time 
import numpy as np
from matplotlib import pyplot as plt
import csv
from test_controller import ArduinoVISADevice 

rm = pyvisa.ResourceManager("@py")

#List resources
def list_resources():
    ports = rm.list_resources()
    print(ports)
    return ports
print(list_resources())

#maak instance voor de ardiuno
arduino = ArduinoVISADevice("ASRL8")
arduino.set_output_value(0)



# def measure_1():
#     return(float(device.query(f"MEAS:CH1?")))
# def measure_2():
#     return(float(device.query(f"MEAS:CH2?")))
# def DAC(i):
#     return((float(i) / 1023)*3.3)
# def ADC(i):
#     return((float(i)/3.3)*1023)


def meetreeks():
    U1 = []
    U2 = []
    U_lamp = []
    for i in np.arange(0, 1023):
        device.query(f"OUT:CH0 {i}")
        U1.append(arduino.)
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
    return(average_volt, average_current, STD_Volt, STD_Current)

[Gem_volt, Gem_stroom, Std_volt, Std_stroom] =Middelen(5) 
#plt.errorbar(Gem_volt, Gem_stroom, xerr = Std_volt, yerr= Std_stroom, fmt = '.')
#plt.show()


with open("measurements.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["U", "I","STD(U)", "STD(I)"])
    for a, b, c, d in zip(Gem_volt, Gem_stroom, Std_volt, Std_stroom):
        writer.writerow([a, b, c, d])





        





















time.sleep(2)
device.query(f"OUT:CH0 0")
