#!/usr/bin/env python3.4
import ursgal
import importlib
import os
import sys
import pickle

class xtandem2csv_1_0_0( ursgal.UNode ):
    """xtandem2csv_1_0_0 UNode"""
    META_INFO = {
        'edit_version'      : 1.00,                                             # flot, inclease number if something is changed (kaz)
        'name'              : 'xtandem2csv',                                    # str, Software name (kaz)
        'version'           : '1.0.0',                                          # str, Software version name (kaz)
        'release_date'      : None,                                             # None, '%Y-%m-%d' or '%Y-%m-%d %H:%M:%S' (kaz)
        'engine_type' : {
            'converter' : True
        },
        'input_extensions'  : ['.xml', '.xml.gz'],                              # list, extensions (kaz)
        'input_multi_file'  : False,                                            # bool, fill true up if multiple files input is MUST like venn-diagram (kaz)
        'output_extensions' : ['.csv'],                                         # list, extensions (kaz)
        'output_suffix'     : None,
        'in_development'    : False,
        'include_in_git'    : True,
        'engine' : {
            'platform_independent' : {
                'arc_independent' : {
                    'exe' : 'xtandem2csv_1_0_0.py',
                },
            },
        },

    }

    def __init__(self, *args, **kwargs):
        super(xtandem2csv_1_0_0, self).__init__(*args, **kwargs)

    def _execute( self ):
        '''
        XML result files from X!Tandem are converted to CSV

        Input file has to be a .xml

        Creates a .csv file and returns its path

        '''
        print('[ -ENGINE- ] Executing conversion ..')
        self.time_point(tag = 'execution')
        xtandem2csv_main = self.import_engine_as_python_function()
        # if self.params['output_file'].lower().endswith('.xml') is False:
        #     raise ValueError('Trying to convert a non-xml file')

        output_file = os.path.join(
                self.params['output_dir_path'],
                self.params['output_file']
            )
        input_file  = os.path.join(
                self.params['input_dir_path'],
                self.params['input_file']
            )

        xtandem2csv_main(
            input_file     = input_file,
            output_file    = output_file,
            decoy_tag      = self.params['translations']['decoy_tag'],
        )

        self.print_execution_time(tag='execution')
        return output_file
