Here are detailed notes on how to find the polarizability of any dye molecule using *ab initio* DFT and TDDFT.

### Step 1: Original .xyz File Creation
Using Avogadro2, a free software you can download on your machine, you draw your desired dye molecule. You should then optimize its shape. For the Mac, on the toolbar, go to Extensions > Open Babel > Optimize Geometry. This optimization algorithm uses what is called a Universal Force Field. The parameters used to generate the Universal Force Field include a set of hybridization dependent atomic bond radii, a set of hybridization angles, van der Waals parameters, torsional and inversion barriers, and a set of effective nuclear charges (https://pubs.acs.org/doi/abs/10.1021/ja00051a040).

Once it is optimized, we then need to export the geometry as a `.xyz` file. On Mac, go to File > Export > Molecule > Save as `.xyz`.

### Step 2: Directory Generation on HPC
Copy `dirGeneration.sh` (shown below) to your research directory that you plan to store your dye molecule project. 
<details>
<summary>dirGeneration.sh</summary>
<br>
<code>
#!/bin/bash

# Prompt the user for the molecule name
echo "Enter the name of your desired molecule:"
read molecule_name

# Check if the molecule name is empty
if [ -z "$molecule_name" ]; then
  echo "Molecule name cannot be empty. Exiting."
  exit 1
fi

# Create a directory with the molecule name
mkdir "$molecule_name"

# Check if the directory creation was successful
if [ $? -ne 0 ]; then
  echo "Failed to create the directory. Exiting."
  exit 1
fi

# Copy template files into the directory with the molecule name
cp -r /home/bldrdge1/data/Plasmon-Dye/polarizabilities/templateDir/* "$molecule_name"

# Check if the copy operation was successful
if [ $? -ne 0 ]; then
  echo "Failed to copy template files. Exiting."
  exit 1
fi

# Rename $MOLECULE$.in to lowercase molecule name.in
mv "$molecule_name/MOLECULE.in" "$molecule_name/${molecule_name,,}.in"

# Replace #MOLECULE# with the lowercase molecule name in each file
for file in "$molecule_name"/*; do
  if [ -f "$file" ]; then
    sed -i "s/#MOLECULE#/${molecule_name,,}/g" "$file"
  fi
done

echo "Directory for $molecule_name created with template files, and replacements completed."
echo "You will need to create an .xyz file detailing the coordinates of the atoms in your dye molecule."
echo "We recommend using Avogadro2."

</code>
</details>

This code, once turned into an executable using `chmod +x dirGeneration.sh` and executed, will ask you for the name of your desired dye molecule and will generate a directory with all the required files for the project.

Lastly, you will need to add your `.xyz` file into the directory under the name `MOLECULE.xyz` where molecule is the lowercase name of your molecule (the same name you used to generate the dir).

One edit needs to be made: in `opt.nw`, you need to input your scratch directory. Usually, this can be found by imputting your username as the #USER# part of the path in `opt.nw`.

### Step 3: DFT Optimization and TDDFT Excitations (using NWChem)

Now, we will need to run the `submit.cmd` file generated in Step 2. It should work without any changes made to your directory (as long as you remembered to include your `.xyz` file). This is the longest computational step you will have to take.

As a result, this should output three files and one directory:
* `opt_log.err` which should be blank if everything ran correctly, 
* `opt_log.out` which should be blank if everything ran correctly, 
* `opt.out` which should include the output of the DFT code.
* `perm/` which should contain many files on your molecule, included two important ones: `MOLECULE.civecs_singlets` and `MOLECULE.dipole_mo`.

### Step 4: CI Vector Coupling (using NWspec)
Once we have the CI vectors generated (in the `perm/` dir), we use `submit_nwspec_1.cmd` to run the couplings between all CI vectors. 

As a result, this should generate three files:
* `MOLECULE_coupl_log.err` which should be blank if everything ran correctly, 
* `MOLECULE_coupl_log.out` which should be blank if everything ran correctly, 
* `MOLECULE_couplings.dat` which should include the output of the coupling code.

### Step 5: Polarizability Generation (using NWspec)
Lastly, we are now only step short of being done. In the `pol.in` file, you should see a value for `absorption_rate`. This requires an eV guess. We look at experimental absorption spectra of the dye molecule, find the main peak, find the eV of the start wavelength and the eV of the end wavelength of the peak, then take the difference. For example, Pyridine has a peak between roughly 230 nm (5.3906 eV) and 260 nm (4.7686 eV), thus the `absorption_rate = 0.622`.

Now that we are set up, we use `submit_nwspec_2.cmd` to submit our `pol.in` file and calculate the polarizabilities. As a result, this should generate three files:
* `MOLECULE_pol_log.err` which should be blank if everything ran correctly, 
* `MOLECULE_pol_log.out` which should be blank if everything ran correctly, 
* `pol_log.out` which should include the output of the polarizability code.

