# Changes to the Mie Multilayer code

*Code inspired by "Improved recursive algorithm for light scattering by a multilayered sphere" from Applied Optics Yang 2003*

[Current webpage app](http://ywangcomp.org/multilayer.html)

[Current repository](https://github.com/kombatEldridge/mieMultilayer/blob/194876399626b4e6be7a885a2d7a52cd65974582/mieMultilayer.py)

[Current README.md](https://kombateldridge.github.io/2022/07/22/Mie-Multilayer-Jupyter-Notebook.html)

---

## Change Log:

### July 22, 2022

* All settings like layer size and dielectric information are stored in a JSON file called mieSettings.txt


```
{
    "numLayers": "3",
    "dielectricData": [
        "dielectricFiles/Au_diel.txt",
        "dielectricFiles/Si_diel.txt",
        "dielectricFiles/Ag_diel.txt"
    ],
    "radii": [
        "10",
        "20",
        "30"
    ],
    "dielectricColumns": [
        "1",
        "2",
        "1",
        "2",
        "1",
        "2"
    ],
    "wavelengthInterval": 
        {
            "startWavelength": "300",
            "stopWavelength": "800",
            "intervalWavelength": "1"
        },
    "outputFileName": "mieResults.txt"
}
```

* Each layer of the sphere now uses a separate dielecric file, but dielectric information can come from on file if user simply inputs the same file path multiple times.
* User now forced to use linear interpolation feature.

### August 12, 2022

* Automatic interpolation optimized to use *polynomial interpolation* for dielectric information (a four-point interpolation inspired by [this resource](https://www.appstate.edu/~grayro/comphys/lecture4_11.pdf)).
* Comments added to code and variable names updated to reflect their function.
* Small optimization changes.

### September 19, 2022

* ***Attempted to*** make the addtion of the [scattnlay](https://github.com/ovidiopr/scattnlay) package to the web application.
* We intend to utilize the work done by K. Ladutenko, U. Pal, A. Rivera and O. Peña-Rodríguez to offer additional tools through our web app.

### September 20, 2022
* The [scattnlay](https://github.com/ovidiopr/scattnlay) package offers a python wrapper (PyBind11) that allows the system to call on C++ files using python. Since our webpage uses python, I would like to use this wrapper. However, PyBind11 requires a g++ version 4.8 (a C++ interpreter) or higher, and our webpage server sadly runs g++ version 4.4 and cannot be updated.

### October 24, 2023
* Small changes made throughout the year but never logged:
    * Info buttons added to each input parameter.
    * App now accepts one or multiple material files.
    * Slide button added to deliberate between one master material file and multiple material files.

---

### Future Work/Works in Progress
    
* The calculations behind $Q_{nf}$ are not correct (I think). Will need to dive further into the math.
* To solidify the validity of the code, I plan on providing a proof for the equations used.
* I need to change every reference of "dielectric" to "refractive index". The code calculates using index and not dielectric. This is a very important distinction. 
