import pyvisa


# List resources
def list_resources():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    return ports


# print(list_resources)


# list_rescources()


class ArduinoVISADevice:
    def __init__(self, resource):
        """create instance of device.

        Args:
            resource (string); name of accessable resource ("ASRL{n}::INSTR")
        """
        rm = pyvisa.ResourceManager("@py")
        self.channel = resource
        self.device = rm.open_resource(
            resource, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        """Request identification of the device"""
        identification = self.device.query("*IDN?")
        print(f"Identification: \n {identification}")

    def set_output_value(self, value):
        """Set the output value of the device
        Args:
            value (integer); output on channel 0
        """
        self.device.query(f"OUT:CH0 {value}")
        self.output_value = value

    def set_output_voltage(self, value):
        """Set the output voltage of the device.

        Args:
            value (float (V)): output voltage in V

        Returns:
            _type_: interger; new value of device on channel 0
        """
        response = self.device.query(f"OUT:CH0 {round((value * 1023) / 3.3)}")
        return response

    def get_output_value(self):
        """return the output value of the device

        Returns:
            _type_: interger; measured output on channel 0
        """
        real_output_value = self.device.query("OUT:CH0?")
        return real_output_value

    def get_input_value(self, port):
        """measure the input value of the device on a given port

        Args:
            port (interger): channel number

        Returns:
            _type_: interger; the measured value of the given port
        """
        input = self.device.query(f"MEAS:CH{port}?")
        return input

    def get_input_voltage(self, port):
        """measure the input value of the device on a given port in volts

        Args:
            port (interger): channel number

        Returns:
            _type_: float; The measured value on the given port in volts
        """
        input = self.device.query(f"MEAS:CH{port}?")
        input_v = (float(input) / 1023) * 3.3
        return input_v


# arduino = ArduinoVISADevice("ASRL8")
# arduino.get_identification()

# arduino.set_output_value(800)
# time.sleep(1)
# print(arduino.get_output_value())
# print(arduino.get_input_value(0))
# print(arduino.get_input_voltage(0))
# print("EN door!")
# arduino.set_output_voltage(2)
# print(arduino.get_output_value())
# print(arduino.get_input_value(0))
# print(arduino.get_input_voltage(0))
# time.sleep(1)
