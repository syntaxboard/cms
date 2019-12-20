import os
from os import listdir
import datetime

class ConfigMgr():
    
    # Constructor
    def __init__(self, lob, WORKING_FOLDER_NAME):
        
        self.log = lob
        self.log.error('This is an error message')
        
        self.config_dir_path = WORKING_FOLDER_NAME.rstrip('\\') + '\\'
        self.code_dir_path = WORKING_FOLDER_NAME + '\\code\\'
    
        # Read Code Source Files
        self.list_of_files = listdir(self.code_dir_path)
        self.gen_config_file(self.list_of_files)
    
    def gen_config_file(self, p_file_content):
        
        # Check for existing file
        l_config_file_path = self.config_dir_path + 'config.txt'
        
        if os.path.exists(l_config_file_path):
            now = datetime.datetime.now()
            hour = '{:02d}'.format(now.hour)
            minute = '{:02d}'.format(now.minute)
            second = '{:02d}'.format(now.second)
            file_suffix = '{}{}{}'.format(hour, minute, second)

            os.rename(l_config_file_path, l_config_file_path.lower().replace('.txt','') + '_' + file_suffix + '.txt')

            
        new_file = open(l_config_file_path, "w")
        
        for i in p_file_content:
            new_file.write('0 ' + i + '\n')
        new_file.close()
        
        