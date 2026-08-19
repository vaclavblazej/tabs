# .tab Format Specification

This document describes the `.tab` plain-text format used in this repository.
Files are rendered by the [tabs-web](https://vaclavblazej.github.io/tabs-web/) preprocessor.

---

## Directory Structure

| Directory | Contents |
|---|---|
| `english/` | Complete songs in English |
| `czech-slovak/` | Complete songs in Czech or Slovak |
| `other/` | Complete songs in other languages |
| `incomplete/` | Work-in-progress songs |
| `melodies/` | Melody/solo-only arrangements (no full song) |

---

## File Naming

```
Artist - Song Title.tab
```

Artist name and song title come from the filename. They are not repeated inside the file.

---

## File Structure

A `.tab` file has three zones in order:

1. **Header block** — optional metadata
2. **Song body** — sections with chords and lyrics
3. **`[Fingerstyle]` block** — optional detailed tab notation

---

## Header Block

Key-value pairs, one per line, at the top of the file:

```
source: https://pisnicky-akordy.cz/...
video: https://www.youtube.com/watch?v=...
capo: 4
```

The header is followed by **two blank lines** before the song body begins.
The header is optional — some files start directly with a section.

### Known header keys

| Key | Purpose |
|---|---|
| `source` | URL of the original source this tab was based on |
| `video` | Reference or play-along video |
| `audio` | Reference audio |
| `live` | Live performance reference |
| `tutorial` | Video tutorial |
| `cover` | Cover version reference |
| `lyrics` | Lyrics reference (e.g. Genius) |
| `note` | Free-text annotation; prefix `!` signals urgency (e.g. `note: ! missing solo`) |
| `capo` | Capo fret number (e.g. `capo: 4`) |
| `tuning` | Tuning offset in semitones (e.g. `tuning: -1` = one semitone down) |
| `original` | Source of original tab if the file was later modified |
| `change` | Description of what was changed from the original |
| `author` | Composer credit |
| `inspiration` | Arrangement inspiration URL |

---

## Song Body

### Sections

Each section starts with a label in square brackets at column 0. Content is indented with 4 spaces.

```
[Verse 1]
    Am               G
    Here come the words
```

**Standard section names:**

- `[Intro]`, `[Outro]`, `[Ending]`
- `[Verse]`, `[Verse 1]`, `[Verse 2]`, …
- `[Chorus]`, `[Pre-Chorus]`, `[Bridge]`
- `[Solo]`, `[Guitar Solo]`, `[Instrumental]`, `[Interlude]`, `[Break]`

**Qualified names** — freeform words can be added to describe variants:

```
[loud Chorus]
[last Chorus]
[Verse calm]
[Guitar Solo]
[Verse 3 intense]
```

**Numbered sections** — use numbers when the same section type has different content:

```
[Verse 1]
[Verse 2]
[Chorus 1]
[Chorus 2]
```

**Repeat reference:**

```
[repeat Chorus]
[repeat Verse 1]
```

Means: play the named section again (no content follows — the label is the instruction).

---

## Chord Placement

### A. Chords above lyrics (standard)

Chord names sit on their own line, horizontally aligned above the syllable where the change occurs:

```
    Am               G             C
    Darkness creeping in from the side
```

### B. Chords on the section header line (compact)

When the chord pattern is simple and uniform throughout the section:

```
[Verse 1] Am G C F  [2x]
    First line of lyrics
    Second line of lyrics
```

### C. Chord-only section (no lyrics)

For instrumental passages, solos, or intros:

```
[Intro]  G D Am Am  G D C C  [2x]

[Solo]  Am F C G  [3x]
```

### Legacy: pipe markers (to be phased out)

Some older files embed `|` characters inside lyric lines to mark where chord changes fall, without naming the chords. This format is no longer used and should be converted.

---

## Chord Notation

### Root notes

Use English notation throughout: **A B C D E F G**.

> **Note on H:** Some files (especially Czech/Slovak) use `H` for B-natural following the German/Czech convention, and `B` for B-flat. This is legacy and should be converted to English notation (`B` = B-natural, `Bb` = B-flat).

### Modifiers

| Notation | Meaning |
|---|---|
| `Am`, `Em` | Minor |
| `A7`, `G7` | Dominant 7th |
| `Cmaj7`, `Fmaj7` | Major 7th |
| `Dsus2`, `Asus4` | Suspended |
| `Cadd9` | Added 9th |
| `Edim`, `Bdim7` | Diminished |
| `Eaug` | Augmented |
| `D6`, `Am7`, `Em9` | 6th, minor 7th, 9th |
| `Dm7b5` | Half-diminished |
| `G/B`, `D/F#`, `Am/C` | Slash chord (bass note after slash) |
| `F#m`, `C#m`, `Bb`, `Eb` | Sharp/flat roots |

### Unknown or uncertain chords

```
?           ← chord is unknown
F#m?        ← chord is present but may be wrong, needs verification
```

### Duration suffixes

These are appended directly to the chord name (no space) to indicate how long the chord lasts within the beat pattern. The baseline is one full beat.

| Suffix | Duration |
|---|---|
| (none) | Full beat |
| `.` (dot) | Half beat |
| `,` (comma) | 3/4 beat |
| `'` (apostrophe) | 1/4 beat or single strum |

> **INCOMPLETE:** The distinction between `'` as a strict 1/4 beat vs. a single strum (which may not map to a fixed subdivision) has not been fully settled. This may be differentiated in a future revision.

Suffixes can be combined and chained:

```
G.G'        ← half-beat G, then quarter-beat G
Am.C.       ← half-beat Am, half-beat C (two chords in one beat)
```

---

## Repeat Markers

`[Nx]` inline after a chord sequence or at the end of a section header line means "repeat this N times":

```
[Chorus] Am G C F  [4x]

[Solo]  E A D A  [2x]
```

`[: ... :]` around one or more lines marks a repeated passage:

> **INCOMPLETE:** This notation appears in a small number of files (e.g. Bastion - Build That Wall). Its exact semantics and whether it is officially supported has not been confirmed.

---

## Lyrics Conventions

- **2–3 spaces** within a lyric line mark a medium or large break in singing.
- **`-` inside a word** marks a prolonged or emphasized syllable: `sta-á-á-le`, `con-ta-in`.
- **A lone `-` line** (indented) represents a silent beat or measure before lyrics resume.
- **`[silence]`** marks an explicit silent measure.
- **`(text)`** inline = performance notes, background vocals, or spoken cues.

### The `+` prefix

A `+` at the start of a line marks content that does not fit the standard repeating pattern — it is something extra.

```
[repeat Chorus]
+   but this extra line only plays at the end
```

When used inside a section (not after a `[repeat ...]`), it marks a lyric or chord line that has additional content compared to the parallel line in other occurrences of the section.

> **INCOMPLETE:** The exact rules for when `+` appears mid-section vs. only after `[repeat ...]` need more examples and clarification.

---

## The `[Fingerstyle]` Section

Optional. Always placed at the bottom of the file. Contains standard ASCII guitar tablature.

```
[Fingerstyle]

[Intro]
   Am          G
e|------------|------------|
B|----1-------|----0-------|
G|---0--2-----|---0--0-----|
D|--2-----2---|--0-----0---|
A|-0----------|------------|
E|------------|-3----------|
```

**String order** (high to low): `e B G D A E`

Sub-sections within `[Fingerstyle]` mirror the song sections (`[Intro]`, `[Verse]`, `[Chorus]`, etc.); not every section needs to be present.

**`R|` strumming guide line:**

```
R|---v---v---^---v---|
```

`v` = downstroke, `^` = upstroke.

### `[Chords]` variant

When only chord voicings are needed (no full tab), a top-level `[Chords]` section lists chord shapes:

```
[Chords]
   Am    G     C     F
e|-0-|--3-|--0-|--1-|
B|-1-|--0-|--1-|--1-|
G|-2-|--0-|--0-|--2-|
D|-2-|--0-|--2-|--3-|
A|-0-|--2-|--3-|--3-|
E|---|--3-|----|--1-|
```

---

## ASCII Tab Technique Symbols

| Symbol | Technique |
|---|---|
| `h` | Hammer-on |
| `p` | Pull-off |
| `b` | Bend string up |
| `r` | Release bend |
| `/` | Slide up |
| `\` | Slide down |
| `v` or `~` | Vibrato |
| `t` or `T` | Right-hand tap |
| `s` | Legato slide |
| `S` | Shift slide |
| `*` | Natural harmonic |
| `[n]` | Artificial harmonic |
| `n(n)` | Tapped harmonic |
| `tr` | Trill |
| `TP` | Tremolo picking |
| `PM` or `_` | Palm muting |
| `\n/` | Tremolo arm dip (n = amount) |
| `=` | Hold bend / connector for hammers/pulls |
| `<>` | Volume swell |
| `x` | Muted note |
| `o` | Open/single note on rhythm slash |
| `(n)` | Optional or ghost note |

---

## Known Format Issues / Migration Notes

- **`H` notation:** Files in `czech-slovak/` and some in `english/` still use `H` for B-natural. These should be converted to `B` (and `B` → `Bb`).
- **Pipe `|` markers:** A small number of files (e.g. Radiohead - Creep, Jason Mraz - I'm Yours) use embedded `|` to mark chord positions without naming chords. These should be converted to standard chord-above-lyrics format.
- **Header key variations:** Some files use non-standard key names (`song video:`, `original chords:`, `source by:`). Standard keys are listed in the header table above.
- **`capo N` vs `capo: N`:** Both forms exist; the colon form (`capo: N`) is preferred for consistency.
