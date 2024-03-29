This reposiroty contains raw [ASCII-tab](https://en.wikipedia.org/wiki/ASCII_tab).
There also is a repository with [preprocessed data (html for offline use)](https://github.com/vaclavblazej/tabs-web) and the processed [website with songs](https://vaclavblazej.github.io/tabs-web/).

*To report problems please open a [new issue](https://github.com/vaclavblazej/tabs/issues/new). I welcome pull requests with new songs (see requirement below).*

---

## New songs

To add a new song or propose changes [create a fork](https://github.com/vaclavblazej/tabs/fork), edit your version, and then create a pull request.

The required format is `.tab`.
It is a free-form format, however, the tabs should conform to the following rules for conssitency.

* start with properties in format: `<property>: <value>`
    * `source` stands for the original source of the tab (even if it was changed later)
    * `video` or `audio` serves as a reference (or play-along)
    * `note` is extra information
* properties are followed with two empty lines
* remainder consist of the song and `[Fingerstyle]` section
* song consists of parts, where every part is delimeted with `[<name>]` and its content is indented with 4 spaces
    * part content has chords and text
    * chords are either after the part name (if text is easy) or above the text
    * text should contain 2 or 3 spaces of there is a middle or big break in the singing
    * word in the text should contain `-` if it is important to emphesise/prolong the syllable after the symbol
    * `[3x]` and similar signify that something should be repeated
    * if something is unknown, then `?` may be used in place of chords
    * if something may be incorrect, then `<something>?` may be used to signify that it should be checked
* if part name contains `[repeat <name>]` then it refers to a part with `<name>` that was played already
* if part name repeats but has different contents, then they should be numbered, e.g., `[Verse 1]` and `[Verse 2]`.
* `[Fingerstyle]` section contains more precise instructions on how to play the song
    * parts of this section copy the parts in the song, but some may be missing

Song may be in the following states:

* Tabs are in the respective language directory of the repository (english songs in *english* directory)
* Incomplete tabs are in the *incomplete* directory
* Complete melodies / solos (without rest of the song) are in the *melodies* directory

## Symbols

Symbols for ASCII-tab from Wikipedia

```
Symbol 	Technique
h 	hammer on
p 	pull off
b 	bend string up
r 	release bend
/ 	slide up
\ 	slide down
v 	vibrato (sometimes written as ~)
t 	right hand tap
s 	legato slide
S 	shift slide
* 	natural harmonic
[n] 	artificial harmonic
n(n) 	tapped harmonic
tr 	trill
T 	tap
TP 	tremolo picking
PM 	palm muting (also written as _)
\n/ 	tremolo arm dip; n = amount to dip
\n 	tremolo arm down
n/ 	tremolo arm up
/n\ 	tremolo arm inverted dip
= 	hold bend; also acts as connecting device for hammers/pulls
<> 	volume swell (louder/softer)
x 	on rhythm slash represents muted slash
o 	on rhythm slash represents single note slash
·/. 	pick slide
```

## Guitar theory

* [Neck patterns](https://www.youtube.com/watch?v=uZg1p2GkUg0)
* [Chord names](https://www.pianochord.org/)

Given the main note of the major scale (1M) or of the minor scale (1m) the following pattern gives which chords are major, minor, or diminished.

```
A|-*m----*m-*M----*M---|
E|-1m----*d-1M---------|
```

C maj
```
  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
e|*--*-----5-----*-----*--1-----*-----*--4-----5-|
B|*--1-----*-----*--4-----5-----*-----*--1-----*-|
G|5-----*-----*--1-----*-----*--4-----5-----*----|
D|*-----*--4-----5-----*-----*--1-----*-----*--4-|
A|*-----*--1-----*-----*--4-----5-----*-----*--1-|
E|*--*-----5-----*-----*--1-----*-----*--4-----5-|
```

* maj - prima, tercie, kvinta
* min - tercie-1
* sus2 - tercie-2
* sus4 - tercie+1
* aug - kvinta+1
* dim - tercie-1, kvinta-1
* 7 - ++septima
* 7maj - ++septima+1
