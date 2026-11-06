import pyvisa
import time


rm = pyvisa.ResourceManager("@py")


def list_rescources():
    ports = rm.list_resources()
    print(ports)
    return ports


list_rescources()


class ArduinoVISADevice:
    def __init__(self, resource):
        self.channel = resource
        self.device = rm.open_resource(
            f"{resource}::INSTR", read_termination="\r\n", write_termination="\n"
        )

    def get_identification(self):
        identification = self.device.query("*IDN?")
        print(f"Identification: \n {identification}")

    def set_output_value(self, value):
        self.device.query(f"OUT:CH0 {value}")
        self.output_value = value

    def set_output(self):
        self.device.query(f"")

    def get_output_value(self):
        real_output_value = self.device.query("OUT:CH0?")
        print(f"real output value: {real_output_value}")
        return real_output_value

    def get_input_value(self, port):
        input = self.device.query(f"OUT:CH{port}?")
        print(f"Measured input value: {input}")
        return input

    def get_input_voltage(self, port):
        input = self.device.query(f"OUT:CH{port}?")
        print(f"ff testen hoor {input}")
        input_v = (float(input) / 1023) * 3.3
        print(f"Input voltage van port {port}: {input_v}")
        return input_v


arduino = ArduinoVISADevice("ASRL8")
arduino.get_identification()

arduino.set_output_value(1000)
time.sleep(0.5)
arduino.get_input_value(1)
arduino.get_input_voltage(1)
time.sleep(0.5)
arduino.get_input_value(1)
arduino.get_input_voltage(1)
