This directory contains ROOT datasets required for this project.



The datasets are not included in this repository. They must be obtained separately from CERN.



1. ### Obtaining the data

   * Visit the CERN Open Data Portal.  
   * Locate the LHCb dataset specified in the main project README.
   * Download the ROOT files required for the analysis.



### 2\. Directory structure

After downloading the datasets, organise them as follows:



data/

├── README.md

└── 00334560\_00000001\_1.dvntuple.root

**───** 00334560\_00000002\_1.dvntuple.root



### 3\. Configuring the data location

This analysis code supports a configurable data directory through the LHCB\_DATA\_DIR variable.

By default, the code expects the datasets to be stored in this directory.

If the datasets are stored elsewhere, configure LHCB\_DATA\_DIR to point to their location before running the analysis.



### 4\. Data management

* It is not recommended to upload large datasets to GitHub.
* ROOT datasets are excluded from version control.
* Analysis should be conducted separately from the original datasets.



For information on installing dependencies, refer to the main project requirements.txt file. For running the analysis, consult the main project README.md file.

