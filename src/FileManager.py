import os
import pandas as pd
import sys

class FileManager:

    def __init__(self, source, destination=None):
        
        self.source = source
        self.destination = destination
        self.arrf_text = None

    def rename_to_txt(self):

        """ Renames the ARFF file, converting it to a txt file in the process. """



        os.rename(self.source,  )

    def check_valid_location(self):
        pass

    def check_file_exists(self):
        pass

    def convert_CSV(self):
        pass


