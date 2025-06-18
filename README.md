# reco_letter

This project is hosted in college server. Following is link to access it:
https://recommendation-generator.bct.itclub.pp.ua/

# How to run?

* Create a python virtual environment

```
 python -m venv venv
```

Activate virtual environment
Firstly, go to the project directory.
Then run,
# In windows 
```
./venv/Scripts/Activate.ps1
```

# In Unix
```
source venv/bin/activate
```

Install all the requirements
```
python -m pip install -r ./requirements.txt
```

This repo is in production. Configure database before running locally. 

Perform migration
```
python manage.py migrate
```

Create a superuser
```
python manage.py createsuperuser
```

Activate the server
```
 python manage.py runserver
```

* Open web browser and you know what to do, right?
# For admin
	1. Open admin panel, 
	2. Create Programs: Example BE
	3. Create Departments: Example BCT
	4. Create Teacher info


# For student
	1. Register
	2. Login
	3. Request for the recommendation letter
	
# For teacher 
	1. Ask the admin to create your profile
	2. Login
	3. View requests (You can also view the list of students that you have recommended.)
	4. Generate the recommendation letter 
	



# Enjoy & have a good day.
# Recommendation-Letter-Generator
