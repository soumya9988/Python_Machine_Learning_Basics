# Join and split methods
new_string = ' '.join(['My', 'name', 'is', 'Simon'])
print(new_string)

join_string = 'Hello World There is a cow'
split_string = join_string.split(' ', 2)
print(split_string)


# rjust() ljust() and center()
print('Hello'.rjust(50, '*'))
print('Hello'.ljust(50, '@'))
print('Hello'.center(50, '&'))

# strip(),rstrip() and lstrip()
print('SpamSpamSpamSpamBacon&EggsSpamSpamSpam'.strip('ampS'))
print('           IamBoredToday       '.rstrip())
print('           IAmBoredToday       '.lstrip())
print('           IAmBoredToday       !'.strip())