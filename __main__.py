from cmslogger import CMSLog
from cmsops import CMSOps
import cmsargs as tiar
import logging 

if __name__ == '__main__':

    # Singleton Objects
    parser = tiar.ArgParser()
    LObj = CMSLog(parser.working_folder)
    LogObj = LObj.getlog()
    
    # Main Processing
    OpsObj = CMSOps(LogObj, parser.action, parser.working_folder)
    logging.shutdown()
