import os
import shutil

def copy_static_to_public():

    static_dir = "static"
    public_dir = "public"

    ### Copy all content from static/ to public/ ###

    #Check whether public dir exists
    if os.path.exists(public_dir):
        #Delete all contents of public/ to ensure copy is clean
        shutil.rmtree(public_dir)

    #Remake fresh copy of public directory
    os.mkdir(public_dir)

    ## Copy all files and subdirectories recursively ##

    # Sample output of the os.walk() function:
        # [
        #   ('static', ['images', 'testing'], ['index.css']),
        #   ('static/images', [], ['rivendell.png']),
        #   ('static/testing', [], [])
        # ]

    # 
    static_dir_contents = []
    for root, dirs, files in os.walk(static_dir):
        static_dir_contents.append((root, dirs, files))

    for item in static_dir_contents:
        
        root_dir = item[0] #This will be a string
        child_dirs = item[1] #This will be a list of strings
        child_files = item[2] #This will be a list of strings

        #Only need to create child directories once.
        #Some results of the os.walk() function will lead to blank 'dirs' lists
        #If the child_dirs list is blank, then we don't need to make any new directories
        if child_dirs:
            for child_dir in child_dirs:
                dst_root_dir = root_dir.replace(static_dir, public_dir, 1)
                dst_dir_path = os.path.join(dst_root_dir, child_dir)
                os.mkdir(dst_dir_path)

        for file in child_files:
            file_path = os.path.join(root_dir, file)
            dest_file_path = file_path.replace(static_dir, public_dir, 1)
            shutil.copy(file_path, dest_file_path)