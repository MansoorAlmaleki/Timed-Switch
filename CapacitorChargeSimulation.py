import matplotlib.pyplot as plt

#equations used in the loop
"""Voltage = Charge(coulomb)/Capacitance(Farads), Charge(coulomb) = Current(ampere) * time"""

"""The simulation approximates the time when a capacitor reaches the threshold voltage in the Simulation Time period.
in some cases where the Simulation period is set to a small value, the simulation dose not simulate over a longer range of time giving a false answer as the
threshold activation time is longer than the simulated period"""

"""if the threshold voltage is greater than supplied voltage the capacitor voltage will never surpass the threshold voltage"""

Capacitance= 0.0001#Farads
Resistance = 1000#ohms
Voltage = 7#supply voltage

#set the voltageThreshold
VoltageThreshold = 2.85

#keep these values as is
TimeUntilTrigger = 0
Surpassed = False

#Simulation period and time step is measured in seconds, increase/decrease whichever value to meet the required case
SimulationPeriod = 1
SimulationTimeIncrement = 0.0001#the simulation timestep where lower means more accurate measurement but in return for a longer processing time

VoltageOverTime = []
TimeStepArray = []
ThresholdVoltageArray = []

ChargeAccumulation = 0
TimeStep = 0
for i in range(int(SimulationPeriod/SimulationTimeIncrement)):
    ThresholdVoltageArray.append(VoltageThreshold)
    TimeStepArray.append(TimeStep)

    Current = (Voltage - (ChargeAccumulation/Capacitance))/Resistance
    ChargeAccumulation += Current*SimulationTimeIncrement
    VoltageOverTime.append(ChargeAccumulation/Capacitance)

    #check if current capacitor voltage is greater than or equal to threshold voltage
    if((ChargeAccumulation/Capacitance) >=  VoltageThreshold and Surpassed == False):
        Surpassed = True
        TimeUntilTrigger = TimeStep

    TimeStep += SimulationTimeIncrement


if(Surpassed):
    plt.title(str(TimeUntilTrigger) + " seconds until triggered")
else:
    plt.title("Capacitor does not exceed threshold voltage")

plt.plot(TimeStepArray, VoltageOverTime)
plt.plot(TimeStepArray, ThresholdVoltageArray)
plt.xlabel("Time (Seconds)")
plt.ylabel("Voltage (V)")
plt.show()
