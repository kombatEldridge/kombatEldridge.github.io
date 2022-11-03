# Multilayer Project Methodology Notes

This blog post is intended to document my processes regarding the DDSCAT Multilayer Project. The processes become tedious and some are small, so I will try to provide step by step descriptions of what to do.

## Project Set Up

In joining with the Freed-Hardeman University Computational Chemistry research group, my collegues and I are investigating the interaction of a multilayered Gold (Au) nanoparticle with light of varying wavelengths. Specifically, we are examining a nanoparticle with a Au core and a Au shell separated by a layer of glass (SiO<sub>2</sub>). 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/kombatEldridge/kombatEldridge.github.io/blob/main/pictures/AuSiO2AuDiagram.png?raw=true">
</p>

# **Chapter 1: Outer Sphere**
# Section 1: Job Submission
## Step 1: Preparing the Shape File
We begin by preparing the shape file to describe the structure to the DDSCAT program. This preparation is complicated for a multi-layered, multi-materialed sphere, so we use Dr. Elise Chaffin's modified shape program (that originally produced nanostar shape files). Through this step process, we will gather a list of all files required for this process.
```
> ./nanostar3
```
Note: inputs ask for diameter, but you should put in radii in $10\, \times$ nanometers (ex. an outer sphere with a $25nm$ radius is entered as $250$).

Lattice spacing is typically $1$. Enter three lines of $1$ to give value to the x, y, and z lattice spacing.

This script will produce a `shape.dat` file.

## Step 2: Dielectric Files
Before we set up the `ddscat.par` file, we need to import any dielectric text files we will be using for our layers. In this project, we need two: `Au_diel.tab` and `SiO2_diel.tab`. These are tab separated files and can be found in many directories. The dielectric files for this project are sourced from Johnson and Christy 1972 and I. H. Malitson 1965 respectively.

## Step 3: DDSCAT Set Up
When we run the ddscat job, we give it a file containing instructions on how to run our job. The `ddscat.par` file contains a lot of lines, but we are only interested in a few. You should copy someone's `ddscat.par` file into your directory and run the following command to begin editing (or use another editor if you prefer):
```
> emacs ddscat.par
```

We are interested in the following sections:

This portion contains the reference to the dielectric files. Make sure you have these files in the same directory as the `ddscat.par` file you are editing now and that they are spelled correctly here.
```
3         = NCOMP = number of dielectric materials
'Au_diel.tab' = file with refractive index 1
'SiO2_diel.tab' = file with refractive index 2
'Au_diel.tab' = file with refractive index 3
```

This effective radii section must contain the correct value. To calculate this value, you find the total radius of the sphere and convert it to microns (micrometers). In this snippet, the radius is $25nm$ = $0.0250 \mu m$
```
'**** Effective Radii (micron) **** '
0.0250 0.0250 1 'LIN' = eff. radii (first, last, how many, how=LIN,INV,LOG)
```

In order to exit the emacs editor, hold CTRL and type x then c (C-x C-c). This exits and askes you to save as well.

## Step 4: SBATCH Preparation and Execution
Now, we are ready almost ready for our first job! However, we need to tell HPC how we want our job ran. We use the `submit_varylamdaddscatnew_array.sh` script. The following changes need to be made to this script:

We need to change the array values to whatever our desired wavelength range is. Here, we are designating our job to run from wavelength $400nm$ to $900nm$ with steps of $10nm$.
```
> emacs submit_varylamdaddscatnew_array.sh

#!/usr/bin/csh
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --mem=50000
#SBATCH --job-name=ddscat
#SBATCH --partition=computeq
#SBATCH --out=dd_scat_%A_%a.out
#SBATCH --array=400-900:10
...
```

Finally, we are ready to run the first job with the following command:
```
> sbatch submit_varylamdaddscatnew_array.sh
```

If you are curious about your job's progress, type:
```
> squeue | grep <your_username>
```
# Section 2: Post Processing
## Step 5: Post Processing Scripts

While your files are running, you can prepare the post processing scripts. 

### ddpostprocess_radial.par

The first of which is the `ddpostprocess_radial.par` that sits in your **files** directory.

Here, we need just need to edit the radius at which the Near Field is measured. We standardly measure NF at $1nm$ off the surface. For a sphere of radius $25nm$ we measure NF at $0.025\mu m + 0.001\mu m = 0.0260\mu m$
```
0.0  0.0  0.0  0.0260      = xorig(1), yorig(1), zorig(1), Rsurf(1) in physical units
```

### submit_ddpost_radial2_EXTNF_multi.sh
In order to submit the post processing file, we edit the `submit_ddpost_radial2_EXTNF_multi.sh` file. Make sure to have the same array here as you did for [Step 4](#step-4-sbatch-preparation-and-execution).
```
> emacs submit_ddpost_radial2_EXTNF_multi.sh 

#!/usr/bin/sh
#SBATCH --cpus-per-task=8
#SBATCH --nodes=1
#SBATCH --mem=32000
#SBATCH --job-name=ddscat_double
#SBATCH --partition=computeq
#SBATCH --out=dd_scat_%A_%a.out
#SBATCH --array=400-900:10
...
```

Once the `ddscat.par` job is finished, you can execute this file using the following command:
```
> sbatch submit_ddpost_radial2_EXTNF_multi.sh
```

### average_Esphere_python3.py
Lastly, once the `submit_ddpost_radial2_EXTNF_multi.sh` jobs are done, we then need to extract the data points from the individual **lam_** folders. We extract the NF data using `average_Esphere_python3.py` making sure that the start, stop, and step are the same as our job's specifications.
```
> emacs average_Esphere_python3.py

...
start=400
stop=900
step=10
...
```

Then execute the script:
```
> python average_Esphere_python3.py
```
### average_EXTABS_sphere_python3.py
Similarly, we need to edit `average_EXTABS_sphere_python3.py` to add the correct start, stop, and step.
```
> emacs average_EXTABS_sphere_python3.py

...
start=400
stop=900
step=10
...
```

Then execute the script:
```
> python average_EXTABS_sphere_python3.py
```

## Step 6: Rename Output Files
You will be running the same post processing scripts next chapter, and they will output files with the same name (which will overwrite the ones you have just created).

Therefore, we need to rename these files to give them a more descriptive name:
```
> mv average_Esphere.txt outer_sphere_average_Esphere.txt
> mv average_EXTABS_sphere.txt outer_sphere_average_EXTABS_sphere.txt
```

## Step 7: Combine Output Files
This step is optional, but it is nice to consolidate the columns in the two outfiles that we actually use in analysis into one file. We use a simple script that accomplishes this task: `combineEsphereEXTABS.py`. This script does not need to be edited unless your directory is not of the format `xcore/ynm-Au_znm-SiO2/`. In that case, just comment out the lines indicated in the script.

Then execute the script:
```
> python combineEsphereEXTABS.py
```

---
# **Chapter 2: Inner Sphere**
# Section 1: Job Submission
## Step 1: ddpostprocessing editing

In order to take measurements now at the inner sphere's surface, we need to change the radius at which the data is collected. To do that, we need to edit `ddpostprocess_radial.par` and reduce the radius. Here, our core has a radius of $10nm$, so we measure NF at $0.011\mu m$.
```
> emacs ddpostprocess_radial.par

0.0  0.0  0.0  0.0110      = xorig(1), yorig(1), zorig(1), Rsurf(1) in physical units
```

The submission of this change is simple:
```
> sbatch submit_ddpost_radial2_EXTNF_multi.sh
```

## Step 2: Create, Rename, and Combine Output Files

This step is the same as Steps 5-7. Make sure that your output files have already been renamed, and then we can run the following scripts:

```
> python average_Esphere_python3.py
> python average_EXTABS_sphere_python3.py
> mv average_Esphere.txt inner_sphere_average_Esphere.txt
> mv average_EXTABS_sphere.txt inner_sphere_average_EXTABS_sphere.txt
> python combineEsphereEXTABS.py
```

---
# **Chapter 3: Image Creation (Optional)**
## Section 1: Mayavi Images
Refer to [this blog](https://kombateldridge.github.io/2022/10/22/Au-SiO2-Au-Gif-Creation-Notes.html).

## Section 2: Spectra Images
Currently, I am using a Jupyter Notebook on the HPC ([Tutorial](https://kombateldridge.github.io/2022/07/01/Jupyter-Notebook-On-HPC.html)) to manually pull all the data into graphs of my choosing. However, I have plans to make this process simpler by using a database containing the data and the metadata about each job and a connection to a Jupyter Notebook coded for image processing. That way, you can command (via SQL) what data you want to compare and have the Notebook visualize the data quickly. Here is a blog I am keeping updated on my progress: [Au-SiO2-Au Multilayered Nanoparticle Project](https://kombateldridge.github.io/2022/09/09/Au-SiO2-Au-Multilayer-Project-Update-1.html).




# ***File Structure***:
- Job Directory (named `/xcore/ynm-Au_znm-SiO2/`)
  - [submit_varylamdaddscatnew_array.sh](#step-4-sbatch-preparation-and-execution)
  - [submit_ddpost_radial2_EXTNF_multi.sh](#submit_ddpost_radial2_extnf_multish)
  - [average_Esphere_python3.py](#average_esphere_python3py)
  - [average_EXTABS_sphere_python3.py](#average_extabs_sphere_python3py)
  - [combineEsphereEXTABS.py](#step-7-combine-output-files)
  - `Files` Directory
    - [nanostar3.sh](#step-1-preparing-the-shape-file)
    - [Au_diel.tab](#step-2-dielectric-files)
    - [SiO2_diel.tab](#step-2-dielectric-files)
    - [ddscat.par](#step-3-ddscat-set-up)
    - [ddpostprocess_radial.par](#ddpostprocess_radialpar)