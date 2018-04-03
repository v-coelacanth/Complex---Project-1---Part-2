

README For Project 1

How to run the code. 

Figure 1 and Mutual Information

Matlab scripts to create figure 1 and to create the data files for estimating mutual information are in the directory Matlab for Figure 1.  

To create figure 1 and the data files for the JIDT mutual information binning algorithm, run the Matlab script figure1abcd_combined_with_mi.  This creates files test_mi_cd.txt and test_mi_cd.txt which you can feed to the JIDT AutoAnalyzer. 

To create the data files for JIDT kernel estimator, run the Matlab script part1abcd_kernal. This creates the data files test_kernal_ab.txt and test_kernal_cd.txt which you can feed to the JIDT AutoAnalyzer. 

Figure 2

The code for making the return map (Figure 2) s in the directory Python Version of Pretty Picture.   It is written in Python 3 and requires that Numpy and Matplotlib be installed.  To run the code, issue the command python3 lattice.py and go get a cup of coffee.  The code takes about 4 minutes to run.  



FIGURES 3 and 4 - Kellin Rumsey

R_Code folder contains two files
   -Project1_Functions.R
   -Project1_Script.R

You will just need to run the Project1_Script.R function. There are just two things to be aware of.
   1. You will need to install two libraries (tidyverse and TransferEntropy). There are two lines
      in the Project1_Script.R file which will do this for you if commented out. 
   2. Since I was averaging over many runs to produce Figure 4b, the script can take hours (~8) to run.
      To avoid this, I have put in a more managable set of parameters (i.e. Smaller N and less time steps).
      This will let you run the code quickly (a minute or two), but won't reproduce my figures exactly (obviously).
      The full inputs which I ran are included but are currently commented out.

Cheers!