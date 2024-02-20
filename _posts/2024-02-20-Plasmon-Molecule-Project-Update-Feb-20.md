### Progress on GitHub

Because I am hoping to get hired in the computer science field when I'm done here, I think its best if my progress is written in the language of the people. Thus, I have a public repo of my work on Github [here](https://github.com/kombatEldridge/plasmonMolecule). Some parts of the final product will be hidden from the repo because they are Dr. Nascimento's work (*Bohr*) and I want to respect his work without accidentally publishing something private. 

### Workflow
As I have combined Bohr and MEEP into one project, I have create this chart to keep track of the overall workflow of the code.
[![](https://mermaid.ink/img/pako:eNqdVU1v2kAQ_SsjS6iXpCHqjUOlFCeEEGgEuVR2Dos9xqusd639aEKB39E_01vv_U0drwGbQFuplpDwzpud92berldBolIMekGnAysuue3BKg4yoV6SnGkbB_49t4W4Z3MUplrImDC42cCm04nlHgqPYSxh-1xFIWZcIsyU0wk-NZFPu8gAVYFWL1ux_i7WRyFa6-FufYpGCWe5kq3o9S46VgITJ9rVbqIhaeJM8G_EhRdOsDfZV3B-_nH9IJjEF_YV4cGROFAZDJgzhjNZK1jDTUuDz5mVOWqeMAFXDiZMqpK6wBNxiO17bPf9Jfz6UcDP73D89wAfevxlt9uFkr9Sx6FEfYS69qgplhoNSospzJfQd8aqosW31YcKD4No6uTpNgw84Da66OeYPAPPoIntMQcdgZyZEyCNLMmJDzFL_VjSE6BiOykoleEVkzhucbn14ojCRK1hGMXxBF_JXrxAY7G8eKqpnsB_QbOGu2hWzZF-mi2QOpVxFClw6pKkYssTdHYPs2Bz3LN7Z_b8IFP6L4myImhzjQh2S9N4mmua8gcS0aTeefaj9nBGbZN-UrmuFd43CHZkcb-5M1wugGqjlmRD8h-jI0V2yXjlwlGzwfzNefTpND8uS2ch06po2eIg8z7qq4JATW1qC53DUklT7wNbHlXryF8LPB85axkQlVylaxg3myVRJY82eAzDm0fos5LNuSDtaI40j6PPzlLhHgxl6hLyUchLogA0jYM2wKRJmkRT5E0z2yeCtLatXzOnU5N4eZWAnVX-POd_PQm5f3sYmaSCNe__3y-tFTMwBROCXo1lkqSwF7ZcD4OzoEBdMJ7S_b2qqsQBDaHA6pKOg5Tp5ziI5YZwzFk1W8ok6Fnt8CxwZUpEQ84WZJmg52_0swBTbpUe1x8E_13Y_Aa1ys__?type=png)](https://mermaid.live/edit#pako:eNqdVU1v2kAQ_SsjS6iXpCHqjUOlFCeEEGgEuVR2Dos9xqusd639aEKB39E_01vv_U0drwGbQFuplpDwzpud92berldBolIMekGnAysuue3BKg4yoV6SnGkbB_49t4W4Z3MUplrImDC42cCm04nlHgqPYSxh-1xFIWZcIsyU0wk-NZFPu8gAVYFWL1ux_i7WRyFa6-FufYpGCWe5kq3o9S46VgITJ9rVbqIhaeJM8G_EhRdOsDfZV3B-_nH9IJjEF_YV4cGROFAZDJgzhjNZK1jDTUuDz5mVOWqeMAFXDiZMqpK6wBNxiO17bPf9Jfz6UcDP73D89wAfevxlt9uFkr9Sx6FEfYS69qgplhoNSospzJfQd8aqosW31YcKD4No6uTpNgw84Da66OeYPAPPoIntMQcdgZyZEyCNLMmJDzFL_VjSE6BiOykoleEVkzhucbn14ojCRK1hGMXxBF_JXrxAY7G8eKqpnsB_QbOGu2hWzZF-mi2QOpVxFClw6pKkYssTdHYPs2Bz3LN7Z_b8IFP6L4myImhzjQh2S9N4mmua8gcS0aTeefaj9nBGbZN-UrmuFd43CHZkcb-5M1wugGqjlmRD8h-jI0V2yXjlwlGzwfzNefTpND8uS2ch06po2eIg8z7qq4JATW1qC53DUklT7wNbHlXryF8LPB85axkQlVylaxg3myVRJY82eAzDm0fos5LNuSDtaI40j6PPzlLhHgxl6hLyUchLogA0jYM2wKRJmkRT5E0z2yeCtLatXzOnU5N4eZWAnVX-POd_PQm5f3sYmaSCNe__3y-tFTMwBROCXo1lkqSwF7ZcD4OzoEBdMJ7S_b2qqsQBDaHA6pKOg5Tp5ziI5YZwzFk1W8ok6Fnt8CxwZUpEQ84WZJmg52_0swBTbpUe1x8E_13Y_Aa1ys__)

### Notes on Workflow
#### Simulating Molecule as Source
Although it is possible to use TDDFT to calculate the polarizability of a molecule under an external field, and it is possible to find dielectric response from polariability, it does not make much sense to simulate something as small as a single molecule as a material with a dielectric response. Thus, simulating a molecule as a point source will do.

#### Capturing Absorption Spectrum from Molecule 
The TDDFT code assumes that all energy absorbed by the molecule will be re-emitted by it in the form of an induced dipole, we are not able to validate a portion of the simulation by comparing it to experimental absorption spectra.

#### Three Timesteps of E field
Since we need to calculate a derivative of the molecule's wavefunction as it relates to the electric field, we collect three timeframes of electric field. Three is the minimum requirement to perform the Runge-Kutta method of derivation.

#### Time Scale Between Meep and Bohr
You are able to calculate the timestep of Meep by `dT = sim.Courant/resolution` but this is in units of Meep time. One time unit in meep is 3.33E-15 seconds. One time unit in bohr is 2.4188843265857E-17 seconds
so `dTbohr = dT * (333.3333333333333/2.4188843265857)`

#### Induced Dipole to Electric Field
Since we found it very difficult to calculate the electric field intensity of an electric dipole at its center, we simply calculate the electric field a few picometers from the center of the molecule.
> **NOTE:** this is the plan, but has not been implemented yet.
