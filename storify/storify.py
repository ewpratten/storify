import os
from meta import PackageMeta

class StorageManager:

    class __StorageHelper:
        def getStorifyBasePath(self):
            """ Returns the base path for storify """

            # For now, we don't need a config to change this
            return os.path.expanduser("~") + "/.storify"
        
        def packageExists(self, meta: PackageMeta):
            """ Does the specified package already have a directory and meta file? """

            # Construct folder name from meta
            directory_path = self.getStorifyBasePath() + "/packages/" + meta.dirstr()
            directory_config = directory_path + "/__META__.json"

            # Return if the folder exists and the config exists
            return os.path.exists(directory_path) and os.path.exists(directory_config)
        
        def createPackage(self, meta: PackageMeta):
            pass

    ## End StorageHelper ##

    def __init__(self, package_name: str, meta: PackageMeta):
        """ Create a new StorageManager for your program """

        # Check if package exists
        package_exists = self.__StorageHelper.packageExists(meta)

        # If not, initalize the package
        if not package_exists:
            self.__StorageHelper.createPackage(meta)
    
    def getPath(self):
        pass
    
    def dumpVar(self, name: str, var):
        # /vars/:name
        pass
    
    def loadVar(self, name: str):
        pass
    
    def write(self, rel_path: str, data, flags):
        # Make sure rel_path starts with /
        pass
    
    def read(self, rel_path: str, flags):
        pass
    
    def put(self, key, val):
        pass
    
    def get(self, key):
        pass


