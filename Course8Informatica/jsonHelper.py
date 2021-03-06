#from mysql.connector import connect
import mysql.connector
from flask import render_template, request
import json
import logging

# while in development
logging.basicConfig(filename='db_classes.log', level=logging.DEBUG)

class JSONhelper():

    def __init__(self, jsondir='jsondumps', filename='jsondump.json'):
        from os import sep
        self.filename = filename
        self.outputdir = jsondir
        self.obj = None                  # todo: determine whether none or empty dict.
        self.__check_already_exists()

    def __check_already_exists(self):
        from os.path import isfile, isdir, getsize
        from os import mkdir, sep
        full_relative_path = f'{self.outputdir}{sep}{self.filename}'

        # check if the file exists
        if isfile(full_relative_path):

            # if the file is not empty, try loading it
            if getsize(full_relative_path) != 0:
                try:
                    with open(full_relative_path, 'r') as file:
                        obj = json.load(file)
                        logging.debug(f'succesfully loaded obj: {str(obj)[:100]}')
                        self.obj = obj
                except Exception as e:
                    print(full_relative_path)
                    print(e)
                    logging.debug(e, "couldn't load file", full_relative_path)
                    raise e
            else:
                logging.debug(f"file '{full_relative_path}' was empty", )
                pass

        # else if the directory exists but there is no file, try making it
        elif isdir(self.outputdir):
            try:
                with open(full_relative_path , 'w') as out:
                    pass

            except Exception as e:
                logging.debug(e,"tried to create the file...")

        # else if it doesn't exist, try creating both
        else:
            try:
                mkdir(self.outputdir)
                try:
                    with open(full_relative_path, 'w') as out:
                        pass
                        # still empty so obj none # todo see prev todo
                        self.obj = None
                except Exception as e:
                    logging.debug(e, "tried to create the file...")
            except PermissionError as e:
                logging.debug(e, "tried to create the directory, but no permission..." , self.outputdir)
                raise e
            except Exception as e:
                logging.debug(e, "tried to create the directory and dont know what happened..", self.outputdir)
                raise e

        self.full_relative_path = full_relative_path

    def __save(self):
        with open(self.full_relative_path, 'w') as file:
            json.dump(self.obj, file)


    def append_data(self, data, name='data'):
        if self.obj:
            self.update({name:data})
        else:
            # self.obj doesnt exist, initiate here
            self.obj = {name:data}
            self.__save()

    def update(self, d):
        if self.obj:
            self.obj.update(d)
        else:
            self.obj = d
        self.__save()

    def data(self):
        return self.obj

    def fetch(self, keys, obj=None):
        # translated dotty
        # https://stackoverflow.com/a/35478322/6934388
        if not obj:
            obj = self.obj

        key = keys[0]
        if len(keys) == 1:
            return obj[key]
        else:
            return self.fetch(keys[1:], obj[key])
