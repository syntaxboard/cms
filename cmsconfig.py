import os
from os import listdir
import datetime

class ConfigGen():
    
    # Constructor
    def __init__(self, p_LogObj, WORKING_FOLDER_NAME):
        
        p_LogObj.error('Retriving code file list.')

        self.config_dir_path = WORKING_FOLDER_NAME.rstrip('\\') + '\\'
        self.code_dir_path = WORKING_FOLDER_NAME + '\\code\\'
    
        # Read Code Source Files
        self.list_of_files = listdir(self.code_dir_path)
        self.gen_config_file(p_LogObj, self.list_of_files)

        
    def gen_config_file(self, p_LogObj, p_file_content):

        # Check for existing file
        l_config_file_path = self.config_dir_path + 'config.txt'

        # Rename existing config file
        if os.path.exists(l_config_file_path):
            now = datetime.datetime.now()
            hour = '{:02d}'.format(now.hour)
            minute = '{:02d}'.format(now.minute)
            second = '{:02d}'.format(now.second)
            file_suffix = '{}{}{}'.format(hour, minute, second)
            
            l_backup_config = l_config_file_path.lower().replace('.txt','') + '_' + file_suffix + '.txt'
            p_LogObj.error('Backingup the existing config.txt file to ' + l_config_file_path)
            os.rename(l_config_file_path, l_backup_config)

        new_file = open(l_config_file_path, "w")
        p_LogObj.error('Attempting to create: ' + l_config_file_path)
        try:
            for i in p_file_content:
                new_file.write('0 ' + i + '\n')
            new_file.close()
        except:
            p_LogObj.error('Error creating file: ' + l_config_file_path)
        else:
            p_LogObj.error(l_config_file_path + ' ,file created')
