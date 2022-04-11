# Installation On Replit

**Breaf information** : By Default the replit online ide uses the Virtual Environment By the Poetry So For Like Adding or Deleting any Projects Mostly Done With Poetry Shell Even if You Are thinking to deploy the Project to replit.

## Getting the Repo On Your Repl

There are 2 ways to get this repo template in repl project.

1. Direct from Replit Shell
2. By Forking This Repo to Github

### 1. Direct from Replit Shell

Follow Given Below Steps.

- Create an Repl With Python Language On Replit.com With Whatever name you want.
- Open Its Shell for Command-line
- Type and Enter `ls` List Files are in Current Repl and Remove all of them With `rm filename.txt` One By One.
- Clone This Repo Into Current Directory By `git clone https://github.com/shriekdj/django_project_template .` and Project Cloned.
- Run `poetry install` for installing dependencies.
- Goto Project `settings.py` and Change Whatever you Want to Change.
- Create Migrations With `python manage.py makemigrations`.
- Run Migrate With `python manage.py migrate`.
- For Running Server Just Click Run Button.
  - It Is Already Configured in `.replit` file to what should be run.

> I Know There Many Ways Out there but it is Completely Tried Process with Minimum Errors.
