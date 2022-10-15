# Au - SiO<sub>2</sub> - Au Multilayered Nanoparticle Project

In joining with the Freed-Hardeman University Computational Chemistry research group, my collegues and I are investigating the interaction of a multilayered Gold (Au) nanoparticle with light of varying wavelengths. Specifically, we are examining a nanoparticle with a Au core and a Au shell separated by a layer of glass (SiO<sub>2</sub>). 

<p align="center" width="100%">
    <img width="50%" src="https://github.com/kombatEldridge/kombatEldridge.github.io/blob/main/pictures/AuSiO2AuDiagram.png?raw=true">
</p>


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
We begin by proprocessing the raw data to be better fit into the *mySQLWorkbench* software. The *.txt* files from the research group were extracted from the HPC, organized in folders by experiment, combined for both inner sphere and outer sphere measurements, and then combined completely into one master *.txt* file containing rows for wavelength ($\lambda$), $Q_{ext}$, $Q_{sca}$, $Q_{abs}$, $E^2$, and experimental conditions. Finally, the master file was split into two files, one containing the results columns, and the other containing the experimental conditions. Both contain a column for the expID which is the foreign key for the results table referencing the conditions table where it is the primary key. All preprocessing was done through multiple *.py* scripts.

### SQL Schema
Our schema is a simple one. We have the option to track more meta data about our experiments (who ran it, when it was ran, configuration file, etc.), but they are not important to our analysis. Perhaps I will add this capability in the future.

<iframe width="100%" height="500px" style="box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); border-radius:15px;" allowtransparency="true" allowfullscreen="true" scrolling="no" title="Embedded DrawSQL IFrame" frameborder="0" src="https://drawsql.app/teams/brintons-team/diagrams/multilayer/embed"></iframe>

### SQL Implimentation
The two text files produced from the preprocessing contain the data for the two tables in the database. I used the *mySQLWorkbench* upload wizard. Now, the two tables are in the database and the tables have been initialized to related to one another.

---

## Future Work

### Deliverables
Next month, I plan on testing the database with my deliverables from the proposal. Below is the original list of deliverables. I expect that things will go well.

1. Retrieve all data points of type \textit{x} given $n$ experimental parameters $[a_1, a_2, a_3, ..., a_n]$. For example, the database is able to return a matrix of data after a user desires to compare the $Q_{ext}$ data points of all experiments with a Au core size $= 5$ nm. However, we also expect the database to handle data requests with multiple data point types and multiple experimental parameters.
2. Add additional data points after a new experiment has been run. We expect to compile more data from future experiments and would like to add them to the database.
3. This is just an idea, but it would be ideal to have the database do some preprocessing on the raw data files. However, right now, the user is responsible for the preprocessing.
\end{enumerate}

### Jupyter Notebook Implementation
All research analysis is done on a Jupyter Notebook server hosted on the HPC. Ideally, I am able to connect the mySQL server to a Jupyter Notebook in order to be an interface of retrieval (Deliverable 1) and preprocessing (Deliverable 3).

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