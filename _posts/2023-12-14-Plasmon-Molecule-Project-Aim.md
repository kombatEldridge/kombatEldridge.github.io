To keep a constant idea of the goals of my project, I will keep this page updated with my tasks and their progress.

### RT-TDDFT: Real Time Time Dependent Density Functional Theory
For the first month of development, Dr. Nascimento and I sat down to write a TDDFT script that runs real time calculations. One would think that the TD ("Time Dependent") part of TDDFT would cover it, but that's not the case. Typically, when research mentions TDDFT, they are really refering to Linear Response TDDFT (and in typical physical chemist fashion, we will elongate the initialism to LR-TDDFT for the sake of convolution and brevity). 

In both LR-TDDFT and RT-TDDFT, the matter in question is illuminated with light and its response is determined. However, in weak light-matter interactions (responses that are less intense than the matter's own intermolecular forces), one can assume a linear response through time and use LR-TDDFT (which actually operates in the frequency domain). Joshua Goings has a [nice blog post](https://joshuagoings.com/2013/04/27/linear-response-td-dft-the-density-density-response-function/) about the math behind LR-TDDFT. However, in stronger interactions, the linear response isn't sufficient and we need to actually calculate the response through time. So, we use RT-TDDFT which doesn't assume a linear response and can simulate those stronger interactions. 

Creating code to run RT-TDDFT has been done in the past and to someone relatively experienced in the field, a month might seem insanely too long to spend on this phase. First of all, thank you for reading my blog post. Share it with some of your friends. Secondly, I'm only a novice. My training has been in classical EM mechanics, so this has been a learning process every step of the way (fostering baby steps in complicated matters is something Dr. Nascimento is blessed at).

Dr. Nascimento has been developing an in-house software for many physical chemistry needs, and so our RT-TDDFT code was written specifically for that framework. We're able to simulate the induced dipole of a molecule by any shape of an incident electric field. The code has been written in python, and as it is just a prototype until we can use it with our classical EM code, it hasn't been optimized for computational time either. Still, calculating pyridine is trivial.

### FDTD: Finite Difference Time Domain
With all these acronyms, this one is the one I get tripped up on this most. Must be something about the repitition.

Now we switch gears from the *ab initio* quantum mechanics with Dr. Nascimento to the classical electromagnetic mechanics with Dr. Wang. Originally, we planned on implimenting our skills and history in DDSCAT with this project, but turning DDSCAT from the frequency domain to the time domain seemed to be a daunting task. Many people in our field (and some outside our field who don't want to go through the trouble of consulting us) use FDTD to simulate light-nanoparticle interactions. You will find many more proprietary softwares offering this method of apporach as apposed to DDA softwares. FDTD aims to solve the Maxwell equations in the time domain too, so we decided to investigate it.

Luckily, there is a group at MIT that has built an open-source python library for FDTD called [MEEP](https://meep.readthedocs.io/en/latest/). There's a bit of a learning curve to their methods, but their documentation is detailed enough to get me acquainted fairly easily.

**As of Dec. 14, 2023, this is where we are. We can simulate a NP and watch its response propogate in real time (see attached GIF). We would like to figure out two main issues with MEEP before we lock in on it: 1) we don't understand how to calculate the important far field effects (extinction and scattering) and 2) we don't know how to run nanometer sized systems. MEEP operates in the micron regime and trying to run a nano-sized job requires 100-fold the amount of computational resources.**

<p align="center" width="100%">
    <img width="150%" src="https://github.com/kombatEldridge/kombatEldridge.github.io/blob/cae5c858ce64e29a586854a4ec5914ee638d0753/pictures/MeepAuSphere-out.gif?raw=true">
</p>
