start1 = ['fee', 'fie', 'foe']
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for i in rhymes:
    row = ''
    for k in start1:
        row += k.capitalize() + '! '
    row += i[0].capitalize() + '!'
    print(row + '\n' + start2 + ' ' + i[1] + '.')
