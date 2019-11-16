text = "X-DSPAM-Confidence:    0.8475";
position = text.find('0')
print(position)
number = float(text[position:])
print(number)
