#!/usr/bin/env python3

import sys

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
NOTES = len(NOTE_NAMES)

class Chord:
    def __init__(self, name, base, notes):
        self.name = name
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

def find(my_chord):
    print('search for',my_chord)
    for chord in chords:
        if len(my_chord-chord.notes) == 0:
            print(chord.name, chord.notes)


def main():
    global chords
    chords = []
    for i in range(len(NOTE_NAMES)):
        # https://www.pianochord.org/
        name = NOTE_NAMES[i]
        chords += [Chord(name + ' major',           i, [0,4,7])]
        chords += [Chord(name + ' minor',           i, [0,3,7])]
        chords += [Chord(name + ' dominant 7',      i, [0,4,7,10])]
        chords += [Chord(name + ' minor 7',         i, [0,3,7,10])]
        chords += [Chord(name + ' major 7',         i, [0,4,7,11])]
        chords += [Chord(name + ' minor major 7',   i, [0,3,7,11])]
        chords += [Chord(name + ' 6',               i, [0,4,7,9])]
        chords += [Chord(name + ' minor 6',         i, [0,3,7,9])]
        chords += [Chord(name + ' 6/9',             i, [0,4,7,9,2])]
        chords += [Chord(name + ' 5',               i, [0,7])]
        chords += [Chord(name + ' 9',               i, [0,4,7,10,2])]
        chords += [Chord(name + ' minor 9',         i, [0,3,7,10,2])]
        chords += [Chord(name + ' major 9',         i, [0,4,7,11,2])]
        chords += [Chord(name + ' 11',              i, [0,4,7,10,2,5])]
        chords += [Chord(name + ' minor 11',        i, [0,3,7,10,2,5])]
        chords += [Chord(name + ' 13',              i, [0,4,7,10,2,5,9])]
        chords += [Chord(name + ' minor 13',        i, [0,3,7,10,2,5,9])]
        chords += [Chord(name + ' add 9',           i, [0,4,7,2])]
        chords += [Chord(name + ' 7-5',             i, [0,4,6,10])]
        chords += [Chord(name + ' 7+5',             i, [0,4,8,10])]
        chords += [Chord(name + ' sus2',            i, [0,2,7])]
        chords += [Chord(name + ' sus4',            i, [0,5,7])]
        chords += [Chord(name + ' dim',             i, [0,3,6])]
        chords += [Chord(name + ' dim7',            i, [0,3,6,9])]
        chords += [Chord(name + ' m7(b5)',          i, [0,3,6,10])]
        chords += [Chord(name + ' aug',             i, [0,4,8])]
        chords += [Chord(name + ' aug7',            i, [0,4,8,10])]
    print('created list of',len(chords),'chords')
    find(set([3,7,9]))
    return 0

if __name__ == '__main__':
    sys.exit(main())


