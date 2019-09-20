# This script grabs SpikeGLX data and stores it in .nwb files.
# authors: Luiz Tauffer and Ben Dichter
# written for Giocomo Lab
# ------------------------------------------------------------------------------
from nwbn_conversion_tools.ephys.acquisition.spikeglx.spikeglx import Spikeglx2NWB

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

    # Load metadata from YAML file
    with open(metafile) as f:
        metadata = yaml.safe_load(f)

    # Create extractor for SpikeGLX data
    npx_file = f_sources[0]
    extractor = Spikeglx2NWB(nwbfile=None, metadata=metadata, npx_file=npx_file)

    # Add acquisition data
    extractor.add_acquisition(es_name='ElectricalSeries', metadata=metadata['Ephys'])

    # Run spike sorting method
    extractor.run_spike_sorting()

    # Save content to NWB file
    extractor.save(to_path=f_nwb)

    # Check file was saved and inform on screen
    print('File saved at:')
    print(f_nwb)
    print('Size: ', os.stat(f_nwb).st_size/1e6, ' mb')


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
