import os.path
import langdetect

from googletrans import Translator
from collections import Counter
from iso_language_codes import language_dictionary

from stringstranslate.exceptions import EXCEPTION_LANGUAGE_CODES


class StringsTranslator:
    """
    Object responsible for the translation of .strings files.
    """

    def __init__(self):
        self.translator = Translator()

    def translate_strings(self, file_name: str, target_lang: str, source_lang=""):
        """
        Translates all of the strings in a .strings file and outputs a newly creates .strings file.

        :param file_name: str; Path to the .strings file to translate
        :param target_lang: str; ISO code of target language
        :param source_lang: str; ISO code of the source language (if not given, the auto-detected language will be used)
        """

        # Prevent invalid language parameter
        if target_lang not in language_dictionary().keys() and target_lang not in EXCEPTION_LANGUAGE_CODES:
            raise ValueError("The target language is not valid.")

        # Prevent invalid file parameter
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The strings file does not exist in the given location.")

        words = []

        # Load the strings to be translated from the file
        for line in open(file_name, "r", encoding="utf-8"):
            if "\"" in line and not line.startswith("/*"):
                words.append(line.split("\"")[1])

        # Detect the source language if not specified
        if not source_lang:
            try:
                detected_langs = [langdetect.detect(word) for word in words]
                source_lang = Counter(detected_langs).most_common(1)[0][0]
            except Exception:
                raise Exception("Language could not be automatically detected.")

        # Translate individual strings and save them into file
        file = open("output/output_" + target_lang + ".strings", "w", encoding="utf-8")
        for word in words:
            file.write("\"" + word.replace("\\", "") + "\" = \"" + self.translator.translate(word, dest=target_lang,
                                                        src=source_lang).text.replace("\\", "").capitalize() + "\";\n")
        file.close()

    def translate_storyboard(self, file_name: str, target_lang: str, source_lang=""):
        """
        Translates all of the strings in a storyboard .strings file and outputs a newly creates .strings file.

        :param file_name: str; Path to the storyboard .strings file to translate
        :param target_lang: str; ISO code of target language
        :param source_lang: str; ISO code of the source language (if not given, the auto-detected language will be used)
        """

        # Prevent invalid language parameter
        if target_lang not in language_dictionary().keys() and target_lang not in EXCEPTION_LANGUAGE_CODES:
            raise ValueError("The target language is not valid.")

        # Prevent invalid file parameter
        if not os.path.isfile(file_name):
            raise FileNotFoundError("The storyboard file does not exist in the given location.")

        ids = []
        words = []

        for line in open(file_name, "r", encoding="utf-8"):
            if len(line) > 1 and "\"" in line and not line.startswith("/*"):
                ids.append(line.split("\"")[1])
                words.append(line.split("\"")[3])

        # Detect the source language if not specified
        if not source_lang:
            try:
                detected_langs = [langdetect.detect(word) for word in words]
                source_lang = Counter(detected_langs).most_common(1)[0][0]
            except Exception:
                raise Exception("Language could not be automatically detected.")

        # Translate individual strings and save them into file
        file = open("output/output_" + target_lang + ".strings", "w", encoding="utf-8")
        for word_id, word in zip(ids, words):
            file.write("\"" + word_id.replace("\\", "") + "\" = \"" + self.translator.translate(word, dest=target_lang,
                                                                    src=source_lang).text.replace("\\", "") + "\";\n")
        file.close()


if __name__ == "__main__":
    pass
