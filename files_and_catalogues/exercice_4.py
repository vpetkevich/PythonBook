test1 = 'This is a test of the emergency text system'
with open('test.txt', 'rt') as test_txt:
    test2 = test_txt.read()
print(test1 == test2)
