# Au - SiO<sub>2</sub> - Au GIF Creation Notes

<p align="center" width="100%">
    <img width="50%" src="https://github.com/kombatEldridge/kombatEldridge.github.io/blob/main/pictures/AuSiO2AuDiagram.png?raw=true">
</p>

---

# Step 1: `Esq_1.vtr` Visualization

## Mayavi Phase
In order to visualize the nearfield data from the DDSCAT output, I used tyhe Mayavi software. From their github [README.md](https://github.com/enthought/mayavi): 
```
Mayavi seeks to provide easy and interactive visualization of 3D data.
```

It provides a user interface that allows for interaction with the data visualization details. However, it can also be easily implimented into a python script that runs the UI with some saved settings. This following terminal command opens the mayavi client with the python script (where the `-x` switch lets mayavi know you are passing a python script). If you do not want to have the mayavi client open and instead have the processing happen off screen, we add the `-o` switch.

```python
$ mayavi2 -x test.py -o
```

If you have multiple datasets needing to be processed in the same manner, this method allows the application of the same settings to every dataset.

## Python Script
First, you need to import the off screen version of the mayavi api. Use the commented version if you want the on screen version.
```python
from mayavi.api import OffScreenEngine
# from mayavi.api import Engine
```

Next, we import the vtk/vtr reader. If your vtk/vtr file is an older binary version, use the commented line.
```python
from mayavi.sources.api import VTKXMLFileReader
# from mayavi.sources.api import VTKFileReader
```

This last import gives access to the graphing module. Our files contain 3D information, but for our research purposes, we only want a 2D contour plane.
```python
from mayavi.modules.contour_grid_plane import ContourGridPlane
```

Now create the MayaVi engine and start it.
```python
engine = OffScreenEngine()
engine.start()
scene = engine.new_scene()
```

We read in the vtk/vtr file and add the file source.
```python
reader = VTKXMLFileReader()
reader.initialize("Esq_1.vtr")
engine.add_source(reader)
```

In order to create the contour grid module, we initialize it with its main command, and then add it to the engine (not the scene).
```python
ContourGridPlane = ContourGridPlane()
engine.add_module(ContourGridPlane)
```

Now comes the settings I applied. Our data object (ContourGridPlane with the initialized `Esq_1.vtr`) has a width of 360 frames (derived from the size of the DDSCAT grid I imagine), so we place the frame in the middle (180).
```python
ContourGridPlane.grid_plane.position = 180
```

However, the frame needs the contour removed so we can see the nanoparticle and not the whole scene.
```python
ContourGridPlane.enable_contours = False
```

We then create a manager to apply some scene changes.
```python
module_manager = engine.scenes[0].children[0].children[0]
```

This sets the colormap look up table (lut) to binary. Other color options are [availible](https://docs.enthought.com/mayavi/mayavi/mlab_changing_object_looks.html).
```python
module_manager.scalar_lut_manager.lut_mode = 'binary'
```

We then set the color range to only represent values from 0 to 500. The default color range is insufficient.
```python
module_manager.scalar_lut_manager.use_default_range = False
module_manager.scalar_lut_manager.scalar_bar.position = [0.1 , 0.01]
module_manager.scalar_lut_manager.scalar_bar.position2 = [0.8 , 0.17]
module_manager.scalar_lut_manager.data_range = [  0., 500.]
```

We place the camera orthogonal to the the -x plane.
```python
scene.scene.x_minus_view()
```


Finally, we save the image created.
```python
scene.scene.save_png("binary.png")
```

So, in all, the python script looks like this.

<details>
  <summary>mayavi_image_creator.py</summary>

    ```python
    from mayavi.api import OffScreenEngine
    from mayavi.sources.api import VTKXMLFileReader
    from mayavi.modules.contour_grid_plane import ContourGridPlane

    # Create the MayaVi engine and start it.
    engine = OffScreenEngine()
    engine.start()
    scene = engine.new_scene()

    # Read in VTK file and add as source
    reader = VTKXMLFileReader()
    reader.initialize("Esq_1.vtr")
    engine.add_source(reader)

    # Add Surface Module
    ContourGridPlane = ContourGridPlane()
    engine.add_module(ContourGridPlane)
    ContourGridPlane.enable_contours = False
    ContourGridPlane.grid_plane.position = 180
    module_manager = engine.scenes[0].children[0].children[0]
    module_manager.scalar_lut_manager.lut_mode = 'binary'
    module_manager.scalar_lut_manager.use_default_range = False
    module_manager.scalar_lut_manager.scalar_bar.position = [0.1 , 0.01]
    module_manager.scalar_lut_manager.scalar_bar.position2 = [0.8 , 0.17]
    module_manager.scalar_lut_manager.data_range = [  0., 500.]

    # Move the camera
    scene.scene.x_minus_view()

    # Save scene to image file
    scene.scene.save_png("binary.png")
    ```
</details>

# HPC Phase
## File Structure 
The `Esq_1.vtr` files sit in their respective directory named `lamxxx`. In my jobs, we have `lam300` to `lam1000`.

All of the `lamxxx` folders sit in the main job directory, where I placed the python script and the following shell script.

## Shell Script

Basically, this shell script opens each `lamxxx` folder, copies the python script, and runs the mayavi command. For the HPC, the `module load openswr` loads the necessary modules for mayavi.
```sh
#!/bin/bash

for i in {300..1000..10}
do
    dir_name="lam"$i
    echo $dir_name
    cd $dir_name
    cp ../mayavi_image_creator.py .
    module load openswr
    mayavi2 -x mayavi_image_creator.py -o
    cd ../
done
```

## Post Processing Python Script

This python script opens each `lamxxx` folder, takes the two images (I made one with the colormap Binary and another in the colormap Copper), places them in the parent director in a folder named `esqPictures`, and renames them by the folder they came from.
```python
import os

pwd = os.getcwd()
for root, dirs, files in os.walk(pwd, topdown=False):
    folders = dirs

if "esqPictures" not in folders:
    print("here!")
    os.mkdir(os.path.join(root, "esqPictures"))
for folder in folders:
    for root2, dirs, files in os.walk(os.path.join(pwd, folder), topdown=False):
        if "binary.png" in files:
            os.rename("".join([os.path.join(root, folder), "/binary.png"]), "".join([pwd, "/esqPictures/", folder,"binary.png"]))
        if "copper.png" in files:
            os.rename("".join([os.path.join(root, folder), "/copper.png"]), "".join([pwd, "/esqPictures/", folder,"copper.png"]))
```

Finally, once all the images are loaded into one folder, I have the script add some details to the images like the wavelength and the scale (you can also add a scale to the mayavi python script, but it messes up some formatting), and then it creates a gif of all the images. Some positioning of the labels and images will need to be changed depending on resolution of the mayavi output images and the scale images.

The font file `cmunrm.ttf` of the text in the image needs to be included in the same folder the python script reads in. Other files include the scale images.
```python
import imageio.v2 as imageio
from PIL import Image, ImageFont, ImageDraw 

filenameCopper = []
filenameBinary = []

# Makes separate lists of all copper pictures and all binary pictures
for root, dirs, files in os.walk("".join([pwd, "/esqPictures"]), topdown=False):
    for filename in files:
        if "copper" in filename:
            filenameCopper.append(filename)
        if "binary" in filename:
            filenameBinary.append(filename)

    # adds text to image, adds scale and legend to image, and creates gif
    images = []
    for file1 in sorted(filenameCopper):
        my_image = Image.open("".join([folder,"/",file1]))
        im2 = Image.open("scaleCopper.png")
        posx, posy = [330, 63]
        sizex, sizey = im2.size
        sizex, sizey = sizex/5, sizey/5
        title_font = ImageFont.truetype('cmunrm.ttf', size=20)
        title_text = file1[0:6]
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((15,15), title_text, (255, 255, 255), font=title_font)
        title_font = ImageFont.truetype('cmunrm.ttf', size=10)
        image_editable.text((posx + 5*sizex+5, posy + 5*sizey-5), "0", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 4*sizey-5), "100", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 3*sizey-5), "200", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 2*sizey-5), "300", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 1*sizey-5), "400", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 0*sizey-5), "500", (255, 255, 255), font=title_font)
        my_image.save("".join([folder,"/",file1]))

        im1 = Image.open("".join([folder,"/",file1]))

        back_im = im1.copy()
        back_im.paste(im2, (posx, posy))
        back_im.save("".join([folder,"/",file1]))

        images.append(imageio.imread("".join([folder,"/",file1])))
    imageio.mimsave("".join([pwd,"/", folder,'_copper.gif']), images, duration=0.05)

    images = []
    for file2 in sorted(filenameBinary):
        my_image = Image.open("".join([folder,"/",file2]))
        im2 = Image.open("scaleBinary.png")
        posx, posy = [330, 63]
        sizex, sizey = im2.size
        sizex, sizey = sizex/5, sizey/5
        title_font = ImageFont.truetype('cmunrm.ttf', size=20)
        title_text = file2[0:6]
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((15,15), title_text, (255, 255, 255), font=title_font)
        title_font = ImageFont.truetype('cmunrm.ttf', size=10)
        image_editable.text((posx + 5*sizex+5, posy + 5*sizey-5), "0", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 4*sizey-5), "100", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 3*sizey-5), "200", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 2*sizey-5), "300", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 1*sizey-5), "400", (255, 255, 255), font=title_font)
        image_editable.text((posx + 5*sizex+5, posy + 0*sizey-5), "500", (255, 255, 255), font=title_font)
        my_image.save("".join([folder,"/",file2]))

        im1 = Image.open("".join([folder,"/",file2]))
        im2 = Image.open("scaleBinary.png")

        back_im = im1.copy()
        back_im.paste(im2, (posx, posy))
        back_im.save("".join([folder,"/",file2]))
        images.append(imageio.imread("".join([folder,"/",file2])))
    imageio.mimsave("".join([pwd,"/", folder,'_binary.gif']), images, duration=0.05)
```

After that, here is an example of my results!

![gif](/pictures/10nm_Gap_copper.gif)



<script type="text/javascript" src="./libgif.js"></script>

<img src="/pictures/10nm_Gap_copper.gif" width="400" height="350" rel:auto_play="0" />

<script type="text/javascript">
    $$('img').each(function (img_tag) {
        if (/.*\.gif/.test(img_tag.src)) {
            var rub = new RubbableGif({ gif: img_tag } );
            rub.load();
        }
    });
</script>

<img id="example1" src="/pictures/10nm_Gap_copper.gif" rel:auto_play="0" width="400" height="350" />
<br>
<a href="javascript:;" onmousedown="sup1.pause(); return false;">Pause</a> |
<a href="javascript:;" onmousedown="sup1.play(); return false;">Play</a> |
<a href="javascript:;" onmousedown="sup1.move_to(0); return false;">Restart</a> |
<a href="javascript:;" onmousedown="sup1.move_relative(1); return false;">Step forward</a> |
<a href="javascript:;" onmousedown="sup1.move_relative(-1); return false;">Step back</a>

Example with rubbing and auto-play on
<img id="example2" src="https://rawgit.com/buzzfeed/libgif-js/master/example_gifs/rub_test.gif" rel:auto_play="1" width="467" height="375" rel:rubbable="1" />
