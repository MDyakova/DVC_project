# DVC_project

# data to dvc (don't launch)

1. dvc init
2. create directory on Google Drive and copy the folder id.
3. dvc remote add -d myremote gdrive://1TmcxBGISOvYFCOfJCEs-iGhODMNC2XPw
4. git add .
5. git commit -m "text"
6. dvc add heart.csv
7. git add heart.csv.dvc .gitignore
8. dvc push


# get data
1. git clone this repo
2. dvc pull heart.csv
3. 