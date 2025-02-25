import os
import shutil
import datetime


def make_reserve_arc(source, dest):
    mamka = source.split('/')
    shutil.copy(source, dest)
    os.chdir(dest)
    shutil.make_archive(str(datetime.datetime.now()), "zip", root_dir='/'.join((dest, mamka)))