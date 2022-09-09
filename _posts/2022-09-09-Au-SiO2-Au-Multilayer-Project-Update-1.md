# Au - SiO<sub>2</sub> - Au Multilayered Nanoparticle Project

In joining with the Freed-Hardeman University Computational Chemistry research group, my collegues and I are investigating the interaction of a multilayered Gold (Au) nanoparticle with light of varying wavelengths. Specifically, we are examining a nanoparticle with a Au core and a Au shell separated by a layer of glass (SiO<sub>2</sub>). 


![Multilayer Diagram](/pictures/AuSiO2AuDiagram.png){:height="236px" width="236px"}.

---

## Experimental Procedure

### Independent Variables
Using the DDSCAT program on the University of Memphis's HPC, the research group has run in total **<ins>78</ins>** different experiments. Each experiment had one or multiple of the following parameters modified:
- Au Core Size: the radius of the Au core in nm.
- SiO<sub>2</sub> Layer Size: the width of the SiO2 layer in nm.
- Au Shell Size: the width of the Au outer layer in nm.
- Inner Layer/Outer Layer: identifies wether the measurements are taken at the surface of the core or the surface of the Au shell.

A table of all experimental conditions computed can be found at the end of the page. Each experiment computed results for both the inner layer and outer layer.

### Dependent Variables
Each experiment returns multiple arrays of data. From the inner and outer layer, we collect data in the form of $Q_{ext}$, $Q_{sca}$, $Q_{abs}$, and $E^2$ for a list of wavelengths (usually 400nm to 1000nm). These measurements are unitless.

---

## Analytical Procedure

Analyzing $78\times4 = 312$ columns of data can be cumberson. However, I am enrolled an a database systems class. Therefore, in an effort to kill two birds with one stone, we will create a database of all the datapoints. This method can be tough to initialize, but once the ball is rolling, a simple query for any combination of experimental parameters will yeild the data set we wish to analyze with eaze.

### Preprocessing
We begin by proprocessing the raw data from the HPC to be better fit into some database managment software. The *txt* files from the research group were extracted from the HPC, organized in folders by experiment, combined for both inner sphere and outer sphere measurements, and then combined completely into one *txt* file containing rows for wavelength, $Q_{ext}$, $Q_{sca}$, $Q_{abs}$, $E^2$, and Experimental Parameters. All preprocessing was done through multiple *.py* scripts.

### SQL Schema
Insert Schema image here.

### SQL Implimentation
Currently, the data has not been implimenting into an SQL server.

---

### Experiments Conducted

| Au Core Size | SiO<sub>2</sub> Layer Size | Au Shell Size |
| ----------- | ----------- | ----------- |
| 5nm | 5nm | 17.5nm |
| 5nm | 6nm | 16.5nm |
| 5nm | 7nm | 15.5nm |
| 5nm | 8nm | 14.5nm |
| 5nm | 9nm | 13.5nm |
| 5nm | 10nm | 12.5nm |
| 5nm | 15nm | 7.5nm |
| 10nm | 5nm | 15nm |
| 10nm | 6nm | 14nm |
| 10nm | 7nm | 13nm |
| 10nm | 8nm | 12nm |
| 10nm | 9nm | 11nm |
| 10nm | 10nm | 10nm |
| 10nm | 15nm | 5nm |
| 10nm | 17.5nm | 2.5nm |
| 15nm | 5nm | 12.5nm |
| 15nm | 6nm | 11.5nm |
| 15nm | 7nm | 10.5nm |
| 15nm | 8nm | 9.5nm |
| 15nm | 9nm | 8.5nm |
| 15nm | 10nm | 7.5nm |
| 15nm | 11nm | 6.5nm |
| 15nm | 12nm | 5.5nm |
| 15nm | 13nm | 4.5nm |
| 15nm | 14nm | 3.5nm |
| 15nm | 15nm | 2.5nm |
| 20nm | 10nm | 2.5nm |
| 20nm | 10nm | 7.5nm |
| 20nm | 10nm | 10nm |
| 20nm | 10nm | 12.5nm |
| 25nm | 3.5nm | 9nm |
| 25nm | 4.5nm | 8nm |
| 25nm | 5nm | 7.5nm |
| 25nm | 5.5nm | 7nm |
| 25nm | 6.5nm | 6nm |
| 25nm | 7.5nm | 5nm |
| 25nm | 8.5nm | 4nm |
| 25nm | 9.5nm | 3nm |
| 25nm | 10.5nm | 2nm |