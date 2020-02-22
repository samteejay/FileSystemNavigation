"""
Program: filesys.py
Author:Samuel O Tjani
Provides a menu-driven tool for navigating a file system
and gathering information on files.
"""

import os, os.path
QUIT = '7'
COMMANDS = ('1', '2', '3', '4', '5', '6', '7')
MENU = """1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a filename
7   Quit the program"""

def main():
   while True:
       print(os.getcwd())
       print(MENU)
       command = accept_command()
       run_command(command)
	   #  to be cont
   
def accept_command():
    """Inputs and returns a legitimate command number."""
	while True:
	    command = eval(input(“Enter a number: “))
		if not command in COMMANDS:
		    print(“Error: command not recognized”)
		else:
		    return commmand
			
def run_command(command):
    """Selects and runs a command."""
    if command == '1':
        list_current_directory(os.getcwd())
	elif command == '2':
	    move_up()
	elif command == '3':
	    move_down(os.getcwd())
	elif command == '4':
        print “The total number of files is”, \
              count_files(os.getcwd())
		#  to be cont
	
def list_current_directory(dir_name):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(dir_name)
	for element in lyst:
	    print(element)
		
def move_up():
	"""Moves up to the parent directory."""
	os.chdir("..")
	
def move_down(current_dir):
    new_dir = input(“Enter the directory name: “)
	if os.path.exists(current_dir + os.sep + new_dir) and \
	   os.path.isdir(new_dir):
	    os.chdir(new_dir)
	else:
        print(“ERROR: no such name”)
		
def count_files(path):
    """Returns the number of files in the cwd and
    all its subdirectories."""
    count = 0
	lyst = os.listdir(path)
	for element in lyst:
	    if os.path.isfile(element):
		    count += 1
		else:
		    os.chdir(element)
			count += count_files(os.getcwd)
			os.chdir("..")
	return count
	