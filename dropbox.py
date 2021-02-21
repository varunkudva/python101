
class VendorId:
    name = None
    vid =

class File:
    file_id
    user_id
    path

class User:
    user_id
    name



class VendorManager:
    def __init__(self):
        self.vendor_map = dict()
        self.vendor_counter = 0
        pass

    def create_id(self):
        self.vendor_counter += 1
        return self.vendor_counter

    def create_storage(self, vendor_id):
        # default storage of 100G
        for server in server_list:
            if server.get_free_storage() > 100:
                path = server.create_path(vendor_id)
                return server.id, path


    def register_vendor(self, name):
        """
        Entry in vendor_id map with path where vendors files are stored
        """
        id  = self.create_id()
        path = create_storage()
        self.vendor_map[id].append(path)


class FileManager:
    def __init__(self):
        pass
    def upload_file(self, vendor_id, user_id):
        # fetch storage of this particular user from vendor servers
         path = VendorManager().get_path(vendor_id, user_id)
         upload(path, file)
        pass


