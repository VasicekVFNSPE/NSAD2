#! /usr/bin/env python
import ROOT
import pythia8
import sys

print("imaginary error fixed")

print("hello from small-change-higgs")

def random_function(number):
        power = number*number
        print(f"Your number is {number} and your number to the power of 2 is {power}.")
random_function(int(sys.argv[4]))

pythia = pythia8.Pythia("",False)
ConfigVariable=sys.argv[1]
pythia.readFile(ConfigVariable)
JmenoVystupRootu=sys.argv[2]
PocetUdalosti=int(sys.argv[3])
pythia.init()
vystup = ROOT.TFile(f"{JmenoVystupRootu}.root", "RECREATE")
#poradi on_on = ISR_FSR
hist_pT = ROOT.TH1D("pT_off_on", "Higgs pT: ISR on, FSR: on; p_{T} [GeV]; Pocet udalosti", 100, 0, 500)
hist_y = ROOT.TH1D("y_off_on", "Higgs rapidita: ISR on, FSR on; y; Pocet udalosti", 100, -5, 5)
for ievent in range(PocetUdalosti):
	if not pythia.next():
		continue
	lastH = -1
	for index, particle in enumerate(pythia.event):
		if particle.id() == 25:
			lastH = index
	if lastH >= 0:
		hist_pT.Fill(pythia.event[lastH].pT())
		hist_y.Fill(pythia.event[lastH].y())

hist_pT.Write()
hist_y.Write()
vystup.Close()
