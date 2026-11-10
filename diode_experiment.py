import time
import numpy as np
from test_controller import ArduinoVISADevice, list_resources


# Make instance for the arduino
# print(list_resources())
# arduino = ArduinoVISADevice("ASRL9::INSTR")
# arduino.set_output_value(0)


# Make function to do a full measurement and return as lists.
class DiodeExperiment:
    def __init__(self, port):
        self.arduino = ArduinoVISADevice(port)
        self.arduino.set_output_value(0)

    # this function does one measurement over the range of voltages
    def measurements(self):
        # U1 = []
        # U2 = []
        I = []
        U_lamp = []
        for i in np.arange(0, 1023):
            self.arduino.set_output_value(i)

            u1 = self.arduino.get_input_voltage(1)
            u2 = self.arduino.get_input_voltage(2)

            # U1.append(u1)
            # U2.append(u2)
            U_lamp.append(u1 - u2)
            I.append(u2 / 220)
            time.sleep(0.001)
        self.data = [U_lamp, I]
        self.arduino.set_output_value(0)
        return self.data

    # Do several measurements and average them for each output. Also return the STD to be able to account for error margins
    def averageddata(self, n):
        print("Averaging")
        metingen_voltage = []
        metingen_stroom = []

        for i in range(n):
            data = self.measurements()
            metingen_voltage.append(data[0])
            metingen_stroom.append(data[1])
            print(i)
        meting_voltage_array = np.array(metingen_voltage)
        meting_stroom_array = np.array(metingen_stroom)

        averaged_volt = np.mean(meting_voltage_array, axis=0)
        averaged_current = np.mean(meting_stroom_array, axis=0)

        STD_Volt = np.std(metingen_voltage, axis=0)
        STD_Current = np.std(metingen_stroom, axis=0)
        self.averageddataset = [averaged_volt, averaged_current, STD_Volt, STD_Current]
        return (averaged_volt, averaged_current, STD_Volt, STD_Current)
