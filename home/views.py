import bs4
import pyttsx3
import requests
import speech_recognition as sr
from django.shortcuts import render

from . import models

base_url = 'https://www.dictionary.com/browse/{}'
base_url1 = 'https://www.thesaurus.com/browse/{}'
title = ''
final_meaning = ''
final_example = ''
synonyms = ''
synonyms2 = ''
antonyms = ''
antonyms2 = ''
data_for_search = {}
data_for_mic = {}


def home(request):
    word_of_the_day_url = 'https://www.dictionary.com/e/word-of-the-day/'
    res = requests.get(word_of_the_day_url)
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    title_word = soup.select('h1')
    raw_title = title_word[2].text
    product = soup.select('p')
    raw_product = product[2].text
    final_title = raw_title.capitalize()
    raw_product1 = raw_product.replace(final_title, '')
    final_product = raw_product1.capitalize()
    word_of_the_day = {
        'final_title': final_title,
        'final_product': final_product
    }
    return render(request, 'base.html', word_of_the_day)


def new_search(request):
    global base_url, title, final_meaning, final_example, data_for_search
    global synonyms, antonyms, base_url1, synonyms2, antonyms2
    title = ''
    final_meaning = ''
    final_example = ''
    data_for_search = {}
    synonyms = ''
    synonyms2 = ''
    antonyms = ''
    antonyms2 = ''
    try:
        search = request.POST.get('search')
        models.Search.objects.create(search=search)
        res = requests.get(base_url.format(search))
        soup = bs4.BeautifulSoup(res.text, features='html.parser')
        meaning = soup.findAll('span', {'one-click-content css-nnyc96 e1q3nk1v1'})
        meaning1 = str(meaning[0].text).strip()
        if ':' in meaning1:
            index = meaning1.find(':')
            final_meaning = meaning1[0:index].capitalize()
        else:
            final_meaning = meaning1.strip().capitalize()
        example = soup.findAll('span', {'luna-example italic'})
        example1 = str(example[0].text)
        final_example = example1.strip().capitalize()
        title = search.capitalize()
        res1 = requests.get(base_url1.format(search))
        soup1 = bs4.BeautifulSoup(res1.text, features='html.parser')
        synonyms1 = soup1.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
        synonymslist = set()
        for i in synonyms1[0:10]:
            if str(i.text) == '':
                synonyms = 'There are no synonyms for this word.'
                break
            c_word = str(i.text)
            synonymslist.add(c_word.capitalize())
        synonyms = ','.join(synonymslist)
        synonyms2 = ';'.join(synonymslist)

        antonyms1 = soup1.find_all('a', {'class': 'css-15bafsg eh475bn0'})
        antonymslist = set()
        for i in antonyms1[0:10]:
            if i.text == '':
                antonyms = 'There are no antonyms for this word.'
                break
            c_word = str(i.text)
            antonymslist.add(c_word.capitalize())
        antonyms2 = ';'.join(antonymslist)
        antonyms = ','.join(antonymslist)

    except IndexError:
        data_for_search = {
            'title': title,
            'final_meaning': final_meaning,
            'final_example': final_example,
            'synonyms': synonyms,
            'antonyms': antonyms,
        }
        return render(request, 'search.html', data_for_search)
    data_for_search = {
        'title': title,
        'final_meaning': final_meaning,
        'final_example': final_example,
        'synonyms': synonyms,
        'antonyms': antonyms,
    }
    return render(request, 'search.html', data_for_search)


def mic(request):
    global base_url, title, final_meaning, final_example
    global data_for_mic, synonyms, antonyms, base_url1, synonyms2, antonyms2
    title = ''
    final_meaning = ''
    final_example = ''
    synonyms = ''
    synonyms2 = ''
    antonyms = ''
    antonyms2 = ''
    # data_for_mic = {}
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('Listening')
            voice = listener.listen(source)
            command = str(listener.recognize_google(voice))
            command = command.lower()
            print(f'{command}')
            if 'alexa' in command:
                command = command.replace('alexa', '')
                if 'search' in command:
                    command = command.replace('search', '')
                    word = command.strip()
                    res = requests.get(base_url.format(word))
                    soup = bs4.BeautifulSoup(res.text, features='html.parser')
                    meaning = soup.findAll('span', {'one-click-content css-nnyc96 e1q3nk1v1'})
                    meaning1 = str(meaning[0].text)
                    if ':' in meaning1:
                        index = meaning1.find(':')
                        final_meaning = meaning1[0:index].capitalize()
                    else:
                        final_meaning = meaning1.strip().capitalize()
                    example = soup.findAll('span', {'luna-example italic'})
                    example1 = str(example[0].text)
                    final_example = example1.strip().capitalize()
                    title = word.capitalize()
                    res1 = requests.get(base_url1.format(word))
                    soup1 = bs4.BeautifulSoup(res1.text, features='html.parser')
                    synonyms1 = soup1.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
                    synonymslist = set()
                    for i in synonyms1[0:10]:
                        if str(i.text) == '':
                            synonyms = 'There are no synonyms for this word.'
                            break
                        c_word = str(i.text)
                        synonymslist.add(c_word.capitalize())
                    synonyms = ','.join(synonymslist)
                    synonyms2 = ';'.join(synonymslist)

                    antonyms1 = soup1.find_all('a', {'class': 'css-15bafsg eh475bn0'})
                    antonymslist = set()
                    for i in antonyms1[0:10]:
                        if i.text == '':
                            antonyms = 'There are no antonyms for this word.'
                            break
                        c_word = str(i.text)
                        antonymslist.add(c_word.capitalize())
                    antonyms = ','.join(antonymslist)
                    antonyms2 = ';'.join(antonymslist)
                    data_for_mic = {
                        'title': title,
                        'final_meaning': final_meaning,
                        'final_example': final_example,
                        'synonyms': synonyms,
                        'antonyms': antonyms,
                        'command': command
                    }
                    return render(request, 'mic.html', data_for_mic)
                else:
                    # data_for_mic = {
                    #     'title': title,
                    #     'final_meaning': final_meaning,
                    #     'final_example': final_example,
                    #     'synonyms': synonyms,
                    #     'antonyms': antonyms,
                    #     'command': command
                    # }
                    return render(request, 'mic.html', data_for_mic)
            else:
                data_for_mic = {
                    'title': title,
                    'final_meaning': final_meaning,
                    'final_example': final_example,
                    'synonyms': synonyms,
                    'antonyms': antonyms,
                    'command': command
                }
                return render(request, 'mic.html', data_for_mic)
    except sr.UnknownValueError:
        return render(request, 'mic.html', data_for_mic)
    except ValueError:
        return render(request, 'mic.html', data_for_mic)


def talk(request, text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()


def speak(request):
    global title, final_meaning, final_example, data_for_search, \
        synonyms, antonyms, synonyms2, antonyms2
    try:
        if synonyms == '':
            if antonyms == '':
                talk(request, f'Title: {title}')
                talk(request, f'Meaning: {final_meaning}')
                talk(request, f'Example: {final_example}')
                talk(request, f'Synonyms: There are no synonyms for this word.')
                talk(request, f'Antonyms: There are no antonyms for this word.')
        elif antonyms == '':
            talk(request, f'Title: {title}')
            talk(request, f'Meaning: {final_meaning}')
            talk(request, f'Example: {final_example}')
            talk(request, f'Synonyms: {synonyms2}')
            talk(request, f'Antonyms: There are no antonyms for this word.')
        elif synonyms == '':
            talk(request, f'Title: {title}')
            talk(request, f'Meaning: {final_meaning}')
            talk(request, f'Example: {final_example}')
            talk(request, f'Synonyms: There are no synonyms for this word.')
            talk(request, f'Antonyms: {antonyms2}')
        else:
            talk(request, f'Title: {title}')
            talk(request, f'Meaning: {final_meaning}')
            talk(request, f'Example: {final_example}')
            talk(request, f'Synonyms: {synonyms2}')
            talk(request, f'Antonyms: {antonyms2}')
        return render(request, 'search.html', data_for_search)
    except RuntimeError:
        return render(request, 'search.html', data_for_search)


def speaker(request):
    global title, final_meaning, final_example, data_for_mic, \
        synonyms, antonyms, antonyms2, synonyms2
    try:
        if synonyms == '':
            if antonyms == '':
                talk(request, f'Title: {title}')
                talk(request, f'Meaning: {final_meaning}')
                talk(request, f'Example: {final_example}')
                talk(request, f'Synonyms: There are no synonyms for this word.')
                talk(request, f'Antonyms: There are no antonyms for this word.')
        elif antonyms == '':
            talk(request, f'Title: {title}')
            talk(request, f'Meaning: {final_meaning}')
            talk(request, f'Example: {final_example}')
            talk(request, f'Synonyms: {synonyms2}')
            talk(request, f'Antonyms: There are no antonyms for this word.')
        elif synonyms == '':
            talk(request, f'Title: {title}')
            talk(request, f'Meaning: {final_meaning}')
            talk(request, f'Example: {final_example}')
            talk(request, f'Synonyms: There are no synonyms for this word.')
            talk(request, f'Antonyms: {antonyms2}')
        else:
            talk(request, f'Title: {title}')
            talk(request, f'Meaning: {final_meaning}')
            talk(request, f'Example: {final_example}')
            talk(request, f'Synonyms: {synonyms2}')
            talk(request, f'Antonyms: {antonyms2}')
        return render(request, 'mic.html', data_for_mic)
    except RuntimeError:
        return render(request, 'mic.html', data_for_mic)
