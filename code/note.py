#!/usr/bin/env python3

import sys

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
NOTES = len(NOTE_NAMES)

def from_names_to_notes(names):
    res = []
    for name in names:
        res += [INVERSE_NOTES[name]]
    return res

class Chord:
    def __init__(self, name, base, score, notes):
        self.name = name
        self.score = score
        res = []
        for i in range(len(notes)):
            res += [notes[i] + base]
        self.notes = set(res)
        self.normalize()

    def normalize(self):
        notes = self.notes
        res = []
        for val in self.notes:
            if(val < 0 or val>=NOTES):
                val = ((val%NOTES)+NOTES)%NOTES
            res += [val]
        self.notes = set(res)

    def contains(self, other):
        return len(other-self.notes) == 0

    def strictly_contains(self, other):
        return self.contains(other) and len(self.notes-other) != 0

#   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
# e|*--*-----*-----*-----*--*-----*-----*--*-------|
# B|*--*-----*-----*--*-----*-----*-----*--*-----*-|
# G|*-----*-----*--*-----*-----*--*-----*-----*----|
# D|*-----*--*-----*-----*-----*--*-----*-----*--*-|
# A|*-----*--*-----*-----*--*-----*-----*-----*--*-|
# E|*--*-----*-----*-----*--*-----*-----*--*-------|
class Guitar:
    def __init__(self, base=None, sz=15):
        self.sz = sz
        if base==None:
            base = ['E','B','G','D','A','E']
        self.base = base

    def print_chord(self,set_chord):
        for i in range(self.sz):
            print("{:>3}".format(str(i)),end='')
        print()
        for b in self.base:
            print(b+'|',end='')
            for i in range(self.sz):
                if i!=0:
                    print('--',end='')
                base_note = from_names_to_notes([b])[0]
                # print(set_chord)
                if (base_note+i)%NOTES in set_chord:
                    c = '*'
                else:
                    c = '-'
                print(c,end='')
            print('-|')

def find(my_chord):
    print('search for',my_chord)
    tmp = []
    for chord in chords:
        if chord.contains(my_chord):
            tmp += [chord]
    contained = len(tmp)*[True]
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if i != j and tmp[i].strictly_contains(tmp[j].notes):
                contained[i]=False
    res = []
    for i in range(len(tmp)):
        if contained[i]:
            res += [tmp[i]]
    res.sort(key=(lambda i : i.score))
    return res

def main():
    global chords
    chords = []
    global INVERSE_NOTES
    INVERSE_NOTES = {}
    for i in range(NOTES):
        INVERSE_NOTES[NOTE_NAMES[i]]=i
    for i in range(len(NOTE_NAMES)):
        # https://www.pianochord.org/
        name = NOTE_NAMES[i]
        chords += [Chord(name + ' major pentatonic',   i, 3, [0,2,4,7,9])]
        chords += [Chord(name + ' egyptian suspended', i, 3, [0,2,5,7,10])]
        chords += [Chord(name + ' blues major',        i, 3, [0,3,5,8,10])]
        chords += [Chord(name + ' blues minor',        i, 3, [0,2,5,7,9])]
        chords += [Chord(name + ' minor pentatonic',   i, 3, [0,3,5,7,10])]

        chords += [Chord(name + ' scale',  i, 1, [0,2,4,5,7,9,11])]
        chords += [Chord(name + 'm scale', i, 2, [0,2,3,5,7,8,10])]
        chords += [Chord(name + '',        i, 1, [0,4,7])]
        chords += [Chord(name + 'm',       i, 2, [0,3,7])]
        chords += [Chord(name + '7',       i, 1, [0,4,7,10])]
        chords += [Chord(name + 'm7',      i, 2, [0,3,7,10])]
        chords += [Chord(name + ' maj7',   i, 3, [0,4,7,11])]
        chords += [Chord(name + 'm maj7',  i, 4, [0,3,7,11])]
        chords += [Chord(name + '6',       i, 3, [0,4,7,9])]
        chords += [Chord(name + 'm6',      i, 4, [0,3,7,9])]
        chords += [Chord(name + '6/9',     i, 3, [0,4,7,9,2])]
        chords += [Chord(name + '5',       i, 3, [0,7])]
        chords += [Chord(name + '9',       i, 3, [0,4,7,10,2])]
        chords += [Chord(name + 'm9',      i, 4, [0,3,7,10,2])]
        chords += [Chord(name + ' maj9',   i, 5, [0,4,7,11,2])]
        chords += [Chord(name + '11',      i, 5, [0,4,7,10,2,5])]
        chords += [Chord(name + 'm11',     i, 6, [0,3,7,10,2,5])]
        chords += [Chord(name + '13',      i, 7, [0,4,7,10,2,5,9])]
        chords += [Chord(name + 'm13',     i, 8, [0,3,7,10,2,5,9])]
        chords += [Chord(name + 'add9',    i, 5, [0,4,7,2])]
        chords += [Chord(name + '7-5',     i, 5, [0,4,6,10])]
        chords += [Chord(name + '7+5',     i, 6, [0,4,8,10])]
        chords += [Chord(name + 'sus2',    i, 3, [0,2,7])]
        chords += [Chord(name + 'sus4',    i, 3, [0,5,7])]
        chords += [Chord(name + 'dim',     i, 4, [0,3,6])]
        chords += [Chord(name + 'dim7',    i, 5, [0,3,6,9])]
        chords += [Chord(name + 'm7(b5)',  i, 5, [0,3,6,10])]
        chords += [Chord(name + 'aug',     i, 4, [0,4,8])]
        chords += [Chord(name + 'aug7',    i, 5, [0,4,8,10])]
    print('created list of',len(chords),'chords')
    set_chord = set(from_names_to_notes(['C','E','G','A',]))
    res = find(set_chord)
    for chord in res:
        print(chord.name, chord.notes)
    guitar = Guitar()
    guitar.print_chord(set_chord)
    return 0

if __name__ == '__main__':
    sys.exit(main())


