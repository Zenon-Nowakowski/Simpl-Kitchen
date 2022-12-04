# Simpl-Kitchen

To run:
1. Clone your personal branch (Dan, Zenon, Jace, Scott)
2. Run "pip install virtualenv" to download a virtual environment package.
3. Run "python3 -m venv env" inside your simpl-kitchen directory
    - You should now have a folder called env and it will look like this:  
4. To activate the virtual environment on windows cd to the env\Scripts folder and run "./activate"
5. Move back to the main Simpl-Kitchen directiory and run "pip install -r requirement.txt 
6. In mysql workbench create a schema called "serversiderendering" and make it your default schema.
7. In database.py change SQLALCHEMY_DATABASE_URL to be your database server. 
8. From the Simpl-Kitchen folder run "uvicorn main:app --reload"

Notes: 
1. Do not push changes from your personal branch to main branch. Only go personal -->> dev.