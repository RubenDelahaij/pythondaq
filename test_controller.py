import pyvisa


# List resources
def list_resources():
    rm = pyvisa.ResourceManager("@py")
    ports = rm.list_resources()
    print(ports)
    return ports


# print(list_resources)


# list_rescources()


class ArduinoVISADevice:
    def __init__(self, resource):
        rm = pyvisa.ResourceManager("@py")
        self.channel = resource
        self.device = rm.open_resource(
            resource, read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        identification = self.device.query("*IDN?")
        print(f"Identification: \n {identification}")

    def set_output_value(self, value):
        self.device.query(f"OUT:CH0 {value}")
        self.output_value = value

    def set_output_voltage(self, value):
        response = self.device.query(f"OUT:CH0 {round((value * 1023) / 3.3)}")
        return response

    def get_output_value(self):
        real_output_value = self.device.query("OUT:CH0?")
        return real_output_value

    def get_input_value(self, port):
        input = self.device.query(f"MEAS:CH{port}?")
        return input

    def get_input_voltage(self, port):
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
