from django.shortcuts import render


def game_home(request):
    return render(request, 'games.html')


def fill_in_the_blanks(request):
    return render(request, 'fillintheblanks.html')


def vocabulary_game(request):
    return render(request, 'vocabularyGame.html')


def guess_the_picture(request):
    return render(request, 'guessthepicture.html')


def jumbled_words_game(request):
    return render(request, 'jumbledwordsgame.html')


def spellbee(request):
    return render(request, 'spellbee.html')


def download(request):
    return render(request, 'download.html')


def hangman(request):
    return render(request, 'hangman.html')


def blogs(request):
    return render(request, 'blogs.html')


def historyblog(request):
    return render(request, 'blogs/historyblog.html')


def communication(request):
    return render(request, 'blogs/communication.html')


def englishlanguage(request):
    return render(request, 'blogs/englishlanguage.html')


def abbreviation(request):
    return render(request, 'blogs/abbreviation.html')


def vocabulary(request):
    return render(request, 'blogs/vocabularyblog.html')


def grammar(request):
    return render(request, 'blogs/grammar.html')


def better_english(request):
    return render(request, 'blogs/betterenglish.html')


def reading_strategies(request):
    return render(request, 'blogs/readingstrategies.html')


def about_us(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')

