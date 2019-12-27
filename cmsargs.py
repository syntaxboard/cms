import argparse

# Class to handle Custom Error Messag in case an invalid argument is passed
class ArgParser():

    def __init__(self):

        parser = argparse.ArgumentParser()

        # Argument
        parser.add_argument('-genfolder',  help="Usage: -genfolder working-path, working root folder, TICMS folder structure is created here", type=str)
        parser.add_argument('-genconfig',  help="Usage: -genconfig config-file-path, Config file in the specified path", type=str)
        parser.add_argument('-run',  help="-run config-file-path, Convert Code to MD, Split Code files and generate docx files", type=str)

        args = parser.parse_args()

        if args.genfolder is not None:
            self.action = "genfolder"
            self.working_folder = args.genfolder
        elif args.genconfig is not None:
            self.action = "genconfig"
            self.working_folder = args.genconfig
        elif args.run is not None:
            self.action = "run"
            self.working_folder = args.run
        else:
            print("")
            print("\t","Please enter one of the following options:")
            print("")
            print("\t","-genconfig config-file-path".ljust(40," "), "Generate Template Config file in the specified code files path, defaults to current run path.")
            print("\t","-genfolder config-file-path".ljust(40," "), "Generates Base folder structure for code, code split, md, md split and docx files using config file.")
            print("\t","-run config-file-path".ljust(40," "), "Generates MD, Split Code and docx files using config file.")



"""
    # Handle Incorrect Options
    def error(self, message):
        # sys.stderr.write("Hello")
        print("")
        self.print_help()
        sys.exit(2)


    # Function to handle the arguments and its values, to perform an action
    def governer(self, genconfig=0, run=0, args):

        for key, value in kwargs.items():
            print ("%s == %s" %(key, value))

        cwd = os.getcwd()

        print("");
        if run != 0:
            top.Run()
        elif genconfig != 0:
            top.GenConfig()
        else:
            print("Please enter one of the following options:")
            print("")
            print("\t","-genconfig config-file-path".ljust(40," "), "Generate Template Config file in the specified path and defaults to current run path.")
            print("\t","-run config-file-path".ljust(40," "), "Convert the MD files to HTMLs using config file.")
"""
