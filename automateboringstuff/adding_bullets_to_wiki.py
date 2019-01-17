
import pyperclip
list_lines = []

# Step 1: Copy and Paste from the Clipboard
wiki_text = pyperclip.paste()
print(wiki_text)


# Step 2: Separate the Lines of Text and Add the Star
lines = wiki_text.split('\n')
for line in lines:
    new_line = '*' + line
    list_lines.append(new_line)
new_list = '\n'.join(list_lines)

# Step 3 : Copy modified text back to Clipboard
pyperclip.copy(new_list)

