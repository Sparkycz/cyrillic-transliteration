# -*- coding: utf-8 -*-
import unittest
import srtranslitr

serbian_alphabet_cyrillic = 'АаБбВвГгДдЂђЕеЖжЗзИиЈјКкЛлЉљМмНнЊњОоПпРрСсТтЋћУуФфХхЦцЧчЏџШш'
serbian_alphabet_latin = 'AaBbVvGgDdĐđEeŽžZzIiJjKkLlLjljMmNnNjnjOoPpRrSsTtĆćUuFfHhCcČčDždžŠš'

special_chars = '‘’‚“”„†‡‰‹›♠♣♥♦‾←↑→↓™!"#$%&\'()*+,-./ :;<=>?@[\\]^_`{|}~…–—¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿×'

diacritic_chars = 'ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝàáâãäåæçèéêëìíîïðñòóôõöøùúûüý'

numerical_chars = '1234567890'

alphabet_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

mix_characters_some_cyrillic = '!ЉFљñМ мНÈÆнЊњО)*+,оП>пР?р'
mix_characters_all_latin = '!LjFljñM mNÈÆnNjnjO)*+,oP>pR?r'

mix_characters_some_cyrillic_no_alpha = '\'Ћ<=>?ћУуФфХхЦцЧчЏ%4џШ12ш♥'
mix_characters_all_latin_no_alpha = '\'Ć<=>?ćUuFfHhCcČčDž%4džŠ12š♥'

class TestSerbianTransliterationFromCyrillicToLatin(unittest.TestCase):

    def test_serbian_alphabet_transliteration(self):
        ''' Transliteration of entire Serbian cyrillic alphabet to latin.
        '''
        transliterated_serbian_alphabet = srtranslitr.to_latin(serbian_alphabet_cyrillic)

        self.assertEqual(transliterated_serbian_alphabet, serbian_alphabet_latin)


    def test_special_characters(self):
        ''' Special characters should remain the same.
        '''
        transliterated_special_chars = srtranslitr.to_latin(special_chars)

        self.assertEqual(transliterated_special_chars, special_chars)


    def test_special_diacritic_characters(self):
        ''' Diacritic characters should remain the same.
        '''
        transliterated_diacritic_chars = srtranslitr.to_latin(diacritic_chars)

        self.assertEqual(transliterated_diacritic_chars, diacritic_chars)


    def test_numerical_characters(self):
        ''' Numerical characters should remain the same.
        '''
        transliterated_numerical_chars = srtranslitr.to_latin(numerical_chars)

        self.assertEqual(transliterated_numerical_chars, numerical_chars)


    def test_latin_alphabet_characters(self):
        ''' Alphabet characters should remain the same.
        '''
        transliterated_alphabet_chars = srtranslitr.to_latin(alphabet_chars)

        self.assertEqual(transliterated_alphabet_chars, alphabet_chars)


    def test_mix_characters(self):
        ''' Serbian cyrillic characters should be transliterated but non serbian cyrillic ones shouldn't.
        '''

        transliterated_mix = srtranslitr.to_latin(mix_characters_some_cyrillic)

        self.assertEqual(transliterated_mix, mix_characters_all_latin)


class TestSerbianTransliterationFromLatinToCyrillic(unittest.TestCase):

    def test_serbian_alphabet_transliteration(self):
        ''' Transliteration of entire Serbian cyrillic alphabet to latin.
        '''
        transliterated_serbian_alphabet = srtranslitr.to_cyrillic(serbian_alphabet_latin)

        self.assertEqual(transliterated_serbian_alphabet, serbian_alphabet_cyrillic)


    def test_special_characters(self):
        ''' Special characters should remain the same.
        '''
        transliterated_special_chars = srtranslitr.to_cyrillic(special_chars)

        self.assertEqual(transliterated_special_chars, special_chars)


    def test_special_diacritic_characters(self):
        ''' Diacritic characters should remain the same.
        '''
        transliterated_diacritic_chars = srtranslitr.to_cyrillic(diacritic_chars)

        self.assertEqual(transliterated_diacritic_chars, diacritic_chars)


    def test_numerical_characters(self):
        ''' Numerical characters should remain the same.
        '''
        transliterated_numerical_chars = srtranslitr.to_cyrillic(numerical_chars)

        self.assertEqual(transliterated_numerical_chars, numerical_chars)

    def test_mix_characters(self):
        ''' Serbian cyrillic characters should be transliterated but non serbian cyrillic ones shouldn't.
        '''
        transliterated_mix = srtranslitr.to_cyrillic(mix_characters_all_latin_no_alpha)

        self.assertEqual(transliterated_mix, mix_characters_some_cyrillic_no_alpha)


if __name__ == '__main__':
    unittest.main()