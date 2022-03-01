#! /usr/bin/bash

echo "Git token for this is present in the parent directory to this directory. Check there\n"

#execute this file to commit the changes to github
git add -A   # it adds all new files, changes in modified files and remove deleted files.
read -p "Enter some commit for the updated changes or additions: " var
git commit -m "$var"
git push -u origin main


#we can also add it in crontab to automate this
