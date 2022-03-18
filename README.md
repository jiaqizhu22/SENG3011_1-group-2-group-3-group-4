# SENG3011_1-group-2-group-3-group-4

## Team Members
- Joel Ivory (z5162834) 
- Hoshang Mehta (z5255679) 
- Lachlan Sutton (z5308261) 
- Jiaqi Zhu (z5261703) 
- William Wan (z5311691) 


## Package Management: Poetry 
How to Install poetry locally: 
`pip install poetry`
How to use poetry to install packages:
`poetry install` 
To add a package into poetry, run: 
`poetry add <package_name>`


## React Frontend
Run frontend: 
`cd PHASE_2/frontend/` 
`npm start` 


## Starting Swagger API: index.html page
- Locating to folder:
`cd PHASE_1/API_SourceCode/`
- Run poetry virtual environment:
`poetry shell`
- Update all packages:
`poetry update`
- Running server:
`python manage.py runserver`
- Or alternatively run server without a virtual environment:
`poetry run python manage.py runserver`


## Create Database
- Locating to folder:
`cd PHASE_1/API_SourceCode/`
- Run poetry virtual environment:
`poetry shell`
- Include scraper app:
`python manage.py makemigrations scraper`
- Return SQL to corresponding migration names:
`python manage.py sqlmigrate scraper 0001`
- Create model tables in my database:
`python manage.py migrate`


## 3-step guide to making model changes
- Change your models (in models.py).
- Run  `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database.


## Version Control: Git 
- Create a new branch: 
`git checkout -b branch_name` 
- List all branches: 
`git branch` 
- Committing: 
`git add my_file.py` 
`git commit -m "Optimized the performance of my_file"` 
`git commit -am "Outstanding changes"` 
- Switch branch: 
`git checkout master` 
- Pull from master/main branch: 
`git pull upstream main` 
- Update local feature branch: 
`git rebase main` 




