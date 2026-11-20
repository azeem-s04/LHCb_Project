#%% Import packages
import uproot
#import awkward as ak
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Access data using settings specified in config.py
from pathlib import Path
import os
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
os.chdir(PROJECT_ROOT)

# Add project root to Python's module search path
sys.path.insert(0, str(PROJECT_ROOT))

import config

print("Config imported from:", config.__file__)
print("SAMPLE_DIR available:", hasattr(config, "SAMPLE_DIR"))

from config import SAMPLE_DIR

print("Sample directory:", SAMPLE_DIR)

#%% Locate ROOT data files in specified directory

root_files = sorted(SAMPLE_DIR.glob("*.root"))

print(f"Number of ROOT files: {len(root_files)}")

for file in root_files:
    print(file.name)
    
#%% Open 1st ROOT file and list its contents
root_file = uproot.open(root_files[0]) # "00334560_00000001_1.dvntuple.root"

print("\nROOT file contents:")
print(root_file.keys())

#%% Access decay tree / inspect the TTree

DecayTree = root_file["Btree/DecayTree"]

print(DecayTree)
print("\nNumber of entries:", DecayTree.num_entries)

#%% Insect branches (columns, keys) of the TTree

DecayBranches = DecayTree.keys()

print("\nNumber of branches:", len(DecayBranches)) # expect 319 branches

output = SAMPLE_DIR / "branches00.txt" # branches of root_files[0]

with open(output, "w") as file:
    
    for branch in DecayBranches:
        file.write(branch + "\n")

print(f"Saved branch list to: {output}" )

#%% Selecting relevant branches

# Opening as Awkward Arrays

# For J/Psi m_inv:
    
muplus_PE = DecayTree["muplus_PE"].array() # default=awk, i.e. highlevel.Array

muplus_PX = DecayTree["muplus_PX"].array()
muplus_PY = DecayTree["muplus_PY"].array()
muplus_PZ = DecayTree["muplus_PZ"].array()

muminus_PE = DecayTree["muminus_PE"].array()

muminus_PX = DecayTree["muminus_PX"].array()
muminus_PY = DecayTree["muminus_PY"].array()
muminus_PZ = DecayTree["muminus_PZ"].array()

#%% Squared invariant dimuon mass calculation

muplus_P = np.sqrt((muplus_PX**2) + (muplus_PY**2) + (muplus_PZ**2))
muminus_P = np.sqrt((muminus_PX**2) + (muminus_PY**2) + (muminus_PZ**2))

energy_squared = (muplus_PE + muminus_PE)**2

momenta_squared = (
    (muplus_PX + muminus_PX)**2
    + (muplus_PY + muminus_PY)**2
    + (muplus_PZ + muminus_PZ)**2
    )

minv_dimuon_squared = energy_squared - momenta_squared

minv_dimuon = np.sqrt(minv_dimuon_squared)

#%% Comparing our calculation with CERN's invariant mass
Jpsi_MM = DecayTree["J_psi_1S_MM"].array() # reconstructed mass
Jpsi_M = DecayTree["J_psi_1S_M"].array() # kinematically-calculated mass (I guess?)

delta = minv_dimuon - Jpsi_MM
print(np.max(delta)) # 80 MeV, about 2.7%

# Our calculations may disagree because the muon momenta and J/psi momenta
# are calculated at different stages in the decay process. If this was a proper
# analysis instead of an intro, maybe we would need to use some algorithm to
# extrapolate the dimuon trajectories back to the decay vertex, and use those
# values instead.

# Instead, I will just use J_psi

#%% Plotting J_psi_1S_M histogram

hist_kwargs = {
    'x' : Jpsi_M,
    'bins' : 200,
    'range' : (2950, 3200),
    }

plt.hist(**hist_kwargs)
plt.title("$J/\Psi$ candidate mass")
plt.xlabel("$m_{J/\psi}$ [MeV]")
plt.ylabel("candidates")

plt.savefig(PROJECT_ROOT / "figures" / "jpsi_mass.png",
            dpi=600, bbox_inches="tight")

plt.show()

#%% Origin plot
# I prefer plotting in Origin than with pyplot.
# Export JPsi_M as .txt:

Jpsi_data = PROJECT_ROOT / "data" / "2016_MagDown" / "Jpsi_M.txt" 
# branches of root_files[0]

with open(Jpsi_data, "w") as file:
    
    for entry in Jpsi_M:
        file.write(f"{entry}\n")

print(f"Exported array to: {Jpsi_data}" )
