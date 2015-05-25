# -*- coding: utf-8 -*-
'''

Creative Limitation

http://en.wikipedia.org/wiki/Creative_limitation

For songwriting / production. This script should print
a bunch of ideas for a song. The goal would then to be
to create a track with the proscibed features.

'''

import random

#set up data

spice = ('key change', 'bonus bar', 'claps',
'drums + melody breakdown', 'Guitar! shout', 
'double time', 'syncopated hits')

feel = ('16th Hats', 'the gallops', 'slow burner',
'4 on the floor', 'synopated kick')

intro = ('don’t bore us, get to the chorus',
'dark and brooding','percussive','hits', 
'lo-fi fade in','lick')

tonality = ('major', 'minor', 'dorian', 'phrygian')

words = ('laser', 'force', 'glitch', 'wave', 
'cyber', 'thrust', 'machine', 'eagle', 'hawk', 'shark',
'bionic', 'eclipse', 'diamond', 'rain', 'chill', 
'fire', 'obey', 'hip', 'ray', 'electron', 'beast', 'escape',
'future', 'battle', 'tomb', 'lost', 'party', 'disco', 
'light', 'lawless', 'axe', 'streets', 'japan', 'speed',
'cocain', 'neon', 'OD', 'time', 'freeway', 'muscle', 'car',
'panther', 'epoch', 'midnight', 'euro', 'wilderness', 
'bleak', 'gem', 'quest', 'run', 'error', 'free')


# Helper functions

def rand_list(alist):
    #returns a random member of list
    x = random.choice(alist)
    return x

# make a song "report"

def song():
    i = rand_list(intro)
    f = rand_list(feel)
    t = rand_list(tonality)
    s = rand_list(spice)
    w = rand_list(words)
    w2 = rand_list(words)
    print('____________________')
    print('')
    print('Intro: \t %s' % i)
    print('Feel: \t %s' % f)
    print('Using a %s scale' % t)
    print('For added spice, through in a %s' % s)
    print('Your words of wisdom are: %s and %s' %(w, w2))
    print('Rock on. \m/')
    print('')
    print('____________________')

