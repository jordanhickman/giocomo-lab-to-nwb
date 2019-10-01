# Opens the NWB conversion GUI
# authors: Luiz Tauffer and Ben Dichter
# written for Giocomo Lab
# ------------------------------------------------------------------------------
from nwbn_conversion_tools.gui.nwbn_conversion_gui import nwbn_conversion_gui

metafile = 'metafile.yml'
conversion_module = 'conversion_module.py'

source_paths = {}
source_paths['spikeglx data'] = {'type': 'file', 'path': ''}

nwbn_conversion_gui(metafile=metafile, conversion_module=conversion_module,
                    source_paths=source_paths)
