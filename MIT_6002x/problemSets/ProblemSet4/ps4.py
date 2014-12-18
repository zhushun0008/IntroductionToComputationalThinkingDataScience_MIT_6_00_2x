# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

# Test ps3b
# virus = ResistantVirus(0.0, 1.0, {"drug1":True, "drug2":False}, 0.0)


#
# PROBLEM 1
#



def simulationTreatAtDiffTime(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                              mutProb, numTrials, startTreatTime, totalTimesteps):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """

    totalVirusPopEachTrial = []
    averTotalVirusPop = []
    averTotalResistentVirusPop = []
    for j in range(numTrials):
#        print "running trial", j

        Viruses = []
        timeSteps = totalTimesteps
        virusPopulation = []
        resistentVirusPopulation = []
        for i in range(numViruses):
            Viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

        patient = TreatedPatient(Viruses, maxPop)

        for i in range(timeSteps):
            if i == startTreatTime:
                patient.addPrescription('guttagonol')

            virusPopulation.append(patient.update())

        totalVirusPopEachTrial.append(virusPopulation[-1])


    return totalVirusPopEachTrial


def plotAll(totalVirusPopEachTimeStep0, totalVirusPopEachTimeStep75, totalVirusPopEachTimeStep150, totalVirusPopEachTimeStep300):
    # Four axes, returned as a 2-d array
    f, axarr = pylab.subplots(2, 2)
    axarr[0, 0].hist(totalVirusPopEachTimeStep0, bins=12, range=(0, 600)) # each bin of size 50
    axarr[0, 0].set_title('Total Virus Treating at Time-Step 0')
    axarr[0, 1].hist(totalVirusPopEachTimeStep75, bins=12, range=(0, 600)) # each bin of size 50
    axarr[0, 1].set_title('Total Virus Treating at Time-Step 75')
    axarr[1, 0].hist(totalVirusPopEachTimeStep150, bins=12, range=(0, 600)) # each bin of size 50))
    axarr[1, 0].set_title('Total Virus Treating at Time-Step 150')
    axarr[1, 1].hist(totalVirusPopEachTimeStep300, bins=12, range=(0, 600)) # each bin of size 50))
    axarr[1, 1].set_title('Total Virus Treating at Time-Step 300')

    pylab.show()



def getCuredFraction(totalVirusList, threshold):
    numCured = 0

    for i in range(len(totalVirusList)):
        if totalVirusList[i] <= threshold:
            numCured += 1
    print "Fraction of cured Patient is ", float(numCured)/len(totalVirusList)
    return numCured, float(numCured)/len(totalVirusList)

def solveProblem4():
    numVirusesList = [100, 200, 400, 800]
    maxPopList = [1000, 1500, 2000, 2500]
    maxBirthProbList = [0.1, 0.2, 0.4, 0.8, 1.6]
    clearProbList = [0.05, 0.1, 0.2, 0.4]
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    numTrials = 300
    totalTimesteps = 300
    startTreatTime150 = 150
    curedFractionListForNumVirus = []
    curedFractionListForMaxPop = []
    curedFractionListForMaxBirthProb = []
    curedFractionListForClearProb = []

    threshold = 50

    for i in range(len(numVirusesList)):
        tempNumVirus = numVirusesList[i]
        totalVirusPopEachTimeStep150 = simulationTreatAtDiffTime(tempNumVirus, maxPop, maxBirthProb, clearProb, resistances,
                                                             mutProb, numTrials, startTreatTime150, totalTimesteps)
        numCured0, curedFraction150 = getCuredFraction(totalVirusPopEachTimeStep150, threshold)
        curedFractionListForNumVirus.append(curedFraction150)


    for i in range(len(maxPopList)):
        tempMaxPop = maxPopList[i]
        totalVirusPopEachTimeStep150 = simulationTreatAtDiffTime(numViruses, tempMaxPop, maxBirthProb, clearProb, resistances,
                                                             mutProb, numTrials, startTreatTime150, totalTimesteps)
        numCured0, curedFraction150 = getCuredFraction(totalVirusPopEachTimeStep150, threshold)
        curedFractionListForMaxPop.append(curedFraction150)

    for i in range(len(maxBirthProbList)):
        tempMaxxBirthProb = maxBirthProbList[i]
        totalVirusPopEachTimeStep150 = simulationTreatAtDiffTime(numViruses, maxPop, tempMaxxBirthProb, clearProb, resistances,
                                                             mutProb, numTrials, startTreatTime150, totalTimesteps)
        numCured0, curedFraction150 = getCuredFraction(totalVirusPopEachTimeStep150, threshold)
        curedFractionListForMaxBirthProb.append(curedFraction150)

    for i in range(len(clearProbList)):
        tempClearProb = clearProbList[i]
        totalVirusPopEachTimeStep150 = simulationTreatAtDiffTime(numViruses, maxPop, maxBirthProb, tempClearProb, resistances,
                                                             mutProb, numTrials, startTreatTime150, totalTimesteps)
        numCured0, curedFraction150 = getCuredFraction(totalVirusPopEachTimeStep150, threshold)
        curedFractionListForClearProb.append(curedFraction150)

    print(curedFractionListForNumVirus)
    print(curedFractionListForMaxPop)
    print(curedFractionListForMaxBirthProb)
    print(curedFractionListForClearProb)



def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    totalTimesteps = 300
    startTreatTime300 = 300
    startTreatTime150 = 150
    startTreatTime0 = 0
    startTreatTime75 = 75
    curedFraction = []
    totalVirusPopEachTimeStep0 = simulationTreatAtDiffTime(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                                                          mutProb, numTrials, startTreatTime0, totalTimesteps)

    totalVirusPopEachTimeStep75 = simulationTreatAtDiffTime(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                                                             mutProb, numTrials, startTreatTime75, totalTimesteps)

    totalVirusPopEachTimeStep150 = simulationTreatAtDiffTime(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                                                             mutProb, numTrials, startTreatTime150, totalTimesteps)

    totalVirusPopEachTimeStep300 = simulationTreatAtDiffTime(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                                                             mutProb, numTrials, startTreatTime300, totalTimesteps)


    threshold = 50
    numCured0, curedFraction0 = getCuredFraction(totalVirusPopEachTimeStep0, threshold)
    numCured75, curedFraction75 = getCuredFraction(totalVirusPopEachTimeStep75, threshold)
    numCured150, curedFraction150 = getCuredFraction(totalVirusPopEachTimeStep150, threshold)
    numCured300, curedFraction300 = getCuredFraction(totalVirusPopEachTimeStep300, threshold)
    print(str(curedFraction0))
    print(str(curedFraction75))
    print(str(curedFraction150))
    print(str(curedFraction300))

    plotAll(totalVirusPopEachTimeStep0, totalVirusPopEachTimeStep75, totalVirusPopEachTimeStep150, totalVirusPopEachTimeStep300)


#simulationDelayedTreatment(300)
#solveProblem4()

#getCuredFraction([10,15],12.5)

#
# PROBLEM 2
#



def simulationTreatWithTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                              mutProb, numTrials, totalTimesteps, drugDelayList):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """

    totalVirusPopEachTrial = []
    averTotalVirusPop = []
    averTotalResistentVirusPop = []
    for j in range(numTrials):
#        print "running trial", j

        Viruses = []
        timeSteps = totalTimesteps
        virusPopulation = []
        resistentVirusPopulation = []
        for i in range(numViruses):
            Viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

        patient = TreatedPatient(Viruses, maxPop)

        for i in range(timeSteps):
            for j in range(len(drugDelayList)):
                if i == drugDelayList[j][1]:
                    patient.addPrescription(drugDelayList[j][0])

            virusPopulation.append(patient.update())

        totalVirusPopEachTrial.append(virusPopulation[-1])


    return totalVirusPopEachTrial





def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    totalTimesteps = 600

    curedFraction = []
    drugDelayList0 = [('guttagonol', 150), ('grimpex', 150)]
    drugDelayList75 = [('guttagonol', 150), ('grimpex', 225)]
    drugDelayList150 = [('guttagonol', 150), ('grimpex', 300)]
    drugDelayList300 = [('guttagonol', 150), ('grimpex', 450)]

    totalVirusPopEachTimeStep0 = simulationTreatWithTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                              mutProb, numTrials, totalTimesteps, drugDelayList0)

    totalVirusPopEachTimeStep75 = simulationTreatWithTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                              mutProb, numTrials, totalTimesteps, drugDelayList75)

    totalVirusPopEachTimeStep150 = simulationTreatWithTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                              mutProb, numTrials, totalTimesteps, drugDelayList150)

    totalVirusPopEachTimeStep300 = simulationTreatWithTwoDrugs(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                              mutProb, numTrials, totalTimesteps, drugDelayList300)


    threshold = 50
    numCured0, curedFraction0 = getCuredFraction(totalVirusPopEachTimeStep0, threshold)
    numCured75, curedFraction75 = getCuredFraction(totalVirusPopEachTimeStep75, threshold)
    numCured150, curedFraction150 = getCuredFraction(totalVirusPopEachTimeStep150, threshold)
    numCured300, curedFraction300 = getCuredFraction(totalVirusPopEachTimeStep300, threshold)
    print(str(curedFraction0))
    print(str(curedFraction75))
    print(str(curedFraction150))
    print(str(curedFraction300))

    plotAll(totalVirusPopEachTimeStep0, totalVirusPopEachTimeStep75, totalVirusPopEachTimeStep150, totalVirusPopEachTimeStep300)


simulationTwoDrugsDelayedTreatment(400)
# x = [0, 75, 150, 300]
# y = [0.84, 0.44, 0.11, 0.07]
# pylab.figure()
# pylab.plot(x, y)
# pylab.show()