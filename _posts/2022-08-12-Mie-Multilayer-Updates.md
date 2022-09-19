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

* ***Attempting to*** make the addtion of the [scattnlay](https://github.com/ovidiopr/scattnlay) package to the web application.
* We intend to utilize the work done by K. Ladutenko, U. Pal, A. Rivera and O. Peña-Rodríguez to offer additional tools through our web app.

---

### Future Work/Works in Progress
    
* There is an issue right now where the near-field enhancement for a pure Silica sphere is returning a value close to $0.014$ where $Q_{nf}=1$ would be expected.
* We are curious to see if we can provide the $Q_{ext}$, $Q_{sca}$, and $Q_{abs}$ for each layer.
* To solidify the validity of the code, I plan on providing a proof for the equations used.
* The webpage version of the code needs to accept more than one dielectric file.
* Webpage version also needs info snippets for each input to help the user.