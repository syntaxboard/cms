import io
import os
from cmslogger import CMSLog
from cmsconfig import ConfigGen

class CMSOps():

    def __init__(self, p_LogObj, p_action, p_working_folder):

        self.working_folder = p_working_folder

        # Process based on p_action
        if p_action == "genfolder":
            self.genfolder(p_LogObj)

        elif p_action == "genconfig":
            self.genconfig(p_LogObj)
            
        elif p_action == "run":
            self.run(p_LogObj)


    ############################################################################
    # CHECKPATH
    # Checks the given folder-path and Returns true or false if exists or not
    ############################################################################
    def checkpath(self):

        try:
            if os.path.isdir(self.working_folder):
                return True
            else:
                return False
        except:
            return False


    ############################################################################
    # GENFOLDER
    # Generates the genfolder folder structure
    ############################################################################
    def genfolder(self,p_LogObj):

        if self.checkpath():

            p_LogObj.error("Attempting to create \code, \md, \docx folders in: " + self.working_folder)
            print("Attempting to create \code, \md, \docx folders in:",self.working_folder)

            try:
                os.mkdir(self.working_folder + '\code')
                os.mkdir(self.working_folder + '\md')
                os.mkdir(self.working_folder + '\docx')
            except:
                p_LogObj.error("Cannot create \code, \md, \docx folders in " + self.working_folder)
                print("Cannot create \code, \md, \docx folders in",self.working_folder)

        else:
            p_LogObj.error(self.working_folder + " Path specified is invalid, please provide a valid path.")
            print(self.working_folder, "Path specified is invalid, please provide a valid path.")


    ############################################################################
    # GENCONFIG
    # Generates the Config File
    ############################################################################
    def genconfig(self,p_LogObj):
        print(self.working_folder)
        l_config_file_content = """
    [TICMS-CONFIG]
    log_path=
    code_source_folder_path=
    md_target_folder_path="""

        if self.checkpath():
            ObjCfg = ConfigGen(p_LogObj, self.working_folder)
            
        else:
            p_LogObj.error(self.working_folder + " Path specified is invalid, please provide a valid path.")
            print(self.working_folder, "Path specified is invalid, please provide a valid path.")


    ############################################################################
    # RUN
    # Run based on the config file
    ############################################################################
    # Read Config File
    def run(self,p_LogObj):
        print(self.working_folder)
        # self.LogObj(

        if self.checkpath():
            with  open(self.working_folder) as f:
                print("Run")
                p_LogObjj("Run")
        else:
            self.LogObj.error("Invalid Path")
            print("Invalid Path")
