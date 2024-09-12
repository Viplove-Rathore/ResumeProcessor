from pyresparser import ResumeParser

def extract_resume_data(file_path):
    data = ResumeParser(file_path).get_extracted_data()
    
    first_name = data.get('name', '').split(' ')[0]  # Split first name
    email = data.get('email', '')
    mobile_number = data.get('mobile_number', '')
    
    return {
        'first_name': first_name,
        'email': email,
        'mobile_number': mobile_number
    }
