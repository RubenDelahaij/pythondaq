import click
from pythondaq.diode_experiment import DiodeExperiment, listresource, inforomation
import csv
from matplotlib import pyplot as plt


@click.group()
def main():
    pass


@main.command()
def list():
    """Command to print the different available devices"""
    print("work in progress, list devices")
    print(listresource())


@main.command()
@click.argument(
    "resource",
    help="The name of the resource the user wants measured, in the string : {ASRL{n}::INSTR}",
)
@click.option(
    "--min",
    help="The value from which the programm starts the measurement [V]",
    default=0.0,
    type=float,
    show_default=True,
)
@click.option(
    "--max",
    help="The value at which the programm stops the measurement [V] ",
    default=3.3,
    type=float,
    show_default=True,
)
@click.option(
    "-s",
    "--stepsize",
    help="The size of the steps the programm makes during measuring [V]",
    default=round(3.3 / 1023, 4),
    type=float,
    show_default=True,
)
@click.option(
    "-a",
    "--averages",
    help="Amount of measurements the programm does to make an averaged data set",
    default=1,
    type=int,
    show_default=True,
)
@click.option(
    "-out",
    "--output",
    help="Name of the exported CSV file. If no name is provided the data is not exported",
)
@click.option(
    "-g/-ng",
    "--graph/--no-graph",
    is_flag=True,
    default=False,
    help="Decides wether the programm plots the obtained data",
)
def scan(resource, min, max, stepsize, averages, output, graph):
    """Scan the current and voltage of the diode over a given interval with a given stepsize"""
    if stepsize == round(3.3 / 1023, 4):
        stepsize = 3.3 / 1023
    arduino = DiodeExperiment(resource)
    data = arduino.averageddata(averages, stepsize, min, max)
    [averaged_volt, averaged_current, STD_Volt, STD_Current] = data
    print(
        f"Average votlage through the Diode: {averaged_volt} \n Average current through the Diode: {averaged_current} \n Standard deviation of the voltage: {STD_Volt} \n Standard deviation of the current: {STD_Current}"
    )
    if output:
        with open(f"{output}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["U", "I", "STD(U)", "STD(I)"])
            for a, b, c, d in zip(
                averaged_volt, averaged_current, STD_Volt, STD_Current
            ):
                writer.writerow([a, b, c, d])
    if graph:
        print("drawing averages")
        plt.errorbar(
            averaged_volt, averaged_current, xerr=STD_Volt, yerr=STD_Current, fmt="."
        )
        plt.show()


@main.command()
@click.argument("device", help="name of the device")
def info(device):
    print(f"Identification: {inforomation(device)}")
