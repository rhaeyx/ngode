import unittest
import uke

class Ukulele_InitTest(unittest.TestCase):
    def setUp(self):
        self.uke_std = uke.Ukulele()

    def test_basic(self):
        self.assertListEqual(self.uke_std.tuning, ['G', 'C', 'E', 'A'])
        self.assertListEqual(self.uke_std.octaves, [4, 4, 4, 4])
        self.assertEqual(self.uke_std.num_frets, 20)
    
    def test_otherTuning(self):
        uke_obj = uke.Ukulele(
            tuning=['E', 'B', 'G', 'D', 'A', 'E'],
            octaves=[4, 4, 4, 4, 4, 5],
            num_frets=15,
        )

        self.assertListEqual(uke_obj.tuning, ['E', 'B', 'G', 'D', 'A', 'E'])
        self.assertListEqual(uke_obj.octaves, [4, 4, 4, 4, 4, 5])
        self.assertEqual(uke_obj.num_frets, 15)


class Ukulele_FretNotesTest(unittest.TestCase):
    def setUp(self):
        self.uke_std = uke.Ukulele()
    
    def test_basic(self):
        fret_notes = self.uke_std.gen_fret_notes()

        for each_string in self.uke_std.tuning:
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes)
                self.assertEqual(len(fret_notes[each_string]), self.uke_std.num_frets)
        
        self.assertListEqual(fret_notes['G'], ['G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D',])
        self.assertListEqual(fret_notes['C'], ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G',])

    def test_otherTuning(self):
        uke_obj = uke.Ukulele(
            tuning=['E', 'B', 'G', 'D', 'A', 'E'],
            octaves=[4, 4, 4, 4, 4, 5],
            num_frets=15,
        )

        fret_notes = uke_obj.gen_fret_notes()

        for each_string in uke_obj.tuning:
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes)
                self.assertEqual(len(fret_notes[each_string]), uke_obj.num_frets)

        self.assertListEqual(fret_notes['E'], ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#',])
        self.assertListEqual(fret_notes['A'], ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B',])


class Ukulele_IdxsOnFretTest(unittest.TestCase):
    def setUp(self):
        self.uke_std = uke.Ukulele()
        self.guitar_std = uke.Ukulele(tuning=['E', 'B', 'G', 'D', 'A', 'E'], octaves=[4, 4, 4, 4, 4, 5], num_frets=15)
    
    def test_basic(self):
        fret_notes = self.uke_std.get_note_idxs_on_fret(['C', 'E', 'G'])
        fret_notes_ans = {
            'G': [0, 5, 9, 12, 17],
            'C': [0, 4, 7, 12, 16, 19],
            'E': [0, 3, 8, 12, 15],
            'A': [3, 7, 10, 15, 19],
        }

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.uke_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])
    
    def test_threeNotesPt1(self):
        fret_notes = self.uke_std.get_note_idxs_on_fret(['D', 'F#', 'A'])
        fret_notes_ans = {
            'G': [2, 7, 11, 14, 19],
            'C': [2, 6, 9, 14, 18],
            'E': [2, 5, 10, 14, 17],
            'A': [0, 5, 9, 12, 17],
        }

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.uke_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])
    
    def test_threeNotesPt2(self):
        fret_notes = self.uke_std.get_note_idxs_on_fret(['A', 'A#', 'B'])
        fret_notes_ans = {
            'G': [2, 3, 4, 14, 15, 16],
            'C': [9, 10, 11],
            'E': [5, 6, 7, 17, 18, 19],
            'A': [0, 1, 2, 12, 13, 14],
        }

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.uke_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])
    
    def test_oneNote(self):
        fret_notes = self.uke_std.get_note_idxs_on_fret(['F'])
        fret_notes_ans = {
            'G': [10],
            'C': [5, 17],
            'E': [1, 13],
            'A': [8],
        }

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.uke_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])

    def test_otherTuningThreeNotesPt1(self):
        fret_notes = self.guitar_std.get_note_idxs_on_fret(['D', 'F#', 'A'])
        fret_notes_ans = {
            'E': [2, 5, 10, 14],
            'B': [3, 7, 10],
            'G': [2, 7, 11, 14],
            'D': [0, 4, 7, 12],
            'A': [0, 5, 9, 12],
        }

        self.assertEqual(self.guitar_std.num_frets, 15)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.guitar_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])
    
    def test_otherTuningThreeNotesPt2(self):
        fret_notes = self.guitar_std.get_note_idxs_on_fret(['B', 'D#', 'F#'])
        fret_notes_ans = {
            'E': [2, 7, 11, 14],
            'B': [0, 4, 7, 12],
            'G': [4, 8, 11],
            'D': [1, 4, 9, 13],
            'A': [2, 6, 9, 14],
        }

        self.assertEqual(self.guitar_std.num_frets, 15)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.guitar_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])
    
    def test_otherTuningOneNote(self):
        fret_notes = self.guitar_std.get_note_idxs_on_fret(['E'])
        fret_notes_ans = {
            'E': [0, 12],
            'B': [5],
            'G': [9],
            'D': [2, 14],
            'A': [7],
        }

        self.assertEqual(self.guitar_std.num_frets, 15)

        for each_string, each_idx_in_str in fret_notes.items():
            with self.subTest(string=each_string):
                self.assertIn(each_string, fret_notes_ans)
                self.assertLess(max(each_idx_in_str), self.guitar_std.num_frets)
                self.assertListEqual(each_idx_in_str, fret_notes_ans[each_string])


class SongCollection_ChordFingeringTest(unittest.TestCase):
    def setUp(self):
        self.uke_std = uke.Ukulele()
    
    def test_basic(self):
        chord_patterns = self.uke_std.get_chord_fingerings('C')
        chord_patterns_ans = [
            [0, 0, 0, 3],
            [0, 0, 0, 7],
            [0, 4, 0, 3],
            [5, 4, 3, 3],
            [5, 7, 8, 7],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)
    
    def test_triadPt1(self):
        chord_patterns = self.uke_std.get_chord_fingerings('F#m')
        chord_patterns_ans = [
            [2, 1, 2, 0],
            [6, 6, 5, 0],
            [6, 6, 5, 4],
            [6, 9, 9, 9],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)
    
    def test_triadPt2(self):
        chord_patterns = self.uke_std.get_chord_fingerings('D#dim')
        chord_patterns_ans = [
            [2, 3, 2, 0],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)
    
    def test_triadPt3(self):
        chord_patterns = self.uke_std.get_chord_fingerings('Esus')
        chord_patterns_ans = [
            [4, 4, 0, 0],
            [2, 4, 0, 2],
            [4, 4, 5, 0],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)
    
    def test_triadPt4(self):
        chord_patterns = self.uke_std.get_chord_fingerings('B+')
        chord_patterns_ans = [
            [0, 3, 3, 2],
            [4, 3, 3, 2],
            [0, 7, 7, 6],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)
    
    def test_seventhPt1(self):
        chord_patterns = self.uke_std.get_chord_fingerings('A7')
        chord_patterns_ans = [
            [0, 1, 0, 0],
            [2, 1, 3, 0],
            [0, 4, 3, 4],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)
    
    def test_seventhPt2(self):
        chord_patterns = self.uke_std.get_chord_fingerings('GM7')
        chord_patterns_ans = [
            [0, 2, 2, 2],
            [4, 2, 2, 2],
            [0, 6, 7, 5],
        ]

        self.assertEqual(self.uke_std.num_frets, 20)

        for each_pattern_ans in chord_patterns_ans:
            with self.subTest():
                self.assertIn(each_pattern_ans, chord_patterns)


if __name__ == '__main__':
    unittest.main()