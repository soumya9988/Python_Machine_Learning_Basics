import re
text = 'English 101 Computer Science 102 Image Processing 103 Optical Studies'
re_obj = re.compile('\d+')
split_obj = re_obj.split(text)
if split_obj:
    print('Split object is ', split_obj)
find_num = re_obj.findall(text)
if find_num:
    print('Findall is ', find_num)
search_num = re_obj.search(text)
if search_num:
    print('Search group is: ', search_num.group())
match_num =  re_obj.match(text)
if match_num:
    print('Match group is: ', match_num.group())

re_num = re.compile('\d')
sub_val = re_num.sub('X', text)
if sub_val:
    print('Substituted value is: ', sub_val)

match = re.compile(r'[^A-Za-z0-9]')
check = match.search('Abcdefgh#0hsjjs@')
if check:
    print('Success', check.group())

emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

pattern = re.compile(r'(\w+)@([A-Z0-9]+)\.([a-z]{2,4})', re.IGNORECASE)
split_user_id = pattern.findall(emails)
if split_user_id:
    for item in split_user_id:
        print('user name:', item[0], 'Domain:', item[1], 'Suffix:', item[2])

text = """Betty bought a bit of butter, 
But the butter was so bitter, 
So she bought some better butter, 
To make the bitter butter better."""
text_compile = re.compile(r'\bb\w*', re.IGNORECASE)
words_with_b = set(text_compile.findall(text))
if words_with_b:
    print(words_with_b)

sentence = """A, very   very; irregular_sentence"""
sub_sent = re.sub(r'\W+', ' ', sentence)
print(sub_sent)

tweet = '''Good advice! RT @TheNextWeb: What I would do differently 
if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet_re = re.compile(r'(A-Z\w+)', re.IGNORECASE)
sent_tweet = tweet_re.findall(tweet)
if sent_tweet:
    print(sent_tweet)


string = 'Python exercises, PHP exercises, C# exercises'
pattern = re.compile(r'exercises', re.IGNORECASE)
check = pattern.finditer(string)
for item in check:
    print('Check:', item.group(), item.start(), item.end())


fox_str = 'The quick brown fox jumps over the lazy dog.'
pattern = re.compile(r'fox', re.IGNORECASE)
check = pattern.search(fox_str)
if check:
    print('Fox at: ', check.group(), check.start(), check.end())

list_words = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
pattern = re.compile(r'\(\.\w+\)')
for item in list_words:
    new_word = pattern.sub('', item)
    print('Word: ', new_word)

