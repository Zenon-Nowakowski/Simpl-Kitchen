# Simpl-Kitchen

To run:
1. Clone the simplkitchen repository using the git clone command.
2. Clone your personal branch (Dan, Zenon, Jace, Scott) using dev as the source 
3. If you haven't done so already run "pip install virtualenv" to download a virtual environment package. 
4. Run "python3 -m venv env" inside your simpl-kitchen directory. You should now have a folder called env inside the main Simple-Kitchen folder. 
5. To activate the virtual environment on windows cd to the env\Scripts folder and run "./activate"
6. Move back to the main Simpl-Kitchen directiory and run "pip install -r requirement.txt 
7. From the Simpl-Kitchen folder run "uvicorn main:app --reload"

Notes: 
1. Do not push changes from your personal branch to main branch. Only go personal -->> dev.