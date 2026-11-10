from diode_experiment import DiodeExperiment
from matplotlib import pyplot as plt
import csv
from test_controller import list_resources

print(list_resources())

experiment = DiodeExperiment("ASRL9::INSTR")
data = experiment.averageddata(2)


def drawaverages():
    print("drawing averages")
    [avg_volt, avg_current, Std_volt, Std_current] = data
    plt.errorbar(avg_volt, avg_current, xerr=Std_volt, yerr=Std_current, fmt=".")
    plt.show()


def getcsv(name):
    with open(f"{name}.csv", "w", newline="") as csvfile:
        [avg_volt, avg_current, Std_volt, Std_current] = data
        writer = csv.writer(csvfile)
        writer.writerow(["U", "I", "STD(U)", "STD(I)"])
        for a, b, c, d in zip(avg_volt, avg_current, Std_volt, Std_current):
            writer.writerow([a, b, c, d])


getcsv("jippiejeee")
drawaverages()

print("Programma is klaar!")
