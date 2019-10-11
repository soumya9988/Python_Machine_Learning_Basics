story = []
format_story = ''


def sentence_maker(phrase):
    interrogative = ('what', 'why', 'when', 'how')

    capitalise = phrase.capitalize()
    if phrase.startswith(interrogative):
        punctuation = '?'
    else:
        punctuation = '.'
    capitalise += punctuation
    return capitalise


while True:
    user_input = input('Enter the phrase of the story. Type quit to exit: ')
    if user_input.lower() == 'quit':
        break
    else:
        story.append(sentence_maker(user_input))

if story:
    format_story = ' '.join(story)
    print(format_story)

