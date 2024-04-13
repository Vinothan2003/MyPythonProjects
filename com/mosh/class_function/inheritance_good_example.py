# Perfect example of Inheritance
class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.flag = False

    def open(self):
        if self.flag:
            raise InvalidOperationError("Stream is already open.")
        self.flag = True

    def close(self):
        if not self.flag:
            raise InvalidOperationError("Stream is already close.")
        self.flag = False


class FileStream(Stream):
    def read(self):
        print("Reading data from file..")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Network")


file_stream = FileStream()

file_stream.open()
# file_stream.open()

file_stream.read()

file_stream.close()
# file_stream.close()
