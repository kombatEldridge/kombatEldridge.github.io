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

### September 20, 2022
* The [scattnlay](https://github.com/ovidiopr/scattnlay) package offers a python wrapper (PyBind11) that allows the system to call on C++ files using python. Since our webpage uses python, I would like to use this wrapper. However, PyBind11 requires a g++ version 4.8 (a C++ interpreter) or higher, and our webpage server runs g++ version 4.4 and cannot be updated unless through a convoluted linux update process. Therefore, I want to use Boost.Python, which is similar to PyBind11 but more heavy duty.
* I plan to convert the PyBind11 files in the repo to use Boost.Python instead. Hopefully, then we can run the [scattnlay](https://github.com/ovidiopr/scattnlay) package on the webpage.

### September 21, 2022
* I converted all the PyBind11 references and files to Boost.Python, but the package is still throwing errors when installing on the website.

```
((mieMultilayer:3.7)) eoks0lmrxaaf@a2plcpnl0711 [~/mieMultilayer/scattnlay]$ pip install .
Processing /home/eoks0lmrxaaf/mieMultilayer/scattnlay
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: numpy in /home/eoks0lmrxaaf/virtualenv/mieMultilayer/3.7/lib64/python3.7/site-packages (from python-scattnlay-Boost==2.3) (1.21.6)
Building wheels for collected packages: python-scattnlay-Boost
  Building wheel for python-scattnlay-Boost (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for python-scattnlay-Boost (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [18 lines of output]
      running bdist_wheel
      running build
      running build_py
      running build_ext
      building 'scattnlay_dp' extension
      /usr/bin/gcc -pthread -Wno-unused-result -Wsign-compare -DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/home/eoks0lmrxaaf/virtualenv/mieMultilayer/3.7/include -I/opt/alt/python37/include/python3.7m -c src/boost-wrapper.cc -o build/temp.linux-x86_64-cpython-37/src/boost-wrapper.o -std=C++0x
      cc1plus: error: unrecognized command line option "-std=C++0x"
      cc1plus: warning: unrecognized command line option "-Wno-unused-result"
      Failed to build all extensions... Building only in double precision...
      running bdist_wheel
      running build
      running build_py
      running build_ext
      building 'scattnlay_dp' extension
      /usr/bin/gcc -pthread -Wno-unused-result -Wsign-compare -DDYNAMIC_ANNOTATIONS_ENABLED=1 -DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -m64 -mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/home/eoks0lmrxaaf/virtualenv/mieMultilayer/3.7/include -I/opt/alt/python37/include/python3.7m -c src/boost-wrapper.cc -o build/temp.linux-x86_64-cpython-37/src/boost-wrapper.o -std=C++0x
      cc1plus: error: unrecognized command line option "-std=C++0x"
      cc1plus: warning: unrecognized command line option "-Wno-unused-result"
      error: command '/usr/bin/gcc' failed with exit code 1
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for python-scattnlay-Boost
Failed to build python-scattnlay-Boost
ERROR: Could not build wheels for python-scattnlay-Boost, which is required to install pyproject.toml-based projects
```
* Maybe the website is case sensitive on `"-std=C++0x"`


![twenty-first night](/pictures/twentyfirst.gif)

---

### Future Work/Works in Progress
    
* There is an issue right now where the near-field enhancement for a pure Silica sphere is returning a value close to $0.014$ where $Q_{nf}=1$ would be expected.
* We are curious to see if we can provide the $Q_{ext}$, $Q_{sca}$, and $Q_{abs}$ for each layer.
* To solidify the validity of the code, I plan on providing a proof for the equations used.
* The webpage version of the code needs to accept more than one dielectric file.
* Webpage version also needs info snippets for each input to help the user.