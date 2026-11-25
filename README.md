**Datasets used in this project:**



https://opendata.cern.ch/record/93946 (magnet down, 2016, 2 files, 2.0 GiB)



Datasets are not uploaded to this repository. Please download the open-access files directly from CERN and handle them as specified in the file "data/data\_README.md". I recommend opening any .svg files in a browser such as Google Chrome, if other methods fail to compile the file properly.



This README is a work in progress and will be corrected, re-arranged and built upon as I work through this project.



### J/Psi to dimuon decay

Using CERN record 93946, candidate dimuon products were plotted as a function of invariant mass in bins of width 1 MeV (natural units). The data were in the range 2995-3195 MeV, and there were 1 267 649 candidate events. The relevant notebook is located at "notebooks/01\_data\_access.py" (I used Spyder).



Upon opening the ROOT file, the invariant mass of the dimuon final state was found to not be the same as the recorded J/Psi mass. I put this down to the J/psi and dimuon states being evaluated at different stages in the reconstruction, so they cannot simply be equated. I may need some algorithm to extrapolate daughter trajectories back to the J/psi decay vertex. Therefore, I worked directly with the J/psi masses (branch "J\_psi\_1S\_M" instead of recalculating using mu+, mu- four-momenta. That is why the x-axes for the two plots in "figures/Jpsi\_inv\_mass/" are m\_{J/psi} instead of m{mu mu}.

