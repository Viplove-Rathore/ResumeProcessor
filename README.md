## ResumeProcessor

ResumeProcessor is a Django project that provides a REST API to process resumes and extract candidate details like first name, email ID, and mobile number. It uses the Django REST Framework and NLP tools to extract relevant information from PDF or Word resumes.


## Table of Contents

   :- Project Setup
   
   :- Database Configuration
   
   :- API Overview
   
   :- Testing the API

   :- References

   
   
## Project Setup

  Ensure you have the following installed on your local machine:
  
      Python 3.8+
      
      PostgreSQL
      
      Pyresparser
      
      Django
      
      Django-RestFramework

  Note: Use Python 3.9 for Pyresparser Package.

## Installation

 -> git clone https://github.com/Viplove-Rathore/ResumeProcessor.git
 
 -> cd ResumeProcessor

## Database Configuration 
 
   This project uses PostgreSQL as the database for development. Ensure you have PostgreSQL installed and create a database and user with appropriate permissions.Then open Setting.py file , select database section and put all the information for database configuration,
 
   DB_NAME=your_database_name
      
   USER=your_database_user
      
   PASSWORD=your_password
      
   HOST=localhost
      
   PORT=5432

   Note: To connect with Postgresql Database , i share some youtube video link in References section.

   First you need to migrate database then start server for api overview.

    For Migrations use command:
            
            python manage.py Makemigrations
            
            Python manage.py migrate
    
    For Server Starting:
    
            Python manage.py runsever

## API Overview
  
  # Endpoint: /api/extract_resume/
  
    This endpoint accepts a POST request with a resume file (PDF or Word document) and extracts the candidate's first name, email ID, and mobile number.

    URL: /api/extract_resume/
    
    Method: POST
    



## Testing:
    
    A Client.py file is present for api testing. It use Python-Request library for request-response.
    Share your resume file path and send request to the server, in response you get information like ,

    {
    
    "first_name": "John",
    
    "email": "john.doe@example.com",
    
    "mobile_number": "123-456-7890"
    
    }


## References       

   For Database configuration: https://www.youtube.com/watch?v=unFGJhIvHU4

   For Pyresparser: Use Python 3.10 or less version

   
    


