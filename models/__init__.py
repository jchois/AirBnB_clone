#!/usr/bin/python3
"""Instance of Application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
