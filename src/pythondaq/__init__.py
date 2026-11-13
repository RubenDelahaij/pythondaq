def main() -> None:
    print("Hello from pythondaq!")


def measureledlight():
    from pythondaq.run_experiment import MeasureLED

    MeasureLED(2, "N", "Placeholder")
    print("YO")
