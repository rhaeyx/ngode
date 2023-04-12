from typing import Sequence
import re

class ChordedInstrument:
    """Represents a chorded instrument

    This class solely consists of class methods and is meant to be
    inherited by subclasses.
    """
    # HINT: Erase these errors and populate these class properties
    #       with the appropriate data:
    #
    # A_chroma - list of strings depicting the chroma scale starting at A
    #            with notes in between written with a sharp (#)
    # A_chroma_flat - same as A_chroma except that notes in between are
    #                 flats (b)
    # chord_maps - dict with key being the chord quality (e.g. m, M, 7)
    #              and value a list of integers depicting the integer
    #              notation for that chord
    A_chroma = ['A', 'A#', 'B','C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    A_chroma_flat = ['A', 'Bb', 'B','C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    chord_maps = {
        'M' : [0,4,7],
        'Maj' : [0,4,7],
        'm' : [0,3,7],
        'min' : [0,3,7],
        '7' : [0,4,7,10],
        'M7' : [0,4,7,11],
        'Maj7' : [0,4,7,11],
        'm7' : [0,3,7,10],
        'min7' : [0,3,7,10],
        'sus' : [0,5,7],
        'sus4' : [0,5,7],
        'sus2' : [0,2,7],
        'dim' : [0,3,6],
        'aug' : [0,4,8],
        '+' : [0,4,8]
    }

    @classmethod
    def split_chord(cls, chord: str) -> tuple[str, str, str]:
        """Split a chord into its components

        A chord consists of three parts - base/root note, accidental(s),
        and chord type. The base/root note is the base label denoting
        which note in the scale the chord most closely sounds like.
        The accidentals (sharps # and flats b) are labels on the
        base/root note. The chord type is the quality of the chord,
        and directly corresponds to which notes in the chromatic
        scale with the base/root note to play/include together.

        The method returns a tuple of the base/root note, accidental(s),
        and chord type, respectively. If the base/root note has
        no accidentals, then that element of the tuple is an empty string.
        Invalid chords entered raises a ``ValueError``.

        :param chord: the chord to split
        :type chord: `str`

        :return: the split chord in terms of its
            root note, accidental, and chord type, respectively
        :rtyp: tuple[str, str, str]

        :raise: ValueError when an empty string is provided,
            the chord is of an invalid format,
            or the chord is not supported by the program

        :classmethod:
        """
        chord = chord.strip()
        
        if (chord == ""):
            raise ValueError("Chord is an empty string.")

        base_note = chord[0]
        
        valid_base_notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        
        if (base_note not in valid_base_notes):
            raise ValueError("Base note is invalid.")
        
        chord = chord.replace(base_note, "")

        # sharp by default as accidental
        accidental = ""
        if ("b" in chord):
            accidental = "b"    # flat

        if ("#" in chord):
            accidental = "#"    # sharp
        
        chord = chord.replace(accidental, "")

        chord_abbr = ["M", "Maj", "m", "min", "7", "M7", "Maj7", "m7", "min7",  
        "sus", "sus4", "sus2", "dim", "aug", "+"]

        chord_type = ""
        for abbr in chord_abbr:
            if (abbr in chord):
                chord_type = abbr
                
        chord = chord.replace(chord_type, "")
        
        if (chord != ""):
            raise ValueError("Invalid chord.")
        
        return (base_note, accidental, chord_type)
        
    @classmethod
    def supported_chords(cls) -> list[str]:
        """Get a list of supported chords

        The list of supported chords returned by this method
        is a list of chord abbreviations.

        :return: a list of supported chord type abbreviations
        :rtyp: list[str]

        :classmethod:
        """
        return ("", "M", "Maj", "m", "min", "7", "M7", "Maj7", "m7", "min7", 
        "sus4", "sus", "sus2", "dim", "aug", "+") 

    @classmethod
    def transpose_chord(cls, chord: str, semitones: int) -> str:
        """Transpose a chord to some amount of semitones

        "Transposing" a chord means finding the ``semitones``
        amount of half-steps to the left or right of the root note
        of the chord. For example, a Am7 chord transposed +2 semitones
        becomes a Bm7 chord while the same transposed -2 semitones becomes
        a Gm7 chord.

        If the root note has a flat in it, the transposed root note will
        have a flat if any. Otherwise, the transposed note will have a
        sharp instead.

        :param chord: the chord to transpose
        :type chord: `str`
        :param semitones: the number of semitones to which the cord is to be transposed
        :type semitones: int

        :return: the newly-transposed chord
        :rtyp: str

        :classmethod:
        """
        
        base_note, accidental, chord_type = cls.split_chord(chord)
        chroma_scale = cls.gen_chroma_scale(base_note + accidental)
                
        return chroma_scale[semitones % len(chroma_scale)] + chord_type

    @classmethod
    def gen_chroma_scale(cls, base_note: str='A') -> list[str]:
        """Generate the chromatic scale from the specified ``base_note``

        The chromatic scale consists of twelve notes ordered in ascending
        pitch or frequency. In English, they are designated with the
        letters A-G with some letters in between affixed by a sharp (#)
        or a flat (b).
        
        The starting note can be changed to produce different variations
        of the scale. For example, if the base note is F, then the scale
        will be listed as such:

            F F# G G# A A# B C C# D D# E

        By default, this method will use sharps to denote the notes in the
        middle of the "normal" notes. If the base note is written with a
        flat, like ``Ab``, then the chromatic scale will be generated using
        flats instead. For example, if the base note is F, then the scale
        using flats will be listed as such:

            F Gb G Ab A Bb B C Db D Eb E

        If the base note is of the invalid format, this method returns an
        empty list.

        :param base_note: the first note in the scale
        :type base_note: str

        :return: the chromatic scale starting from ``base_note``. The length
            of the list should be twelve
        :rtyp: list[str]

        :classmethod:
        """                        
        # validate input
        # check base note length
        if (len(base_note) > 2):
            return []
        
        if not ((base_note in cls.A_chroma) or (base_note in cls.A_chroma_flat)):
            return []
        
        scale = cls.A_chroma
        if base_note not in cls.A_chroma:
            scale = cls.A_chroma_flat

        index = scale.index(base_note)
        chroma_scale = scale[index:] + scale[:index]
        return chroma_scale

    @classmethod
    def get_notes_from_intervals(cls, base_note: str, intervals: Sequence[int]) -> tuple[str]:
        """Get the corresponding notes given an integer notation and the base note

        This method is used to retrieve the notes that make up a chord. Chords
        can be represented in `integer notation <https://integermusic.blogspot.com/2014/11/chords.html>`_, which
        denotes which notes in the chromatic scale in relation to a base/root note
        is part of the chord. For example, with a base note B:

        * {0} represents the note set {B}
        * {0, 4, 7} represents the note set {B, D#, F#} - a B major chord

        :param base_note: the first note in the chromatic scale
        :type base_note: str
        :param intervals: the notes to retrieve in integer notation
        :type intervals: Sequence[int]

        :return: a tuple of notes corresponding to the integer notation ``intervals``.
            The length of the tuple should be equal to the length of ``intervals``.
        :rtyp: tuple[str]

        :classmethod:
        """
        base_note, accidental, chord_type = cls.split_chord(base_note)
        chroma_scale = cls.gen_chroma_scale(base_note + accidental)
        
        notes = []
        for interval in intervals:
            notes.append(chroma_scale[interval % len(chroma_scale)])
        
        return tuple(notes)        

    @classmethod
    def get_chord_notes(cls, chord: str) -> tuple[str]:
        """Get the notes corresponding to a chord

        The method accepts ``chord``s in abbreviation notation only
        Valid chords include (but not limited to): ``A``, ``Amaj7``,
        ``Cdim``.

        :param chord: the chord whose component notes we want to retrieve
        :type chord: str

        :return: the notes of the chord in ascending order in relation
            to the chromatic scale. The first element should be the
            base/root note of the chord.
        :rtyp: tuple[str]

        :classmethod:
        """
        base_note, accidental, chord_type = cls.split_chord(chord)
        chroma_scale = cls.gen_chroma_scale(base_note + accidental)
        
        if (chord_type == ""):
            chord_type = "M"
                    
        notes = []
        for note in cls.chord_maps[chord_type]:
            notes.append(chroma_scale[note])
            
        return tuple(notes)

class Ukulele(ChordedInstrument):
    """Represents a ukulele

    An ukulele is a :py:class:`ChordedInstrument` where we can extract
    the fingerings of a specific chord. We are also able to play a sound
    using this class.
    """
    def __init__(self, tuning: Sequence[str]=['G', 'C', 'E', 'A'], octaves: Sequence[int]=[4, 4, 4, 4], num_frets: int=20):
        """Instantiate an object of this class

        This method will instantiate a new :py:class:`Ukulele`
        object with the given ``tuning``, corresponding ``octaves``,
        and ``num_frets``. The number of elements in ``tuning`` and
        ``octaves`` should be the same.

        Objects of this class have only the following properties:
        * tuning
        * octaves
        * num_frets

        :param tuning: tuning of strings the ukulele. The standard tuning
            of an ukulele from left to right is [G4, C4, E4, A4]
        :type tuning: list[str] or tuple[str]
        :param octaves: corresponding octaves of the tuning
        :type octaves: list[int] or tuple[int]
        :param num_frets: number of frets in the ukulele
        :type num_frets: int
        """
        self.tuning = tuning
        self.octaves = octaves
        self.num_frets = num_frets    
    

    def gen_fret_notes(self) -> dict[str, list[str]]:
        """Generate a chromatic scale for each string in the :py:class:`Ukulele`

        This method generates the chromatic scale using :py:attr:num_frets notes
        for each base/root note in :py:attr:tuning of the ukulele.

        :return: a dictionary containing the chromatic scale for each note
            in each string of the ukulele. The number of elements in each
            value of the dictionary should be equal to the number of frets
        :rtyp: dict[str, list[str]]
        """
        fret_notes = {}
        for note in self.tuning:
            chroma_scale = self.gen_chroma_scale(note)
            while (len(chroma_scale) < self.num_frets):
                chroma_scale += chroma_scale
                
            fret_notes[note] = chroma_scale[:self.num_frets]
        return fret_notes

    def get_note_idxs_on_fret(self, notes: list[str]) -> dict[str, list[int]]:
        """Get the strings and frets where certain notes are located

        This method determines, for each string in the ukulele, the location
        of each fret in each string. When pressed and strummed individually, it
        will produce a sound from one of the notes in the ``notes`` parameter.

        For example::

            fret_map = uke.get_note_idxs_on_fret(['C', 'E', 'G'])
            fret_map['C'] # Contains [0, 4, 7, 12, ...]
            fret_map['G'] # Contains [0, 5, 9, 12, ...]

        Note that the size of the list corresponding to each string will be different,
        but the numbers are always less than :py:attr:num_frets.

        :param notes: the notes we want to find on the fretboard
        :type notes: list[str]

        :return: a dictionary with its keys being the elements of :py:attr:tuning
            corresponding to the "default"/"open" tone of the string.
            Its values correspond to which frets a note in ``notes`` are located.
        :rtyp: dict[str, list[int]]
        """
        fret_notes = self.gen_fret_notes()
        idxs_on_fret = {}
        for key, scale in fret_notes.items():
            idxs = []
            for i, note in enumerate(scale):
                if note in notes:
                    idxs.append(i)
            idxs_on_fret[key] = idxs
        return idxs_on_fret

    def get_chord_fingerings(self, chord_name: str) -> list[list[int]]:
        """Get the possible chord fingerings for a chord

        This method will find all possible chord fingerings for a chord.
        It is a list where each element is a list of the same length as
        :py:attr:`~.tuning` with each nth element in the list corresponding
        to the fret to press in the nth string in :py:attr:`~.tuning`. If
        an element is zero, it means that the string is open (i.e. not
        pressed).

        The fingerings have the following properties:

        * All strings are strummed, i.e. each string has a finger
        * Each finger in a chord should be +- 3 of the average fret
          position of all of the fingers in it.
        * The largest spacing between any two fingers is at most four
          frets.
        * Open strings are not counted when computing for the average
          fret position or spacing between any two fingers.
        * The maximum position of the closest finger from the fret nut
          is the seventh fret.

        The ``chord_name`` supplied should be a valid one according to
        :py:meth:`split_chord`.

        :param chord_name: the name of the chord to process
        :type chord_name: str

        :return: a list of the possible fingerings for the chord
        :rtyp: list[list[int]]
        """
        
        chords = {
            "A" : {
                "M" : [[2, 1, 0, 0], [2, 1, 0, 4], [2, 4, 0, 4], [6, 4, 0, 0], 
                [2, 4, 5, 4], [6, 9, 0, 0], [6, 4, 5, 0], [6, 4, 5, 4], 
                [6, 9, 0, 7], [6, 4, 5, 7], [9, 11, 0, 0], [6, 9, 5, 7], 
                [9, 9, 9, 0], [6, 9, 9, 7], [9, 9, 9, 7]],
                "m" : [[2, 0, 0, 0], [2, 0, 0, 3], [5, 0, 0, 0], [2, 4, 0, 3],
                [5, 4, 0, 0], [9, 0, 0, 0], [2, 4, 5, 3], [5, 9, 0, 0],
                [5, 9, 0, 0], [5, 4,5, 0], [9, 0, 5, 0], [5, 4, 5, 3],
                [5, 4, 8, 0], [5, 0, 5, 7], [9, 0, 8, 0], [5, 9, 5, 7],
                [5, 4, 5, 7], [9, 0, 5, 7], [5, 9, 5, 7], [9, 9, 8, 0],
                [5, 9, 8, 7], [9, 9, 8, 7]],
                "7" : [[0, 1, 0, 0], [0, 1, 3, 0], [0, 1, 0, 4], [2, 1, 3, 0],
                [0, 1, 5, 0], [0, 4, 0, 4], [2, 1, 3, 4], [0, 1, 5, 4], 
                [0, 4, 3, 4], [0, 7, 0, 4], [2, 4, 3, 4], [6, 4, 3, 0],
                [6, 7, 0, 0], [0, 4, 5, 4], [6, 7, 3, 0], [0, 7, 5, 4],
                [0, 7, 9, 0], [6, 4, 3, 4], [6, 7, 0, 4], [6, 7, 5, 0],
                [0, 9, 9, 0], [6, 4, 3, 7], [6, 7, 0, 7], [6, 7, 5, 4],
                [6, 7, 9, 0], [6, 7, 0, 10], [6, 7, 3, 7], [0, 7, 9, 7],
                [6, 9, 0, 10], [6, 7, 5, 7], [9, 7, 9, 0], [0, 9, 9, 7],
                [0, 9, 9, 10], [6, 7, 9, 7], [9, 7, 9, 7], [6, 9, 9, 10],
                [9, 7, 9, 10], [9, 9, 9, 10]],
                "M7" : [[1, 1, 0, 0], [1, 1, 4, 0], [1, 1, 0, 4], [2, 1, 4, 0],
                [1, 1, 5, 0], [1, 4, 0, 4], [2, 1, 4, 4], [1, 1, 5, 4], 
                [1, 4, 4, 4], [2, 4, 4, 4], [6, 4, 4, 0], [6, 8, 0, 0], 
                [1, 4, 5, 4], [6, 8, 4, 0], [6, 4, 4, 4], [6, 8, 0, 4], 
                [6, 8, 5, 0], [6, 4, 4, 7], [6, 8, 0, 7], [6, 8, 5, 4],
                [6, 8, 9, 0], [6, 8, 4, 7], [6, 8, 5, 7], [9, 8, 9, 0], 
                [6, 8, 9, 7], [9, 8, 9, 7], [9, 8, 9, 11], [9, 9, 9, 11]],
                "m7" : [[0, 0, 3, 0], [0, 0, 0, 0], [0, 0, 0, 3], [2, 0, 3, 0], 
                [0, 0, 5, 0], [0, 0, 0, 7], [0, 4, 0, 3], [2, 0, 3, 3], 
                [5, 0, 3, 0], [0, 0, 5, 3], [0, 0, 8, 0], [0, 0, 0, 10], 
                [0, 0, 3, 7], [0, 4, 3, 3], [0, 7, 0, 3], [2, 4, 3, 3], 
                [5, 4, 3, 0], [5, 7, 0, 0], [0, 0, 5, 7], [0, 4, 5, 3], 
                [0, 4, 8, 0], [5, 7, 3, 0], [0, 7, 5, 3], [0, 7, 8, 0], 
                [5, 4, 3, 3], [5, 7, 0, 3], [5, 0, 3, 7], [0, 0, 8, 7], 
                [5, 7, 5, 0], [0, 9, 8, 0], [5, 4, 3, 7], [5, 7, 0, 7], 
                [9, 0, 0, 10], [0, 4, 8, 7], [5, 7, 5, 3], [5, 7, 8, 0], 
                [5, 7, 3, 7], [0, 7, 8, 7], [5, 7, 5, 7], [9, 7, 8, 0], 
                [0, 9, 8, 7], [0, 9, 8, 10], [5, 7, 8, 7], [9, 0, 8, 10], 
                [9, 7, 8, 7], [9, 7, 8, 10], [9, 9, 8, 10]], 
                "sus4" : [[2, 2, 0, 0], [2, 2, 0, 5], [2, 4, 0, 5], 
                [7, 4, 0, 0], [2, 4, 5, 5], [7, 9, 0, 0], [7, 4, 5, 0], 
                [7, 9, 0, 5], [7, 4, 5, 5], [7, 9, 5, 7], [7, 4, 5, 7], 
                [9, 9, 0, 5], [7, 9, 5, 7], [9, 9, 10, 0], [9, 9, 5, 5], 
                [7, 9, 10, 7], [9, 9, 10, 7]], 
                "sus2" : [[2, 4, 0, 2], [4, 4, 0, 0], [2, 4, 5, 2], 
                [4, 4, 5, 0], [4, 4, 5, 2], [4, 4, 7, 0], [4, 4, 5, 7], 
                [9, 11, 0, 0,], [9, 9, 7, 0], [9, 11, 7, 0], [9, 9, 7, 7]], 
                "dim" : [[2, 0, 5, 6], [2, 3, 5, 3], [5, 3, 5, 0], 
                [8, 0, 5, 0], [5, 3, 5, 3], [5, 0, 5, 6], [8, 0, 8, 0], 
                [5, 3, 5, 6], [8, 0, 5, 6], [8, 0, 11, 0], [5, 9, 5, 6], 
                [8, 9, 8, 0], [5, 9, 8, 6], [8, 9, 8, 6]], 
                "aug" : [[2, 1, 1, 0], [2, 1, 1, 4], [2, 5, 1, 4], 
                [2, 5, 5, 4], [6, 5, 5, 0], [6, 5, 5, 4], [6, 5, 9, 0], 
                [6, 5, 5, 8], [6, 9, 5, 8], [10, 9, 9, 0], [6, 9, 9, 8], 
                [10, 9, 9, 8]]
            },
            "A#" : {
                "M" : [[3, 2, 1, 1], [3, 2, 1, 5], [3, 5, 1, 5], [3, 5, 6, 5], 
                [7, 5, 6, 5], [7, 5, 6, 8], [7, 10, 6, 8], [7, 10, 10, 8], 
                [10, 10, 10, 8]],
                "m" : [[3, 1, 1, 1], [3, 1, 1, 4], [3, 5, 1, 4], [3, 5, 6, 4], 
                [6, 5, 6, 4], [6, 5, 6, 8], [6, 10, 6, 8], [6, 10, 9, 8], 
                [10, 10, 9, 8]],
                "7" : [[1, 2, 1, 1], [1, 2, 4, 1], [1, 2, 1, 5], [3, 2, 4, 1], 
                [1, 5, 1, 5], [3, 2, 4, 5], [1, 5, 4, 5], [3, 5, 4, 5], [7, 5, 4, 5], 
                [7, 5, 4, 8], [7, 8, 6, 5], [7, 8, 4, 8], [7, 8, 6, 8], [7, 8, 10, 8], 
                [10, 8, 10, 8], [7, 10, 10, 11], [10, 8, 10, 11], [10, 10, 10, 11]],
                "M7" : [[2, 2, 1, 0], [3, 2, 1, 0], [2, 2, 1, 1], [3, 2, 5, 0], 
                [2, 2, 6, 0], [2, 2, 5, 1], [2, 2, 1, 5], [3, 2, 5, 1], 
                [3, 2, 6, 0], [2, 5, 1, 5], [3, 2, 5, 5], [2, 2, 6, 5], [7, 5, 5, 0], 
                [2, 5, 5, 5], [3, 5, 5, 5], [7, 5, 6, 0], [2, 5, 6, 5], [7, 9, 6, 0], 
                [7, 5, 5, 5], [7, 10, 6, 0], [7, 5, 5, 8], [7, 10, 10, 0], 
                [7, 9, 6, 5], [7, 9, 5, 8], [10, 9, 10, 0], [7, 9, 6, 8], [10, 10, 10, 0], 
                [7, 9, 10, 8], [10, 9, 10, 8]],
                "m7" : [[1, 1, 1, 1], [1, 1, 4, 1], [1, 1, 1, 4], [3, 1, 4, 1], 
                [1, 5, 1, 4], [3, 1, 4, 4], [1, 5, 4, 4], [3, 5, 4, 4], [6, 5, 4, 4], 
                [6, 5, 4, 8], [6, 8, 6, 4], [6, 8, 4, 8], [6, 8, 6, 8], [6, 8, 9, 8], 
                [10, 8, 9, 8], [10, 8, 9, 11], [10, 10, 9, 11]],
                "sus4" : [[3, 3, 1, 1], [3, 5, 6, 6], [8, 5, 6, 6], [8, 5, 6, 8], 
                [8, 10, 6, 8], [10, 10, 6, 6], [8, 10, 11, 8], [10, 10, 11, 8]],
                "sus2" : [[3, 0, 1, 1], [3, 0, 1, 3], [5, 2, 1, 1], [3, 5, 1, 3], 
                [5, 5, 1, 1], [3, 5, 6, 3], [5, 5, 6, 3], [5, 0, 6, 8], [5, 5, 6, 8], 
                [10, 0, 6, 8], [10, 10, 8, 8]],
                "dim" : [[3, 1, 0, 1], [3, 1, 0, 4], [3, 4, 0, 4], [3, 4, 6, 4], 
                [6, 4, 6, 4], [6, 10, 0, 7], [6, 4, 6, 7], [6, 10, 6, 7], [6, 10, 9, 7], 
                [9, 10, 9, 7]],
                "aug" : [[3, 2, 2, 1], [3, 2, 2, 5], [3, 6, 2, 5], [3, 6, 6, 5], [7, 6, 6, 5], 
                [7, 6, 6, 9], [7, 6, 9, 10], [7, 10, 10, 9], [11, 10, 10, 9]]
            },
            "B" : {
                "M" : [[4, 3, 2, 2],[4, 3, 2, 6],[4, 6, 2, 6],[4, 6, 7, 6],[8, 6, 7, 6],
                [8, 6, 7, 9],[8, 11, 7, 9],[8, 11, 11, 9],[11, 11, 11, 9]],
                "m" : [[4, 2, 2, 2],[4, 2, 2, 5],[4, 6, 2, 5],[4, 6, 7, 5],
                [7, 6, 7, 5],[7, 6, 7, 9],[7, 11, 7, 9],[7, 11, 10, 9],
                [11, 11, 10, 9]],
                "7" : [[2, 3, 2, 0],[4, 3, 2, 0],[2, 3, 2, 2], [4, 3, 5, 0],
                [2, 3, 5, 2],[2, 3, 2, 6],[4, 3, 5, 2],[4, 3, 7, 0],[2, 6, 2, 6],
                [4, 3, 5, 6],[8, 6, 5, 0],[2, 6, 5, 6],[4, 6, 5, 6],[8, 6, 7, 0],
                [8, 9, 7, 0],[8, 6, 5, 6],[8, 11, 7, 0],[8, 6, 5, 9],[8, 11, 11, 0],
                [8, 9, 7, 6],[8, 9, 5, 9],[11, 9, 11, 0],[8, 9, 7, 9],[11, 11, 11, 0],
                [8, 9, 11, 9],[11, 9, 11, 9]],
                "M7" : [[3, 3, 2, 1],[4, 3, 2, 1],[3, 3, 2, 2],[3, 3, 6, 2],[3, 3, 2, 6],
                [4, 3, 6, 2],[3, 6, 2, 6],[4, 3, 6, 6],[3, 3, 7, 6],[3, 6, 6, 6],
                [4, 6, 6, 6],[3, 6, 7,6],[8, 6, 6, 6],[8, 6, 6, 9],[8, 10, 7, 6],
                [8, 10, 6, 9],[8, 10, 7, 9],[8, 10, 11, 9],[11, 10, 11, 9]],
                "m7" : [[2, 2, 2, 0],[4, 2, 2, 0],[2, 2, 2, 2],[4, 2, 5, 0],
                [2, 2, 5, 2],[2, 2, 2, 5],[4, 2, 5, 2],[2, 6, 2, 5],[4, 2, 5, 5],
                [7, 6, 5, 0],[2, 6, 5, 5],[4, 6, 5, 5],[7, 6, 7, 0],[7, 9, 7, 0],
                [7, 6, 5, 5],[7, 6, 10, 0],[7, 11, 7, 0],[7, 6, 5, 9],[7, 11, 10, 0],
                [7, 9, 7, 5],[7, 9, 5, 9],[11, 9, 10, 0],[7, 9, 7, 9],[11, 11, 10, 0],
                [7, 9, 10, 9],[11, 9, 10, 9]],
                "sus4" : [[4, 4, 2, 2],[4, 6, 0, 2],[4, 6, 0, 7],[4, 6, 7, 7],
                [9, 11, 0, 9],[9, 6, 7, 7],[11, 11, 0, 7],[9, 6, 7, 9],[11, 11, 0, 9],
                [9, 11, 7, 9],[11, 11, 7, 7]],
                "sus2" : [[4, 1, 2, 2],[4, 1, 2, 4],[4, 6, 2, 4],[6, 6, 2, 2],
                [4, 6, 7, 4],[6, 6, 7, 4],[6, 6, 7, 9],[11, 11, 9, 9]],
                "dim" : [[4, 2, 1, 2],[4, 2, 1, 5],[4, 5, 1, 5],[4, 5, 7, 5],
                [7, 5, 7, 5],[7, 5, 7, 8],[7, 11, 7, 8],[7, 11, 10, 8],[10, 11, 10, 8]],
                "aug" : [[0, 3, 3, 2],[4, 3, 3, 2],[4, 3, 3, 6],[0, 3, 7, 6],
                [4, 3, 7, 6],[0, 7, 7, 6],[4, 7, 7, 6],[8, 7, 7, 6],[8, 7, 7, 10],
                [0, 11, 11, 10],[8, 7, 11, 10],[8, 11, 11, 10]]
            },
            "C" : {
                "M" : [[0, 0, 0, 3],[0, 0, 0, 7],[0, 4, 0, 3],[0, 0, 0, 10],
                [0, 0, 3, 7],[0, 4, 3, 3],[0, 7, 0, 3],[5, 4, 3, 3],[5, 7, 0, 3],
                [5, 0, 3, 7],[0, 0, 8, 7],[5, 4, 3, 7],[5, 7, 0, 7],[9, 0, 0, 10],
                [0, 4, 8, 7],[5, 7, 3, 7],[0, 7, 8, 7],[5, 7, 8, 7],[9, 0, 8, 10],
                [9, 7, 8, 7],[9, 7, 8, 10]],
                "m" : [[0, 0, 3, 6],[0, 3, 3, 3],[3, 3, 3, 5],[5, 0, 3, 6],
                [0, 0, 8, 6], [5, 3, 3, 6],[5, 7, 3, 6],[0, 0, 11, 10],[0, 7, 8, 6],
                [5, 7, 8, 6],[8, 0, 8, 10],[8, 0, 11, 10],[8, 7, 8, 6],[8, 7, 8, 10]],
                "7" : [[0, 0, 0, 1],[3, 0, 0, 1],[0, 4, 0, 1],[5, 0, 0, 1],
                [3, 0, 0, 3],[0, 4, 3, 1],[5, 4, 0,1],[3, 0, 0, 7],[3, 4, 0, 3],
                [3, 4, 3, 0],[5, 4, 3, 1],[0, 0, 6, 7],[0, 4, 6, 3],[3, 0, 3, 7],
                [3, 4, 3, 3],[3, 7, 0,3],[3, 0, 6, 7],[3, 4, 6, 3],[0, 4, 6, 7],
                [0, 10, 0, 7],[3, 4, 3, 7],[3, 7, 0, 7],[5, 4, 6, 3],[5, 0, 6, 7],
                [0, 10, 0, 10],[0, 7, 6, 7],[3, 7, 3, 7],[5, 4, 6, 7],[9, 0, 6, 7],
                [0, 10, 6, 7],[3, 7, 6, 7],[5, 6, 7, 7],[9, 0, 6, 10]],
                "M7" : [[0, 0, 0, 2],[4, 0, 0, 2],[0, 4, 0, 2],[5, 0, 0, 2],
                [4, 0, 0, 3],[0, 4, 3, 2],[5, 4, 0, 2],[4, 0, 0, 7],[4, 4, 0, 3],
                [4, 4, 3, 2],[5, 4, 3, 2],[0, 0, 7, 7], [0, 4, 7, 3],[4, 0, 3, 7],
                [4, 4, 3, 3],[4, 7, 0, 3],[4, 0, 7, 7],[4, 4, 7, 3],[0, 4, 7, 7],
                [0, 11, 0, 7],[4, 4, 3, 7],[4, 7, 0, 7],[5, 4, 3, 7],[5, 0, 7, 7],
                [4, 0, 8, 7],[0, 11, 0, 10],[0, 7, 7, 7],[4, 7, 3, 7],[5, 4, 7, 7],
                [9, 0, 7, 7],[4, 4, 8, 7],[0, 11, 7, 7],[4, 7, 7, 7],[5, 7, 7, 7],
                [9, 0, 7, 10],[0, 11, 8, 7],[4, 7, 8, 7],[9, 7, 7, 7],[9, 11, 0, 10]],
                "m7" : [[0, 3, 3, 1],[3, 3, 3, 1],[5, 3, 3, 1],[0, 0, 6, 6],[0, 3, 6, 3],
                [3, 0, 3, 6],[3, 3, 3, 3],[3, 0, 6, 6],[3, 3, 6, 3],[0, 3, 6, 6],[3, 3, 3, 6],
                [5, 3, 6, 3],[5, 0, 6, 6],[0, 7, 6, 6],[3, 7, 3, 6],[5, 3, 6, 6],[8, 0, 6, 6],
                [0, 10, 6, 6],[3, 7, 6, 6],[5, 7, 6, 6],[8, 0, 6, 10],[0, 10, 8, 6],
                [8, 7, 6, 6],[8, 7, 6, 10],[0, 10, 11, 10],[8, 10, 8, 6],[8, 10, 6, 10],
                [8, 10, 8, 10],[8, 10, 11, 10]],
                "sus4" : [[0, 0, 1, 3],[0, 5, 1, 3],[0, 5, 3, 3],[5, 5, 3, 3],
                [0, 0, 8, 8],[0, 5, 8, 8],[0, 7, 8, 8],[5, 7, 8, 8,],[10, 0, 8, 10],
                [10, 7, 8, 8],[10, 7, 8, 10]],
                "sus2" : [[0, 0, 3, 5],[0, 2, 3, 3],[5, 2, 3, 3],[5, 0, 3, 5],[7, 0, 3, 3],
                [0, 0, 8, 5],[5, 2, 3, 5],[7, 0, 3, 5],[5, 7, 3, 5],[7, 7, 3, 3],[0, 0, 10, 10],
                [0, 7, 8, 5],[5, 7, 8, 5],[7, 8, 0, 10],[7, 0, 10, 10],[7, 7, 8, 5],
                [7, 7, 8, 10]],
                "dim" : [[5, 3, 2, 3],[5, 0, 2, 6],[5, 3, 2, 6],[5, 6, 2, 5],
                [5, 6, 8, 6],[8, 0, 8, 9],[8, 0, 11, 9],[8, 6, 8, 6],[8, 6, 8, 9],
                [11, 0, 11, 9]],
                "aug" : [[1, 0, 0, 3],[1, 4, 0, 3],[1, 4, 4, 3],[5, 4, 4, 3],
                [5, 0, 4, 7],[5, 4, 4, 7],[5, 8, 0, 7],[9, 0, 0, 11],[5, 8, 4, 7],
                [5, 8, 8, 7],[9, 0, 8, 11],[9, 8, 8, 7],[9, 8, 8, 11]]
            },
            "C#" : {
                "M" : [[1, 1, 1, 4],[1, 5, 1, 4],[1, 5, 4, 4],[6, 5, 4, 4],
                [6, 5, 4, 8],[6, 8, 4, 7],[6, 8, 9, 8],[10, 8, 9, 8],
                [10, 8, 9, 11]],
                "m" : [[1, 1, 0, 4],[1, 4, 0, 4],[1, 4, 4, 4],[6, 4, 4, 4],
                [6, 8, 0, 4],[6, 4, 4, 7],[6, 8, 0, 7],[4, 6, 8, 7],
                [6, 8, 9, 7],[9, 8, 9, 7],[9, 8, 9, 11]],
                "7" : [[1, 1, 1, 2],[4, 1, 1, 2],[1, 5, 1, 2],[4, 1, 1, 4],
                [1, 5, 4, 2],[4, 5, 4, 1],[4, 5, 4, 2],[6, 5, 4, 2],[4, 5, 4, 4],
                [4, 5, 7, 4],[4, 5, 4, 8],[6, 5, 7, 4],[4, 8, 4, 8],[6, 5, 7, 8],
                [4, 8, 7, 8],[6, 8, 7, 8],[10, 8, 7, 8],[10, 8, 7, 11],
                [10, 11, 9, 8], [10, 11, 7, 11],[10, 11, 9, 11]],
                "M7" : [[1, 0, 1, 3],[1, 1, 1, 3],[1, 0, 1, 4],[5, 1, 1, 3],
                [5, 0, 1, 4],[1, 5, 1, 3],[5, 1, 1, 4],[1, 5, 4, 3],[5, 5, 1, 4],
                [5, 5, 4, 3],[5, 0, 4, 8],[6, 5, 4 ,3],[6, 0, 4, 8],
                [5, 5, 4, 4],[6, 0, 8, 8],[5, 5, 8, 4],[5, 0, 9, 8],
                [5, 5, 4, 8],[6, 5, 8, 4],[6, 0, 9, 8],[5, 8, 4, 8],[6, 5, 8, 8],
                [10, 0, 9, 8],[5, 5, 9, 8],[10, 0, 8, 11]],
                "m7" : [[1, 1, 0, 2],[4, 1, 0, 2],[1, 4, 0, 2],[4, 1, 0, 4],
                [1, 4, 4, 2],[6, 4, 0, 3],[4, 4, 0, 4],[4, 4, 4, 2],[6, 4, 4, 2],
                [4, 4, 4, 4],[4, 8, 0, 4],[4, 4, 7, 4],[4, 4, 4, 7],[4, 8, 0, 7],
                [6, 4, 7, 4],[4, 8, 4, 7],[6, 4, 7, 7],[4, 8, 7, 7]],
                "sus4" : [[1, 1, 2, 4],[6, 6, 4, 4],[6, 6, 4, 4],[6, 8, 9, 9],
                [11, 8, 9, 9],[11, 8, 9, 11]],
                "sus2" : [[1, 3, 4, 4],[6, 3, 4, 4],[6, 3, 4, 6],[6, 8, 4, 6],
                [8, 8, 4, 4],[6, 8, 9, 6],[8, 8, 9, 6],[8, 8, 9, 11]],
                "dim" : [[0, 1, 0, 4],[0, 4, 0, 4],[0, 4, 3, 4],[0, 7, 0, 4],
                [6, 4, 3, 4],[6, 7, 0, 4],[6, 4, 3, 7],[6, 7, 0, 7],[6, 7, 0, 10],
                [6, 7, 3, 7],[0, 7, 9, 7]],
                "aug" : [[2, 1, 1, 0],[2, 1, 1, 4],[2, 5, 1, 4],[6, 5, 5, 0],[2, 5, 5, 4],
                [6, 5, 5, 4],[6, 5, 9, 0],[6, 5, 5, 8],[6, 9, 5, 8],[10, 9, 9, 0]]
            },
            "D" : {
                "M" : [[2, 2, 2, 0],[2, 2, 2, 5],[2, 6, 2, 5],[7, 6, 5, 0],[2, 6, 5, 5],[7, 6, 5, 5],[7, 6, 10, 0],[7, 6, 5, 9],[7, 9, 5, 9],[11, 9,10, 0],[7, 9, 10, 9],[11, 9, 10, 9]],
                "m" : [[2, 2, 1, 0],[2, 2, 1, 5],[2, 5, 1, 5],[7, 5, 5, 0],[2, 5, 5, 5],[7, 5, 5, 5],[7, 5, 5, 8], [7, 9, 5, 8],[10, 9, 10, 0]],
                "7" : [[2, 0, 2, 0],[2, 0, 2, 3],[5, 0, 2, 0],[2, 2, 2, 3],[2, 0, 2, 5],[5, 2, 2, 0],[5, 2, 2, 3],[5, 0, 2, 5],[2, 6, 2, 3],[5, 6, 2, 0]],
                "M7" : [[2, 1, 2, 0],[2, 1, 2, 4],[2, 2, 2, 4],[2, 1, 2, 5],[6, 2, 2, 0],[6, 2, 2, 4],[2, 6, 2, 4]],
                "m7" : [[2, 0, 1, 0],[2, 0, 1, 3],[5, 0, 1, 0],[2, 2, 1, 3],[2, 0, 1, 5],[5, 2, 1, 0],[5, 2, 1, 3],[5, 0, 1, 5]],
                "sus4" : [[0, 2, 3, 0],[0, 2, 5, 0],[2, 2, 3, 0],[0, 2, 5, 5],[2, 2, 3, 5],[7, 7, 3, 0],[0, 7, 10, 0]],
                "sus2" : [[2, 2, 0, 0],[2, 2, 0, 5],[7, 4, 0, 0],[2, 4, 0, 5],[7, 4, 5, 0],[7, 9, 0, 0],[2, 4, 5, 5]],
                "dim" : [[1, 2, 1, 5],[1, 5, 1, 5],[1, 5, 4, 5],[7, 5, 4, 5],[7, 5, 4, 8],[7, 8, 4, 8],[7, 8, 10, 8]],
                "aug" : [[3, 2, 2, 1],[3, 2, 2, 5],[3, 6, 2, 5],[3, 6, 6, 5],[7, 6, 6, 5],[7, 6, 6, 9],[7, 10, 6, 9]]
            },
            "D#" : {
                "M" : [[0, 3, 3, 1],[3, 3, 3, 1],[0, 3, 6, 6],[3, 3, 3, 6], [0, 7, 6, 6],
                [3, 7, 3, 6],[0, 10, 6, 6],[3, 7, 6, 6]],
                "m" : [[3, 3, 2, 1],[3, 3, 2, 6], [3, 6, 2, 6], [3, 6, 6, 6],
                [8, 6, 6, 6],[8, 6, 6, 9]],
                "7" : [[0, 1, 3, 1],[3, 1, 3, 1],[0, 3, 3, 4],[3, 1, 3, 4],[0, 3, 6, 4]],
                "M7" : [[0, 2, 3, 1],[3, 2, 3, 1],[0, 3, 3, 5],[0, 2, 3, 6],[0, 2, 6, 5]],
                "m7" : [[3, 1, 2, 2],[3, 1, 2, 4],[3, 3, 2, 4],[6, 3, 2, 4],[3, 6, 2, 4]],
                "sus4" : [[1, 3, 4, 1],[3, 3, 4, 1],[3, 3, 4, 6],[8, 8, 6, 6],[8, 10, 11, 11]],
                "sus2" : [[3, 3, 1, 1],[3, 5, 6, 6],[8, 5, 6, 6],[8, 5, 6, 8],[8, 10, 6, 8]],
                "dim" : [[2, 3, 2, 0],[2, 3, 2, 6],[2, 6, 2, 6],[8, 6, 5, 0],[2, 6, 5, 6]],
                "aug" : [[0, 3, 3, 2],[4, 3, 3, 2],[0, 3, 7, 6],[4, 3, 3, 6],[0, 7, 7,6]]
            },
            "E" : {
                "M" : [[1, 4, 0, 2],[1, 4, 4, 2],[4, 4, 4, 2],[4, 4, 4, 7],[4, 8, 0, 7]],
                "m" : [[0, 4, 0, 2],[0, 4, 3, 2],[4, 4, 3, 2],[0, 4, 7, 7],[0, 11, 0, 7]],
                "7" : [[1, 2, 0, 2],[1, 2, 0, 5],[1, 2, 4, 2],[1, 4, 0, 5],[4, 2, 4, 2]],
                "M7" : [[1, 3, 0, 2],[1, 3, 4, 2],[4, 3, 4, 2],[4, 3, 4, 6],[4, 4, 4, 6]],
                "m7" : [[0, 2, 0, 2],[0, 2, 0, 5],[0, 2, 3, 2],[0, 4, 0, 5],[4, 2, 3, 2]],
                "sus4" : [[2, 4, 0, 2],[4, 4, 0, 0],[2, 4, 5, 2],[4, 4, 5, 0],[4, 4, 5, 2]],
                "sus2" : [[4, 4, 2, 5],[4, 6, 0, 5],[7, 6, 0, 5],[9, 6, 0, 5],[7, 6, 0, 7]],
                "dim" : [[0, 4, 0, 1],[0, 4, 3, 1],[3, 4, 3, 1],[0, 4, 6, 7],[0, 10, 0, 7]],
                "aug" : [[1, 0, 0, 3],[1, 4, 0, 3],[1, 4, 4, 3],[5, 4, 4, 3],[5, 0, 4, 7]]
            },
            "F" : {
                "M" : [[2, 0, 1, 0],[2, 0, 1, 3],[5, 0, 1, 0],[2, 5, 1, 3],[5, 5, 1, 0]],
                "m" : [[1, 0, 1, 3],[1, 5, 1, 3],[1, 5, 4, 3],[5, 5, 4, 3],[5, 0, 4, 8]],
                "7" : [[2, 3, 1, 0],[2, 3, 1, 3],[5, 3, 1, 0],[2, 0, 5, 6],[2, 3, 5, 3]],
                "M7" : [[2, 0, 0, 0],[2, 0, 0, 3],[5, 0, 0, 0],[2, 5, 0, 0],[2, 4, 1, 0]],
                "m7" : [[1, 3, 1, 3],[1, 3, 4, 3],[5, 3, 4, 3],[5, 0, 4, 6],[5, 3, 4, 6]],
                "sus4" : [[3, 0, 1, 1],[3, 0, 1, 3],[5 ,0, 1, 1],[3, 5, 1, 3],[5, 5, 1, 1]],
                "sus2" : [[0, 0, 1, 3],[0, 5, 1, 3],[0, 5, 3, 3],[0, 0, 8, 8],[5, 5, 3, 3]],
                "dim" : [[1, 5, 1, 2],[1, 5, 4, 2],[4, 5, 4, 2],[4, 5, 3, 8],[4, 8, 4, 8]],
                ("aug", '+') : [[2, 1, 1, 0],[2, 1, 1, 4],[2, 5, 1, 4],[2, 5, 5, 4],[6, 5, 5, 0]]
            },
            "F#" : {
                "M" : [[3, 1, 2, 1],[3, 1, 2, 4],[3, 6, 2, 4],[3, 6, 6, 4],[6, 6, 6, 4]],
                "m" : [[2, 1, 2, 0],[2, 1, 2, 4,],[2, 6, 2, 4],[6, 6, 2, 0],[2, 6, 5, 4],
                [6, 6, 5, 0],[6, 6, 5, 4],[6, 9, 9, 9]],
                "7" : [[3, 1, 0, 1],[3, 1, 0, 4],[3, 4, 2, 1],[3, 4, 0, 4],[3, 6, 0, 4]],
                "M7" : [[3, 1, 1, 1],[3, 1, 1, 4],[3, 5, 2, 1],[3, 5, 1, 4],[3, 5, 2, 4]],
                "m7" : [[2, 1, 0, 0],[2, 1, 0, 4],[2, 6, 0, 0],[2, 4, 2, 0],[2, 4, 0, 4]],
                "sus4" : [[4, 1, 2, 2],[4, 1, 2, 4],[4, 6, 2, 4],[6, 6, 2, 2],[4, 6, 7, 4]],
                "sus2" : [[1, 1, 2, 4],[6, 6, 4, 4],[6, 8, 9, 9],[11, 8, 9, 9],[11, 8, 9, 11]],
                "dim" : [[2, 0, 2, 0],[2, 0, 2, 3],[5, 0, 2, 0],[2, 6, 2, 3],[5, 6, 2, 0]],
                "aug" : [[3, 2, 2, 1],[3, 2, 2, 5],[3, 6, 2, 5],[3, 6, 6, 5],[7, 6, 6, 5]]
            },
            "G" : {
                "M" : [[0, 2, 3, 2],[4, 2, 3, 2],[4, 2, 3, 5],[0, 7, 7, 5],[4, 7, 3, 5]],
                "m" : [[0, 2, 3, 1],[3, 2, 3, 1],[0, 2, 6, 5],[3, 2, 3, 5],[0, 7, 6, 5]],
                "7" : [[0, 2, 1, 2],[0, 5, 1, 3],[4, 2, 1, 2],[0, 5, 3, 2],[4, 2, 1, 5]],
                "M7" : [[0, 2, 2, 2],[0, 6, 2, 2],[4, 2, 2, 2],[0, 6, 3, 2],[0, 6, 7, 5], [4, 2, 2, 5]],
                "m7" : [[0, 2, 1, 1],[0, 5, 1, 1],[3, 2, 1, 1],[0, 5, 3, 1],[3, 2, 1, 5]],
                "sus4" : [[0, 0, 3, 5],[0, 2, 3, 3],[0, 0, 8, 5],[5, 2, 3, 3],[5, 0, 3, 5]],
                "sus2" : [[0, 2, 3, 0],[0, 2, 5, 0],[2, 2, 3, 0],[0, 2, 5, 5],[2, 2, 3, 5]],
                "dim" : [[0, 1, 3, 1],[3, 1, 3, 1],[3, 1, 3, 4],[0, 7, 6, 4],[3, 7, 3, 4]],
                "aug" : [[0, 3, 3, 2],[4, 3, 3, 2],[0, 3, 7, 6],[4, 3, 3, 6],[0, 7, 7, 6]]
            },
            "G#" : {
                "M" : [[1, 3, 4, 3],[5, 3, 4, 3],[5, 0, 4, 6],[5, 3, 4, 6],[8, 0, 4, 6]],
                "m" : [[1, 3, 4, 2],[4, 3, 4, 2],[4, 3, 4, 6],[4, 8, 4, 6],[4, 8, 7, 6]],
                "7" : [[1, 0, 2, 3],[1, 3, 2, 3],[5, 3, 2, 3],[5, 0, 2, 6],[5, 3, 2, 6]],
                "M7" : [[1, 1, 0, 2],[0, 0, 4, 3],[0, 0, 3, 6],[0, 3, 3, 3],[1, 3, 3, 3]],
                "m7" : [[1, 3, 2, 2],[4, 3, 2, 2],[4, 3, 2, 6],[4, 6, 4, 2],[4, 6, 2, 6]],
                "sus4" : [[1, 3, 4, 4],[6, 3, 4, 4],[6, 3, 4, 6],[6, 8, 4, 6],[8, 8, 4, 4]],
                "sus2" : [[1, 3, 4, 1],[3, 3, 4, 1],[3, 3, 4, 6],[8, 8, 6, 6],[8, 10, 11, 11]],
                "dim" : [[1, 2, 4, 2],[4, 2, 4, 2],[4, 2, 4, 5],[4, 8, 4, 5],[4, 8, 7, 5]],
                "aug" : [[1, 0, 0, 3],[1, 4, 0, 3],[1, 4, 4, 3],[5, 4, 4, 3],[5, 0, 4, 7]]
            }
        }
        
        base_note, accidental, chord_type = self.split_chord(chord_name)
        
        # # no chord type supplied
        # if chord_type == "":
        #     all_chords = []
        #     for chord_type in chords[base_note + accidental].values():
        #         for fingering in chord_type:
        #             all_chords.append(fingering)
        #     return all_chords
        
        # return ("", "M", "Maj", "m", "min", "7", "M7", "Maj7", "m7", "min7", 
        # "sus4", "sus", "sus2", "dim", "aug", "+") 
        
        types_to_type = {
            "M" : ["", "M", "Maj"],
            "m" : ["m", "min"],
            "7" : ["7"],
            "M7" : ["M7", "Maj7"],
            "m7" : ["m7", "min7"],
            "sus4" : ["sus4", "sus"],
            "sus2" : ["sus2"],
            "dim" : ["dim"],
            "aug" : ["aug", "+"]
        }
        
        for type, types in types_to_type.items():
            if chord_type in types:
                chord_type = type

        return chords[base_note + accidental][chord_type]
        
class UkulelePrinter:
    """Represents a ukulele printer

    This class contains convenience methods to print different
    ukulele graphics in the terminal. It can print two
    representations of a ukulele - full and compact. The full
    graphic is used in the chord browser where the fretboard
    is oriented horizontally and spans the whole width of the
    terminal, and the compact graphic is used in the song
    browser where the fretboard is oriented vertically and
    only has a provision for at most four frets and the fret
    nut.
    """
    FRET_HEAD_FULL = """\
  OOO
___|____
        `;...
           ||
           ||
           ||
           ||
           ||
           ||
___.____,;'''
   |
  OOO
    """

    FRET_HEAD_COMPACT = """\
_______
| | | |
| | | |
| | | |
| | | |
'''''''
    """

    @classmethod
    def full_head_rows(cls) -> int:
        """Return the number of lines/rows of the full ukulele head

        :return: number of lines/rows of the full ukulele head
        :rtyp: int

        :classmethod:
        """
        return (12)

    @classmethod
    def full_head_max_cols(cls) -> int:
        """Return the number of maximum columns of the full ukulele head

        The graphic for the ukulele head has different number of columns
        per line. This method returns the maximum number of columns in
        each line.

        :return: number of maximum columns of the full ukulele head
        :rtyp: int

        :classmethod:
        """
        return (13)
    
    @classmethod
    def compact_head_rows(cls) -> int:
        """Return the number of lines/rows of the compact ukulele head

        :return: number of lines/rows of the compact ukulele head
        :rtyp: int

        :classmethod:
        """
        return (7)

    @classmethod
    def compact_head_max_cols(cls) -> int:
        """Return the number of maximum columns of the compact ukulele head

        The graphic for the ukulele head has different number of columns
        per line. This method returns the maximum number of columns in
        each line.

        :return: number of maximum columns of the compact ukulele head
        :rtyp: int

        :classmethod:
        """
        return (4)

    @classmethod
    def str_uke_full(cls, fret_width: int=9, num_frets: int=12) -> list[str]:
        """Return the lines that represent the graphic for a full ukulele

        The full ukulele graphic is used in the chord browser where the fretboard
        spans the whole column. It consists of the head of the ukulele
        and the frets. Each fret has a width ``fret_width`` and each string is
        drawn using the ``-`` character, with each fret demarcated by a
        ``|`` character. The last fret ends with a ``|``.

        :param fret_width: the number of characters consisting each fret
        :type fret_width: int
        :param num_frets: the number of frets in the ukulele
        :type num_frets: int

        :return: a list of strings representing each line of the graphic
            of a whole ukulele. 
        :rtyp: list[str]

        :classmethod:
        """
        cls.fret_width = fret_width
        
        # HINT: Looking at ``FRET_HEAD_FULL~``, you may notice that
        #       the "strings" occur at lines 4 to 7 inclusive, while
        #       line 3 has no "string".
        uke_full = []
        for line in cls.FRET_HEAD_FULL.split("\n"):
            uke_full.append(line)
        
        # top and bottom part
        uke_full[2] = uke_full[2] + (('_' * fret_width) + '.') * num_frets
        uke_full[3] = uke_full[3] + ((' ' * fret_width) + '|') * num_frets
        uke_full[8] = uke_full[8] + (('_' * fret_width) + '|') * num_frets
        
        for i in range(4, 8):
            uke_full[i] = uke_full[i] + (('-' * fret_width) + '|') * num_frets

        return uke_full