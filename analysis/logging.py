# --------------------------------------------------------------------------------
# Author: Loping151
# GitHub: https://github.com/Loping151/pytools151
# Description: This repository contains a collection of Python tools designed to
#              enhance productivity and simplify various tasks. The code is open
#              for use and can be freely used, modified, and distributed.
# License: MIT License - Feel free to use and modify the code as you wish.
# --------------------------------------------------------------------------------
import os
import datetime



class Logger:
    def __init__(self, log_dir, level='INFO', log_file_name='.log'):
        self.LEVELS = {
            'DEBUG': 0,
            'INFO': 1,
            'WARNING': 2,
            'ERROR': 3,
            'CRITICAL': 4
        }
        self.log_dir = log_dir
        self.log_file_path = os.path.join(log_dir, log_file_name)
        self.level = self.LEVELS[level]
        os.makedirs(log_dir, exist_ok=True)
        
        with open(self.log_file_path, 'w') as log_file:
            log_file.write("Logger initialized.\n")

    def write(self, message, level='INFO'):
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{current_time}] {message}\n"
        
        if self.LEVELS[level] >= self.level:
            print(log_message)
        
        with open(self.log_file_path, 'a') as log_file:
            log_file.write(log_message)
