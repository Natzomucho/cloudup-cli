class Error():
    def __init__(self, error):
        self.error = error
    
    def not_found(self, file_type, file_name):
        print('The {} file `{}` was not found'.format(file_type, file_name))