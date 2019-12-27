import os

class cs_engine():

    
    def __init__(self, p_code_path, p_split_file_path, p_code_file):
        # Read
        self.code_splitter(p_code_path, p_code_file)
        
    def write2file(self, p_split_file_path, p_file_name,p_file_content):
        new_file = open(p_split_file_path + p_file_name, "a")
        new_file.write(p_file_content)
        new_file.close()
    
    def code_splitter(self, p_code_path, p_split_file_path, p_code_file):
        fp = open(p_code_path + p_code_file,"r")  
        line = fp.readline()
        l_count = 1
        
#        l_md_count = 0
        l_md_start = 0
        l_code_start = 0
        l_code_end = 0
        l_file_name = ''
        # Code / MD Block
        l_block = ''
        l_class_sep = '```'
        
        while line: 
               file =line.strip()
               #file=" ".join([a.strip() for a in b.split("\n") if a])
               #print(file)
               
               input_file = open(file,"r")
               #print (input_file)
               l_filename=os.path.basename(file).split(".")[0]   
               l_counter =1
               #print (l_filename)
               while True:
                    curr_line =input_file.readline() # Read line by line, to variable current line
                    if not curr_line:
                        break                          # Break if there is no line to read
                    
                    l_line = curr_line #.replace('## >','').rstrip()
                    
                    # print(l_line)
                    
                    # Detect Code End
                    if  l_line.find(l_class_sep) >= 0  and l_code_start == 1 and l_md_start == 1:
                        l_code_end = 1
                        l_code_start = 0
                        l_md_start = 0
                        l_counter+=1
                        print(l_filename)
        #                print(" == Block Start == ")
        #                print(l_block)
        #                print("== Block End == ")
                        self.write2file(p_split_file_path, l_file_name, l_block)
                        
                        l_block = ''
                        
                    # Detect Code Start                               
                    if l_line == l_class_sep and l_code_start == 0 and l_md_start == 1:
                        l_code_start = 1
                        l_code_end = 0
                        
                    # Detect MD    
                    if l_line[0:1] == '#' and l_md_start == 0:
                        l_file_name = curr_line.replace('#','').strip()
                       # l_file_name = l_filename + str(randint(0, 1000)) +'.py'
                        l_file_name = l_filename + str(l_counter) +'.py'
                        l_md_start = 1
                        l_code_end = 0
                        
                    # Generate Block
                    if l_code_start == 1 and l_md_start == 1 and l_code_end == 0:
                        if l_line != l_class_sep:
                            l_block = l_block  + '\n' + l_line
                            
               line = fp.readline()
               l_count += 1
                # Close the File stream handler
               input_file.close()
        fp.close()