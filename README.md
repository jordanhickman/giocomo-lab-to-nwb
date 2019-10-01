# giocomo-lab-to-nwb
NWB conversion scripts and tutorials.
A collaboration with [Giocomo Lab](https://giocomolab.weebly.com/).

# Install
To clone the repository and set up a conda environment, do:
```
$ git clone https://github.com/ben-dichter-consulting/giocomo-lab-to-nwb.git
$ conda env create -f giocomo-lab-to-nwb/make_env.yml
$ source activate giocomo_lab_nwb
```

Alternatively, to install directly in an existing environment:
```
$ pip install giocomo-lab-to-nwb
```

# Use
After activating the correct environment, the conversion function can be used in different forms:

**1. Imported and run from a python script:** <br/>
Here's an example: we'll grab SpikeGLX data from `.imec0.ap.bin` files and convert it to a `.nwb` file.
```python
from giocomo_lab_to_nwb.conversion_tools.conversion_module import conversion_function

source_paths = {}
source_paths['spikeglx data'] = {'type': 'file', 'path': 'G4_190620_keicontrasttrack_10secBaseline1_g0_t0.imec0.ap.bin'}
f_nwb = 'output.nwb'
metafile = 'metafile.yml'

conversion_function(source_paths=source_paths,
                    f_nwb=f_nwb,
                    metafile=metafile)
```
<br/>

**2. Command line:** <br/>
Similarly, the conversion function can be called from the command line in terminal:
```
$ python conversion_module.py [imec_bin_file] [output_file] [metadata_file]
```
<br/>

**3. Graphical User Interface:** <br/>
To use the GUI, just run the auxiliary function `nwb_gui.py` from terminal:
```
$ python nwb_gui.py
```
<br/>

**4. Tutorial:** <br/>
At [tutorials](https://github.com/ben-dichter-consulting/giocomo-lab-to-nwb/tree/master/tutorials) you can also find Jupyter notebooks with the step-by-step process of conversion.
