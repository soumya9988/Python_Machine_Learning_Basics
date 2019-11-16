import bs4

# Finding an Element with the select() Method.
# Selectors are like regular expressions: They specify a pattern to look for,
# in this case, in HTML pages instead of general text strings

with open('example.html', 'r') as html_file:
    html_text = html_file.read()
soup_obj = bs4.BeautifulSoup(html_text, 'html.parser')
file_author = soup_obj.select('#author')
print(file_author[0].text, file_author[0].attrs)

dir_obj = soup_obj.select('p')
len_dir_obj = len(dir_obj)
for i in range(len_dir_obj):
    print(dir_obj[i].get_text())

span_elem = soup_obj.select('span')
print(span_elem[0].get('id'), span_elem[0].get_text())

