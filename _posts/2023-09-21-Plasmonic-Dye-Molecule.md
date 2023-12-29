We have begun a new project. We have been inspired from many directions to begin trying to simulate the interaction between a plasmonic NP and a solution of dye molecules. 

**UPDATE (Dec 29th, 2023): As of now, we are not using DDA and instead using FDTD as our classical method.**

Motivations:
* Many of our applications in NP end with optical detection and SERS enhancement with Raman-active dye molecules.
* I am extremely interested in electronic structure theory and the representation of a dye molecule is best from an *ab initio* point.
* Our friends at Freed-Hardeman Dr. Barr and Dr. Chaffin would like to simulate a layer of dye molecules on the surface of a NP in DDSCAT.

## Step 1: How would we implement a dye molecule in DDSCAT?
When inputting a material into DDSCAT, all we are asked for is the dielectric response function of the material. This is easily found for metals and other bulk elements, as it is well known in the experimental field. 

I suppose a dielectric response function could be found out of a bulk dye solution, but these moleucles are usually aqueous which would not accurately model the dye itself. Additionally, we may want to simulate one dye molecule on its own, and at the size of a dye moleucle, classical dielectrics would not hold. We need the *ab initio* dielectric response.

Dr. Nascimento at the University of Memphis, who taught me electronic structure, knows theory and has a script that can take a molecule and calculate its polarizability $\alpha$. The DDSCAT program actually takes the dielectric fuction $\epsilon$ and transforms it into a polarizability internally. Because we cannot explicitly give DDSCAT $\alpha$ data of our dye, we convert it to $\epsilon$. Below is the derivation I made to easily convert between the two:

![Polarizability to Dielectric Proof](/pictures/polarizationproof.png)

Now, we can use this proof to translate between Dr. Nascimento's polarizability code output and the DDSCAT dielectric input. 

*As of now (10/03/2023), there is an issue with the polarizability to dielectric code. I suspect that because of the sheer magnitude of the d$^3$ factor, the original equation breaks down in applicability. Removing the constant $\frac{4\pi}{3d^3}$ would fix the magnitude issue, but the relationship between polarizability and dielectric is not linear, so removing this constant affects not only the intensity of the result, but the shape as well.* 

## Step 2: Shape File Generation
Now, we must develop a plan as to how to simulate these two materials together. First, it is best if we ensure that our *ab initio* dye simulation is accurate. We should be able to simulate a solution of aqueous dye molecules in DDSCAT and measure their absorbance.

### Dye Only Simulation
I created a f90 script that takes a specified number of dye molecules, dipole distance, and cube width. It randomly populates the cube with the number of dye molecules. 

In initial trial with a dipole distance of 0.2nm, dye numbers at or below $10^7$ do not give a response. 

Here is a list of trails performed initially:

Single DM:
```
100=L/dd,   0.20=dd    0.12407E-03=aeff     0.20754E-03=conc 
1 = NAT
```

100 DM:
```
100=L/dd,   0.20=dd    0.57588E-03=aeff     0.20754E-01=conc 
100 = NAT
```

1,000 DM:
```
100=L/dd,   0.20=dd    0.12407E-02=aeff     0.20754E+00=conc 
1000 = NAT
```

10,000 DM:
```
100=L/dd,   0.20=dd    0.26730E-02=aeff     0.20754E+01=conc 
10000 = NAT
```

100,000 DM:
```
100=L/dd,   0.20=dd    0.57588E-02=aeff     0.20754E+02=conc 
100000 = NAT
```

1,000,000 DM:
```
100=L/dd,   0.20=dd    0.12407E-01=aeff     0.20754E+03=conc 
1000000 = NAT
```

