# This script grabs electrophysiology data and stores it in .nwb files.
# authors: Luiz Tauffer and Ben Dichter
# written for Giocomo Lab
# ------------------------------------------------------------------------------
from pynwb import NWBFile, NWBHDF5IO, ProcessingModule
from pynwb.device import Device
from pynwb.base import TimeSeries

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import yaml
import numpy as np
import os


def conversion_function(*f_sources, f_nwb, metafile, **kwargs):
    """
    Copy data stored in a set of .npz files to a single NWB file.

    Parameters
    ----------
    *f_sources : str
        Possibly multiple paths to source files.
    f_nwb : str
        Path to output NWB file, e.g. 'my_file.nwb'.
    metafile : str
        Path to .yml meta data file
    **kwargs : key, value pairs
        Extra keyword arguments.
    """
    pass




#If called directly fom terminal
if __name__ == '__main__':
    import sys

    if len(sys.argv)<4:
        print('Error: Please provide source files, nwb file name and metafile.')

    f1 = sys.argv[1]
    f_nwb = sys.argv[2]
    metafile = sys.argv[3]
    conversion_function(f1,
                        f_nwb=f_nwb,
                        metafile=metafile)
