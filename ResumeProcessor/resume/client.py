import requests

url = 'http://127.0.0.1:8000/api/extract_resume/'
files = {'file': open('Resume Path (in pdf or docx format)', 'rb')}
response = requests.post(url, files=files)
print(response.json())

# This is our client application.
# our sample resume is SampleResume.pdf


#expected output : {'first_name': 'KIAN', 'email': 'kianmarsh@email.com', 'mobile_number': '456-7890'}

