from pythondaq.diode_experiment import DiodeExperiment
from matplotlib import pyplot as plt
import csv
from pythondaq.arduino_device import list_resources

print(list_resources())

# experiment = DiodeExperiment("ASRL9::INSTR")
# data = experiment.averageddata(2)


class run_experiment:
    def __init__(self, name):
        """start experiment

        Args:
            name (string): ("ASRL{10}::INSTR")
        """
        self.experiment = DiodeExperiment(name)

    def measure(self, it):
        """make measurements

        Args:
            iterations (interger): number of measurements done for the average

        Returns:
            _type_: (list); new averaged data set
        """
        self.data = self.experiment.averageddata(it)
        return self.data

    def drawdata(self):
        """produce graph of most recent dataset"""
        print("drawing averages")
        [avg_volt, avg_current, Std_volt, Std_current] = self.data
        plt.errorbar(avg_volt, avg_current, xerr=Std_volt, yerr=Std_current, fmt=".")
        plt.show()

    def getcsv(self, name):
        """Turn current data into CSV file

        Args:
            name (string): name of csv file
        """
        with open(f"{name}.csv", "w", newline="") as csvfile:
            [avg_volt, avg_current, Std_volt, Std_current] = self.data
            writer = csv.writer(csvfile)
            writer.writerow(["U", "I", "STD(U)", "STD(I)"])
            for a, b, c, d in zip(avg_volt, avg_current, Std_volt, Std_current):
                writer.writerow([a, b, c, d])


experiment = run_experiment("ASRL8::INSTR")
print(experiment.measure(2))
experiment.drawdata()
experiment.getcsv("tatsa")

print("Programma is klaar!")
