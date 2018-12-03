import string


word = 'banana'
def count_char(text, aChar):
    lettercount = 0
    for c in text:
        if c == aChar:
            lettercount = lettercount + 1
    return lettercount


print(count_char(word, "a"), word.count('a'))

instruction = """Heat oven to 350°F. Prepare two 8-inch round cake pans by buttering (or spraying) and then adding a 
piece of parchment to the bottom of the pan.Sift together cake flour, baking powder and salt in a medium bowl and set 
aside. In the bowl of a stand mixer with whisk attachment cream together butter and sugar on medium-high until light 
and fluffy, at least 3 minutes. Lower speed to medium and add in egg yolks, one at a time, whisking after each addition.
With the mixer on low, add in milk and vanilla and fully incorporate. (usually about 1 minute)
Remove bowl from mixer and fold flour mixture into butter mixture. Mix until just combined.
In a small bowl add the melted butter and cocoa and mix until combined.
Add 3/4 cup of the yellow cake batter into the cocoa/butter mixture and fold together.
Now add 3/4 cup of yellow cake batter to each cake pan and smooth out.
Divide the chocolate batter evenly between the two pans by dropping spoonfuls in a circle over the yellow batter.
Divide the remaining yellow cake batter between the pans and smooth out as much as possible without mixing.
Take a clean table knife and make a swirling pattern throughout the cake to gently achieve the marble effect.
Bake for 20-30* minutes or until an inserted toothpick is removed clean. Start checking the cake at 20 minutes. In the 
winter I can get away with a 22 minute bake time but in the summer it increases to 28 minutes. Just keep a close eye on
it. Cool for about 10 minutes then turn out onto a wire rack.
"""

count_alpha = 0
count_digit = 0
count_e = 0
for char in instruction:
    if char in string.ascii_letters:
        count_alpha += 1
        if char.upper() == 'E':
            count_e += 1
    elif char in string.digits:
        count_digit += 1
perc_e = count_e / count_alpha * 100


print('No of alphabets are %d, digits are %d and no of E are %d %.2f)' % (count_alpha, count_digit, count_e, perc_e))
