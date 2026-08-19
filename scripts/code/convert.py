#!/usr/bin/env python3

# Simple script that enables views over tabs and basic operations over guitar tabs.

#  import sys
import re
from copy import deepcopy
import traceback

class ConError(Exception):
    pass

class Input:
    def __init__(self):
        self.lines = []
        self.idx = 0
        try:
            while True:
                self.lines.append(input())
        except EOFError:
            pass

    def next_line(self):
        if self.idx == len(self.lines):
            raise ConError()
        res = self.lines[self.idx]
        self.idx += 1
        return res

    def get_all_input(self):
        return '\n'.join(self.lines)

inputstream = Input()


def is_empty_line(line):
    return len(line) == 0

def is_property_line(line):
    return line.__contains__(':')

def get_property_line(line):
    split = line.index(':')
    return (line[:split].strip(),line[split+1:].strip())

def starts_with_heading(line):
    return len(line) != 0 and line[0] == '['

def get_section_heading(line):
    begbr = line.index('[')
    endbr = line.index(']')
    name = line[begbr+1:endbr]
    return (name,line[endbr+1:].strip())

def is_chord_line(line):
    copy = line[:]
    orig_len = len(copy)
    copy = re.sub('[A-Gm0-9 ]', '', copy)
    new_len = len(copy)
    return new_len < orig_len/2

class Section:
    def __init__(self, name):
        self.name = name
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

class Chord:
    def __init__(self, symbols):
        self.main = ""
        state = 0
        for (i,c) in enumerate(symbols):
            if state == 0:
                # must start with the main chord name
                if c in ['C','D','E','F','G','A','B']:
                    state += 1
                    continue
                break # fail
            elif state == 1:
                # may contain sharp or flat
                if c in ['#','b']:
                    pass
                state += 1
            elif state == 2:
                # may contain minor
                if c in ['m']:
                    pass
                state += 1
            elif state == 3:
                # may contain additional modifiers
                if symbols[i:i+3] in ['maj','add','sus','dim','aug']:
                    pass
                state += 1
            elif state == 4:
                # may contain extra numbers
                if symbols[i:] in ['6','7','6/9','5','11','13']:
                    pass
                state += 1


class ChordLine:
    def __init__(self, line):
        pass

class Song:
    def __init__(self):
        self.properties = {}
        self.sections = []
        self.error = None
        self.name_to_section_idx = {}

    def add_property(self, key, value):
        self.properties[key] = value

    def add_section(self, name, optional_chords):
        # todo optional_chords
        self.name_to_section_idx[name] = len(self.sections)
        self.sections.append(Section(name))

    def repeat_section(self, name):
        if name in self.name_to_section_idx:
            self.sections.append(deepcopy(self.sections[self.name_to_section_idx[name]]))
            return True
        return False

    def add_line(self, line):
        self.sections[-1].add_line(line)

def is_link(line):
    return line[:4] == 'http'

def make_link(name, link):
    return f'<a href={link}>{name}</a>'

def make_property(name, value):
    return f'<span>{name}: {value}</span>'

def print_parse_error(song):
    html_string = []
    html_string.append('<html>')
    html_string.append(song.error)
    html_string.append('<pre>')
    html_string.append(inputstream.get_all_input())
    html_string.append('</pre>')
    html_string.append('</html>')
    return '\n'.join(html_string)

def song_to_html(song):
    if song.error:
        return print_parse_error(song)
    html_string = []
    html_string.append('<html>')
    html_string.append('<ul>')
    for (k,p) in song.properties.items():
        html_string.append('<li>')
        if is_link(p):
            html_string.append(make_link(k,p))
        else:
            html_string.append(make_property(k,p))
        html_string.append('</li>')
    html_string.append('</ul>')
    html_string.append('<pre>')
    for section in song.sections:
        html_string.append(f'[{section.name}]')
        for line in section.lines:
            html_string.append(f'{line}')
    html_string.append('</pre>')
    html_string.append('</html>')
    return '\n'.join(html_string)

def parse_song_from_tab():
    song = Song()
    try:
        line = inputstream.next_line()
        # process properties until newline
        while True:
            while is_empty_line(line):
                line = inputstream.next_line()
            if not is_property_line(line):
                break
            (key, value) = get_property_line(line)
            song.add_property(key, value)
            line = inputstream.next_line()
        # process song sections (verse, chorus, etc.)
        while True:
            while is_empty_line(line):
                line = inputstream.next_line()
            # process section name
            (name, optional_chords) = get_section_heading(line)
            repeat_key = 'repeat '
            if name[:len(repeat_key)] == repeat_key:
                name = name[len(repeat_key):]
                if song.repeat_section(name):
                    line = inputstream.next_line()
                    continue
            song.add_section(name, optional_chords)
            # process section text
            while True:
                line = inputstream.next_line()
                if starts_with_heading(line):
                    break
                if is_chord_line(line):
                    # todo preprocess chords
                    song.add_line(line)
                else:
                    song.add_line(line)
    except ConError:
        # remove extra newlines at the end
        if len(song.sections) != 0:
            while len(song.sections[-1].lines) != 0 and len(song.sections[-1].lines[-1]) == 0:
                song.sections[-1].lines.pop()
    except ValueError as e:
        song.error = f"could not parse correctly line {inputstream.idx}\n\n{traceback.format_exc()} {line}\n\n"
    return song

def main():
    song = parse_song_from_tab()
    print(song_to_html(song))
    if song.error is not None:
        exit(24)

if __name__ == '__main__':
    main()
    exit(0)
