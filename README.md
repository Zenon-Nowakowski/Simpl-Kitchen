# Simpl-Kitchen

To run:
1. Clone the Simpl-Kitchen repository using the git clone command and add the new repository to your workspace folder in VS code.
2. Create your personal branch (Dan, Zenon, Jace, Scott) using dev as the source whichever way you prefer (github desktop, github.com, command line, etc) 
3. If you haven't done so already run "pip install virtualenv" to download a virtual environment package. 
4. Inside the Simpl-Kitchen directory, run "python3 -m venv env". You should now have a folder called env inside the main Simple-Kitchen folder. 
5. To activate the new virtual environment you just made cd to the Simple-Kitchen\env\Scripts folder and run "./activate"
6. Navigate back to the main Simpl-Kitchen directiory and run "pip install -r requirements.txt 
7. From the Simpl-Kitchen folder run "uvicorn main:app --reload"

Notes: 
1. Do not push changes from your personal branch to main branch. Only go personal -->> dev.