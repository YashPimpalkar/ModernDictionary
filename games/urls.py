from django.urls import path

from . import views

urlpatterns = [
    path('games', views.game_home, name='games'),
    path('fillintheblanksgame', views.fill_in_the_blanks, name='fillintheblanksgame'),
    path('vocabularygame', views.vocabulary_game, name='vocabularygame'),
    path('guessthepicture', views.guess_the_picture, name='guessthepicture'),
    path('jumbledwords', views.jumbled_words_game, name='jumbledwords'),
    path('spellbee', views.spellbee, name='spellbee'),
    path('download', views.download, name='download'),
    path('hangman', views.hangman, name='hangman'),
    path('blogs', views.blogs, name='blogs'),
    path('historyofdictionary', views.historyblog, name='historyofdictionary'),
    path('communicationskills', views.communication, name='communicationskills'),
    path('englishlanguage', views.englishlanguage, name='englishlanguage'),
    path('abbreviation', views.abbreviation, name='abbreviation'),
    path('vocabulary', views.vocabulary, name='vocabulary'),
    path('grammar', views.grammar, name='grammar'),
    path('betterenglish', views.better_english, name='betterenglish'),
    path('readingstrategies', views.reading_strategies, name='readingstrategies'),
    path('aboutus', views.about_us, name='aboutus'),
    path('privacy', views.privacy, name='privacy')
]
