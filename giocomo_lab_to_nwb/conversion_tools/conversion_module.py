# This script grabs SpikeGLX data and stores it in .nwb files.
# authors: Luiz Tauffer and Ben Dichter
# written for Giocomo Lab
# ------------------------------------------------------------------------------
from nwbn_conversion_tools.ephys.acquisition.spikeglx.spikeglx import Spikeglx2NWB
from ndx_labmetadata_giocomo import LabMetaData_ext
import pynwb

import yaml
import copy
import os


def conversion_function(source_paths, f_nwb, metadata, **kwargs):
    """
    Copy data stored in a set of .npz files to a single NWB file.

    Parameters
    ----------
    source_paths : dict
        Dictionary with paths to source files/directories. e.g.:
        {'spikeglx data': {'type': 'file', 'path': ''}}
    f_nwb : str
        Path to output NWB file, e.g. 'my_file.nwb'.
    metadata : dict
        Dictionary containing metadata
    **kwargs : key, value pairs
        Extra keyword arguments.
    """

    # Source files
    npx_file = None
    for k, v in source_paths.items():
        if source_paths[k]['path'] != '':
            if k == 'spikeglx data':
                npx_file = source_paths[k]['path']

    # Remove lab_meta_data from metadata, it will be added later
    # Spikeglx2NWB cannot manipulate custom nwb extensions
    metadata0 = copy.deepcopy(metadata)
    metadata0['NWBFile'].pop('lab_meta_data', None)

    # Create extractor for SpikeGLX data
    extractor = Spikeglx2NWB(nwbfile=None, metadata=metadata0, npx_file=npx_file)

    # Add acquisition data
    extractor.add_acquisition(es_name='ElectricalSeries', metadata=metadata['Ecephys'])

    # Run spike sorting method
    extractor.run_spike_sorting()

    # Save content to NWB file
    extractor.save(to_path=f_nwb)

    # Add other fields
    with pynwb.NWBHDF5IO(f_nwb, 'a') as io:
        nwb = io.read()

        # Add lab_meta_data
        lab_metadata = LabMetaData_ext(
            name=metadata['NWBFile']['lab_meta_data']['name'],
            acquisition_sampling_rate=metadata['NWBFile']['lab_meta_data']['acquisition_sampling_rate'],
            number_of_electrodes=metadata['NWBFile']['lab_meta_data']['number_of_electrodes'],
            file_path=metadata['NWBFile']['lab_meta_data']['file_path'],
            bytes_to_skip=metadata['NWBFile']['lab_meta_data']['bytes_to_skip'],
            raw_data_dtype=metadata['NWBFile']['lab_meta_data']['raw_data_dtype'],
            high_pass_filtered=metadata['NWBFile']['lab_meta_data']['high_pass_filtered'],
            movie_start_time=metadata['NWBFile']['lab_meta_data']['movie_start_time'],
        )
        nwb.add_lab_meta_data(lab_metadata)

        # add information about the subject of the experiment
        experiment_subject = Subject(subject_id=metadata['NWBFile']['subject']['subject_id'],
                                     species=metadata['NWBFile']['subject']['species'],
                                     description=metadata['NWBFile']['subject']['description'],
                                     genotype=metadata['NWBFile']['subject']['genotype'],
                                     date_of_birth=metadata['NWBFile']['subject']['date_of_birth'],
                                     weight=metadata['NWBFile']['subject']['weight'],
                                     sex=metadata['NWBFile']['subject']['sex'])
        nwb.subject = experiment_subject

        io.write(nwb)

    # Check file was saved and inform on screen
    print('File saved at:')
    print(f_nwb)
    print('Size: ', os.stat(f_nwb).st_size/1e6, ' mb')


# If called directly fom terminal
if __name__ == '__main__':
    import sys
    import yaml

    if len(sys.argv) < 4:
        print('Error: Please provide source files, nwb file name and metafile.')

    source_paths = {}
    source_paths['spikeglx data'] = {'type': 'file', 'path': sys.argv[1]}
    f_nwb = sys.argv[2]

    # Load metadata from YAML file
    metafile = sys.argv[3]
    with open(metafile) as f:
       metadata = yaml.safe_load(f)

    conversion_function(source_paths=source_paths,
                        f_nwb=f_nwb,
                        metadata=metadata)
