*This post copies the earlier [Feb 20th](2024-02-20-Plasmon-Molecule-Project-Update-Feb-20.md) update in form but with updated information.*

### Progress on GitHub

As I work on this project, I am learning more about GitHub and industry use of its tools. My commits to the project are a good way of tracking issues, and if I mess up, I am able to review the changes I made and revert the issue.

### Workflow

The current version of the code employs two input files: a Meep file and a Bohr file.
[![](https://mermaid.ink/img/pako:eNptU8lu2zAQ_ZUBAaMXJbGdyFZ0KJBm34yi6aWVfKClscVWJAUuabz9e8dUGqtBBPCgWd68eTOzZoUukaWs14O1UMKlsM7ZvNZ_ioobl7PwXzlZP_AZ1nZnmPPa4nYL214vV2-h8P0iV_D6nZ1lt6rxDq5EjXa6d1yRXTjBa7FCeERsOr7r7JtX8CSkr7kTWk27eHBw8HljtTcFRqBnv7BwEUhdY-Frsti3LPJ6R6W_Tq43cPUeAjb_cjZw36EVfNcdLsFwkx09IrfeIHBVguXPCJcvEVwu6a1gH84duArf-Hyy0GgrdnTyvNPGTUC9zc4rLH6DmIckpBxnRAFzgXX5HgoqboEEVgssYW60hBUaDbMlMQLeNAYLwWcUx6X2ynWK3QbJqMhEb-Auy_MJvtCUhETrsDmath1-EP8DbWiXmNTU_Y6PQYRCK0uUnCARZKuKROUsMSTLDFEFgUoStqPMfXfgX3Rl2roP-4iH7FxLGth_8glV-oI6LkVDRvBWqEXQhVZkgQf33jlOLFylyxZwsgecZJdSOJpAzY1YhaUgvLBtQGK2S7Tr7oNxtWB3LGISjeSipNNY76BzRtUl7vY_ZyXOua_pOnK1pVDunX5aqoKlzniMmG9K7vBC8IXhkqXhXiKGpXDaPLbnFq4uYg1XLF2zF5YOh8lhPBydxsdxchwPBsk4YkuWxv3D0TA-TeL4ZDRKxsl4G7GV1oQ6OByMk-T0OOmfxHF_MB4EtJ_B19Iw2i-q1_Lbv7h1OSA?type=png)](https://mermaid.live/edit#pako:eNptU8lu2zAQ_ZUBAaMXJbGdyFZ0KJBm34yi6aWVfKClscVWJAUuabz9e8dUGqtBBPCgWd68eTOzZoUukaWs14O1UMKlsM7ZvNZ_ioobl7PwXzlZP_AZ1nZnmPPa4nYL214vV2-h8P0iV_D6nZ1lt6rxDq5EjXa6d1yRXTjBa7FCeERsOr7r7JtX8CSkr7kTWk27eHBw8HljtTcFRqBnv7BwEUhdY-Frsti3LPJ6R6W_Tq43cPUeAjb_cjZw36EVfNcdLsFwkx09IrfeIHBVguXPCJcvEVwu6a1gH84duArf-Hyy0GgrdnTyvNPGTUC9zc4rLH6DmIckpBxnRAFzgXX5HgoqboEEVgssYW60hBUaDbMlMQLeNAYLwWcUx6X2ynWK3QbJqMhEb-Auy_MJvtCUhETrsDmath1-EP8DbWiXmNTU_Y6PQYRCK0uUnCARZKuKROUsMSTLDFEFgUoStqPMfXfgX3Rl2roP-4iH7FxLGth_8glV-oI6LkVDRvBWqEXQhVZkgQf33jlOLFylyxZwsgecZJdSOJpAzY1YhaUgvLBtQGK2S7Tr7oNxtWB3LGISjeSipNNY76BzRtUl7vY_ZyXOua_pOnK1pVDunX5aqoKlzniMmG9K7vBC8IXhkqXhXiKGpXDaPLbnFq4uYg1XLF2zF5YOh8lhPBydxsdxchwPBsk4YkuWxv3D0TA-TeL4ZDRKxsl4G7GV1oQ6OByMk-T0OOmfxHF_MB4EtJ_B19Iw2i-q1_Lbv7h1OSA)

### Notes on Workflow

#### Simulating Molecule as Source

Currently, the molecule's electric response is the only response being tracked and used to represent the molecule. You are able to specify the time dependent polarization of a point source in Meep, so once we calculate the induced dipole from Bohr, that value is converted to Meep units and fed into the custom source representing the molecule.

Here we have a sample of the CustomSource in Meep where it was given a constant polarization in the $E_z$ direction. The simulation restarts when we measure the values in the other direction. Notice the time it takes the source to reach that constant value, that's a [Meep FAQ](https://meep.readthedocs.io/en/latest/FAQ/#why-doesnt-the-continuous-wave-cw-source-produce-an-exact-single-frequency-response).
![Constant-valued CustomSource in the Ez direction](../pictures/meepDipole-out_20240926_174218.gif)

#### Capturing Absorption Spectrum from Molecule

The TDDFT code assumes that all energy absorbed by the molecule will be re-emitted by it in the form of an induced dipole, so we are not able to validate a portion of the simulation by comparing it to experimental absorption spectra. We can, however, shoot a Gaussian pulse at the molecule and measure its responses to the different molecules.

#### Three Timesteps of E field

Since we need to calculate the derivative of the molecule's wavefunction as it relates to the electric field, we deploy the RK4 method to find a good approximation. To do that we collect three timeframes of electric field. Three is the minimum requirement to perform RK4. After three frames are measured, the fourth frame is added and the first frame is removed so the three total are used again in the next timestep.

#### Time Scale Between Meep and Bohr

You are able to calculate the timestep of Meep by `dT = sim.Courant/resolution`, but this is in units of Meep time. One time unit in Meep is 3.33E-15 seconds. One time unit in Bohr is 2.4188843265857E-17 seconds
so $\Delta t_{bohr} = \Delta t_{Meep} * (333.3333333333333/2.4188843265857)$
