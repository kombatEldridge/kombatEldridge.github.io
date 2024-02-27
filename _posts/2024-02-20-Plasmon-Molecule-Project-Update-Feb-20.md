### Progress on GitHub

Because I am hoping to get hired in the computer science field when I'm done here, I think its best if my progress is written in the language of the people. Thus, I have a private repo of my work on GitHub. Some parts of the project need to be hidden from the repo because they are Dr. Nascimento's work (*Bohr*) and I want to respect his work without accidentally publishing something private. That being said, when the project is done, I will release the repo as public to be seen by the masses. 

### Workflow
As I have combined Bohr and Meep into one project, I have created this chart to keep track of the overall workflow of the code.
[![](https://mermaid.ink/img/pako:eNqdVU1v2kAQ_SsjS6iXpCHqjUOlFCeEEGgEuVR2Dos9xqusd639aEKB39E_01vv_U0drwGbQFuplpDwzpud92berldBolIMekGnAysuue3BKg4yoV6SnGkbB_49t4W4Z3MUplrImDC42cCm04nlHgqPYSxh-1xFIWZcIsyU0wk-NZFPu8gAVYFWL1ux_i7WRyFa6-FufYpGCWe5kq3o9S46VgITJ9rVbqIhaeJM8G_EhRdOsDfZV3B-_nH9IJjEF_YV4cGROFAZDJgzhjNZK1jDTUuDz5mVOWqeMAFXDiZMqpK6wBNxiO17bPf9Jfz6UcDP73D89wAfevxlt9uFkr9Sx6FEfYS69qgplhoNSospzJfQd8aqosW31YcKD4No6uTpNgw84Da66OeYPAPPoIntMQcdgZyZEyCNLMmJDzFL_VjSE6BiOykoleEVkzhucbn14ojCRK1hGMXxBF_JXrxAY7G8eKqpnsB_QbOGu2hWzZF-mi2QOpVxFClw6pKkYssTdHYPs2Bz3LN7Z_b8IFP6L4myImhzjQh2S9N4mmua8gcS0aTeefaj9nBGbZN-UrmuFd43CHZkcb-5M1wugGqjlmRD8h-jI0V2yXjlwlGzwfzNefTpND8uS2ch06po2eIg8z7qq4JATW1qC53DUklT7wNbHlXryF8LPB85axkQlVylaxg3myVRJY82eAzDm0fos5LNuSDtaI40j6PPzlLhHgxl6hLyUchLogA0jYM2wKRJmkRT5E0z2yeCtLatXzOnU5N4eZWAnVX-POd_PQm5f3sYmaSCNe__3y-tFTMwBROCXo1lkqSwF7ZcD4OzoEBdMJ7S_b2qqsQBDaHA6pKOg5Tp5ziI5YZwzFk1W8ok6Fnt8CxwZUpEQ84WZJmg52_0swBTbpUe1x8E_13Y_Aa1ys__?type=png)](https://mermaid.live/edit#pako:eNqdVU1v2kAQ_SsjS6iXpCHqjUOlFCeEEGgEuVR2Dos9xqusd639aEKB39E_01vv_U0drwGbQFuplpDwzpud92berldBolIMekGnAysuue3BKg4yoV6SnGkbB_49t4W4Z3MUplrImDC42cCm04nlHgqPYSxh-1xFIWZcIsyU0wk-NZFPu8gAVYFWL1ux_i7WRyFa6-FufYpGCWe5kq3o9S46VgITJ9rVbqIhaeJM8G_EhRdOsDfZV3B-_nH9IJjEF_YV4cGROFAZDJgzhjNZK1jDTUuDz5mVOWqeMAFXDiZMqpK6wBNxiO17bPf9Jfz6UcDP73D89wAfevxlt9uFkr9Sx6FEfYS69qgplhoNSospzJfQd8aqosW31YcKD4No6uTpNgw84Da66OeYPAPPoIntMQcdgZyZEyCNLMmJDzFL_VjSE6BiOykoleEVkzhucbn14ojCRK1hGMXxBF_JXrxAY7G8eKqpnsB_QbOGu2hWzZF-mi2QOpVxFClw6pKkYssTdHYPs2Bz3LN7Z_b8IFP6L4myImhzjQh2S9N4mmua8gcS0aTeefaj9nBGbZN-UrmuFd43CHZkcb-5M1wugGqjlmRD8h-jI0V2yXjlwlGzwfzNefTpND8uS2ch06po2eIg8z7qq4JATW1qC53DUklT7wNbHlXryF8LPB85axkQlVylaxg3myVRJY82eAzDm0fos5LNuSDtaI40j6PPzlLhHgxl6hLyUchLogA0jYM2wKRJmkRT5E0z2yeCtLatXzOnU5N4eZWAnVX-POd_PQm5f3sYmaSCNe__3y-tFTMwBROCXo1lkqSwF7ZcD4OzoEBdMJ7S_b2qqsQBDaHA6pKOg5Tp5ziI5YZwzFk1W8ok6Fnt8CxwZUpEQ84WZJmg52_0swBTbpUe1x8E_13Y_Aa1ys__)

### Notes on Workflow
#### Simulating Molecule as Source
Although it is possible to use TDDFT to calculate the polarizability of a molecule under an external field, and it is possible to find dielectric response from polarizability, it does not make much sense to simulate something as small as a single molecule as a material with a dielectric response. Thus, simulating a molecule as a point source will do.

#### Capturing Absorption Spectrum from Molecule 
The TDDFT code assumes that all energy absorbed by the molecule will be re-emitted by it in the form of an induced dipole, we are not able to validate a portion of the simulation by comparing it to experimental absorption spectra.

#### Three Timesteps of E field
Since we need to calculate a derivative of the molecule's wavefunction as it relates to the electric field, we collect three timeframes of electric field. Three is the minimum requirement to perform the Runge-Kutta method of derivation.

#### Time Scale Between Meep and Bohr
You are able to calculate the timestep of Meep by `dT = sim.Courant/resolution`, but this is in units of Meep time. One time unit in Meep is 3.33E-15 seconds. One time unit in Bohr is 2.4188843265857E-17 seconds
so `dTbohr = dT * (333.3333333333333/2.4188843265857)`

#### Nuances of Simulating a Molecule as a Point Source
Though the original incident electric field in Meep will be polarized in one coordinate direction (default: `z`), the objects simulated are three-dimensional, so their field response will illicit electric fields in all three directions. All that being said, the electric field collection at the position of the molecule needs to survey all three direction components and pass each into Bohr individually. ([#1](https://github.com/kombatEldridge/plasmonMolecule/issues/1))

According to Physics, the electric field due to a point dipole will irradiate in a spherical fashion, but the strength along that sphere will not be equal. We need to create an overall dipole moment from Bohr's calculations and use the equation the issue cited below to find the field strength at every point on the sphere. ([#2](https://github.com/kombatEldridge/plasmonMolecule/issues/2))