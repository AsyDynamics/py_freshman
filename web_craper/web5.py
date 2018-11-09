try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print('Tag not found')
else:
    if badContent == None:
        print('Tag no found')
    else:
        print(badContent)
