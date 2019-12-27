import datetime
import logging 

class CMSLog():
    
    ############################################################################
    def __init__(self,working_folder):

        # Create a File Handler
        now = datetime.datetime.now()
        file_suffix = '{}{}{}'.format( '{:02d}'.format(now.hour)
                                      ,'{:02d}'.format(now.minute)
                                      ,'{:02d}'.format(now.second))

        log_file_name = 'ticms_'+ file_suffix+ '.log'
        self.tinitiateLOG = logging.getLogger('tinitiate')
        LogFile = logging.FileHandler(working_folder + log_file_name)

        # formatter = logging.Formatter('[%(asctime)s]: %(message)s')
        formatter = logging.Formatter('[%(asctime)s][%(module)s - %(funcName)s]: %(message)s')

        LogFile.setFormatter(formatter)
        LogFile.setLevel(logging.ERROR)

        self.tinitiateLOG.addHandler(LogFile)
        # self.tinitiateLOG.debug("test")
    ############################################################################

    def getlog(self):
        return self.tinitiateLOG
