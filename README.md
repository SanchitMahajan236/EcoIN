# EcoIN
A place where you can find all the answers related to your environment concerns.

# Live Deployment
View live deployment at https://localhost:8000

# Installiation
### Requirements
Install PIP in your local system.

If not then follow these commands
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python get-pip.py
```
Fork / Download this respository to you local computer.
### Fork
After Forking,
create a new folder in you local computer
Then type the following commands
```
git init
```
```
git clone https://github.com/SanchitMahajan236/EcoIN.git
```
### Download
Directly download the repository

VirtualEnvironment is suggested. So incase if you dont have a virtual environment
```
pip install virtualenvwrapper
```
Now create a new virtual environment.
In this case I am calling my virtual environment as `VirtualEnv`.
```
python -m venv VirtualEnv
```

If you already have an existing virtual environment then activate it by
```
VirtualEnv\Scripts\activate
```

Now install the requirements (this is a one time command, no need to run this again).
```
pip install -r requirements.txt
```
If there is any issue in above step, try the following command to install pillow, and rerun the above command
```
python -m pip install pillow
```

# Running the code
Navigate to the directory which has `manage.py` in it.
In this case it is in backend
i.e `.../EcoIn/backend`
then type
```
python manage.py runserver
```

You can view the website at
```
localhost:8000   or http://127.0.0.1:8000
```
