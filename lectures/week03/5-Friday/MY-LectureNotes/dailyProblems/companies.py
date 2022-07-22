import imghdr
import data 

#? Loop through the company data and display logo image and company name on an html page. 
#* to run the file:  python companies.py > index.html

companies = data.data

html = """

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Companies</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/css/bootstrap.min.css" integrity="sha384-r4NyP46KrjDleawBgD5tp8Y7UzmLA05oM1iAEQ17CSuDqnUK2+k9luXQOfXJCJ4I" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.0.0-alpha1/js/bootstrap.min.js" integrity="sha384-oesi62hOLfzrys4LxRF63OJCXdXDipiYWBnvTl9Y9/TRlw5xlKIEHpNyvvDShgf/" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<div class="container">
"""
color = 'bg-warning'


new_html = ''


for i in companies:
  if color == 'bg-warning':
    color = 'bg-danger'
  else: color = 'bg-warning'
  
  new_html += f"""
    
    <div class="row">
      <div class="col-6 {color}">
        {i['business_name']}
      </div>
      <div class="col-6">
        <img src="{i['logo']}" alt="business_logo">
      </div>
    </div>
  """


html+= new_html



html += """
</div>
</body>
</html>

"""

print(html)