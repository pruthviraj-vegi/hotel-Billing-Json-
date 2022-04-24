import json
import os

os.chdir(os.path.expanduser('~/Documents'))


class JsonFile:
    def __init__(self):

        self.data_list = None
        self.object_id = None
        self.data = None
        self.collection = None
        self.path_dir = os.path.join('Senior')

        if os.path.isdir(self.path_dir):
            pass
        else:

            os.makedirs(self.path_dir)
            lst = []
            with open(os.path.join(self.path_dir, 'Bills.json'), 'w') as fp:
                json.dump(lst, fp)
            with open(os.path.join(self.path_dir, 'Stock.json'), 'w') as fp:
                json.dump(lst, fp)
            with open(os.path.join(self.path_dir, 'Active.json'), 'w') as fp:
                json.dump(lst, fp)

    def getJsonPath(self, collection):
        self.collection = collection
        file_path = os.path.join(self.path_dir, f'{self.collection}.json')
        if os.path.isfile(file_path):
            return file_path

    def addDataToJson(self, collection, data):
        self.collection = collection
        self.data = data
        with open(self.getJsonPath(self.collection), 'r') as file:
            lst = json.load(file)

        lst.append(self.data)

        with open(self.getJsonPath(self.collection), 'w') as file:
            json.dump(lst, file)

    def readJsonData(self, collection):
        self.collection = collection

        with open(self.getJsonPath(self.collection), 'r') as file:
            lst = json.load(file)
        return lst

    def deleteJsonData(self, collection, object_id):
        self.collection = collection
        self.object_id = object_id

        with open(self.getJsonPath(self.collection), 'r') as file:
            lst = json.load(file)
        try:
            for i in lst:
                if i['_id'] == self.object_id:
                    lst.remove(i)
        except BaseException:
            pass
        with open(self.getJsonPath(self.collection), 'w') as file:
            json.dump(lst, file)

    def updateJsonData(self, collection, object_id, data_list):
        self.collection = collection
        self.object_id = object_id
        self.data_list = data_list

        with open(self.getJsonPath(self.collection), 'r') as file:
            lst = json.load(file)
        try:
            for i in lst:
                if i['_id'] == self.object_id:
                    i = self.data_list
                    print('updated')
                    break
        except BaseException:
            pass
        with open(self.getJsonPath(self.collection), 'w') as file:
            json.dump(lst, file)


