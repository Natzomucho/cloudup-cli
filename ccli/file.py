from pathlib import Path

class File():
    def __init__(self, workdir):
        self.workdir =  Path(workdir)

    def exists(self, path):
        
        filename = self.workdir / path

        return filename.exists()