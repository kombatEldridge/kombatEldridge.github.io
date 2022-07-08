# Calculating Light Scattering, Absorption, and Near Field Enhancement in a Multilyered Sphere using Mie Theory

*Code inspired by "Improved recursive algorithm for light scattering by a multilayered sphere" from Applied Optics Yang 2003*

## Section 1: Background Information
This walkthrough aims to teach the reader about a recursive algorithm developed by [Wen Yang](https://opg.optica.org/ao/abstract.cfm?uri=ao-42-9-1710) on the topic as well as the addition of a Near Field Enhancement calculation to the system.

This algorithm has been developed to apply Mie Theory [^j] to a multilayered sphere. The algorithm works only for layered spheres, and will not correctly interpret any other morphology. The image below shows an example of concentric layers of spheres as one unit. 
![Multilayer Diagram](/pictures/multilayerimg.png)
### Dielectric File
The user must have a text file containing the dielectric/refractive index information for the materials in the multilayered sphere. Because the code in its current state will only search through one dielectric file, there should only be one wavelength column (example below). This file must be placed in the same directory as the code.
![Dielectric Example](/pictures/diel_img.png)
The script has the capability to interpolate between these wavelengths if your dielectric file has asymmetric gaps. 

## Section 2: Script Use
The script will prompt the user for information about the system to be analyzed.

**Question 1: How many layers?**

Input how many layers in total the system has. This must be an integer greater than 1. If the user wants to run a homomaterial system, just input two or more layers and when asked their radii, let the outermost radius be the true radius and assign the other radii values smaller than the first. Finally, just assign the same dielectric to every shell to get a homomaterial system.

**Question 2: What is the radius of each layer?**

Input, starting with the innermost core layer, the outer radius measurement of each layer in **nm**. These can be float values (with decimals).

**Question 3: What columns of the dielectric file are for each layer?**

Input, starting with the innermost core layer, the column index (where the first column of wavelengths is indexed at 0) for the real and imaginary component of the refractive index of each layer's material. Ex: for the image above, the columns for silver (Ag) are 1 and 2.

**Question 4: How would you like to have your wavelength intervals from your dielectric file?**

Choose between two options:

1. Keep your original wavelengths and their intervals.
2. Ask the script to linearly interpolate wavelengths inbetween the original wavelengths.

**Question 4b: What is your deisred interval?**

If the user answered 2 to question 4, they will be asked to specify what interval between the wavelengths they would like the script to produce. By hitting `Enter/Return`, the user chooses to default the interval to 1nm. However, the user can input any float value.

## Section 3: Output File

The script will begin to calculate multiple data points for each wavelength. The output file will be a text file containing a header row, columns for each data point, and a row for each wavelength.

![Output File](/pictures/output_img.png)

The outputs are as follows:

- Column 0: Lambda/Wavelength
- Column 1: Qext
- Column 2: Qsca
- Column 3: Qabs
- Column 4: Cext
- Column 5: Csca
- Column 6: Cabs
- Column 7+: Near Field Enhancement for each layer

---
The script for this project can be found (here)[https://github.com/kombatEldridge/kombatEldridge.github.io/blob/d3715b8c9c1276d6e54b2d4db2f5290a6719a634/Mie_Multilayer.ipynb]

[^j]: Describes the scattering of light by a non-absorbing, partially-absorbing, or perfectly conducting sphere.