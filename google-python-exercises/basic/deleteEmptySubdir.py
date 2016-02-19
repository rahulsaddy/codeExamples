# Code to walk from CWD and go down deleting empty sub directories
for root, dirs, files in os.walk(os.getcwd()):
    for name in dirs:
        try:
            os.rmdir(os.path.join(root, name))
        except WindowsError:
            print 'Skipping', os.path.join(root, name)