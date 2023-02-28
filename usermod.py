import requests


def pr_red(red):
    print("\033[91m {}\033[00m" .format(red))


def doth_trans(text):
    """
    https://api.funtranslations.com/translate/dothraki.json?text=Have%20you%20seen%20my%20lady%E2%80%99s%20dragon%3F
    example API call URL
    """
    # text = 'I run another test!'
    punctuation = {' ': '%20', '.': '%2E', '!': '%21', '?': '%3F', "'": '%27'}
    for i in punctuation:
        # print (i)
        new_text = text.replace(i, punctuation[i])
        text = new_text
        # iterates through the dictionary to URL encode the text
        # print(new_text)

    url = 'https://api.funtranslations.com/translate/dothraki.json?text=' + text
    translation = requests.get(url)
    translation = translation.json()
    # print(translation)

    if 'error' in translation:
        pr_red('ERROR ACCESSING API.\nPlease wait 1 hour and try again.')

    else:
        print()
        pr_red(translation['contents']['translated'])
        print(' is Dothraki for: ', end='')
        pr_red(translation['contents']['text'])

