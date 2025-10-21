sudo find /root -maxdepth 1 -type f -name "*log*" -exec mv {} ~/logs/ \;
# Explanation :
# sudo: since im a non root user
# find: starts searching in directories
# maxdepth: defines how many subdirectories to dive into, this is kept 1 as we want to search only in root directory
# type f: to make sure only files are taken
# name "*log*" : regex statement that matches files that has log somewhere in their name
# exec mv: executes a move function if file is found that moves files in logs folder of home directory
# \; : ensures exec is ended properly
