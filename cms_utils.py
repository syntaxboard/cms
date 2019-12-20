import datetime
import logging 

class CMSLog():
    
    def __init__(self,working_folder):
        # Create a File Handler
        now = datetime.datetime.now()
        hour = '{:02d}'.format(now.hour)
        minute = '{:02d}'.format(now.minute)
        second = '{:02d}'.format(now.second)
        file_suffix = '{}{}{}'.format(hour, minute, second)

        log_file_name = 'run_log_'+ file_suffix+ '.log'
        self.tinitiateLOG = logging.getLogger('tinitiate')
        self.LogFile = logging.FileHandler(working_folder + log_file_name)
        self.LogFile.setLevel(logging.ERROR)
        self.tinitiateLOG.addHandler(self.LogFile)
        
    def  get_logger(self):
        return self.tinitiateLOG