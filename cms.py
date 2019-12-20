###############################################################################
#
#   CONTENT MANAGER SYSTEM
#   1. Generate Config
#      Usage: cms.py C:\\Tinitiate\\work\\python GC
#  
#   2. Generate MD, SPLIT-CODE, DOCX
#      Usage:
#
###############################################################################
from config_engine import ConfigMgr
# from code_splitter_engine import cs_engine
from cms_utils import CMSLog
from cms_md import cms_md
import sys
import logging


cms_args = sys.argv

WORKING_FOLDER_NAME = cms_args[1] # Check if \\ is appeneded
OPERATION = cms_args[2]

try:
    LANGUAGE = cms_args[3]
except:
    pass

try:
    DONT_RETAIN_YAML = cms_args[4]
except:
    pass



if WORKING_FOLDER_NAME == '':
    print("Please Specify Working Folder Name in Windows Path Escape Format!!")

elif  WORKING_FOLDER_NAME != '':
    lob = CMSLog(WORKING_FOLDER_NAME)
    x = lob.get_logger()

    if OPERATION.upper().strip() == 'GC':
        gcObj = ConfigMgr(x,WORKING_FOLDER_NAME)
    
    if OPERATION != "GC":
        # p_log_obj, p_code_file_folder, p_md_file_folder, p_language, p_dont_retain_yaml, p_code_file)
        md_gen = cms_md( x
                        ,WORKING_FOLDER_NAME + "\\code\\"
                        ,WORKING_FOLDER_NAME + '\\md\\'
                        ,LANGUAGE
                        ,DONT_RETAIN_YAML
                        ,'')
        
        cs_gen = cs_engine( x
                           ,WORKING_FOLDER_NAME + "\\code\\"
                           ,WORKING_FOLDER_NAME + '\\md\\'
                           )

    logging.shutdown()

    # Sanity Checks
    # Check for Config File in Working Folder
    # Check if Config Entry with valid control switches exist
    
    # if OPERATION.upper().strip() == 'RUN':
    #    gen_config_file(list_of_files)
