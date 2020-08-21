# strings-translate
A simplistic package for automatic translation of `.strings` files using the **Google Translate API**. As the Google Translate has come to a stage where, while not completely perfect, one can always count on it to provide sufficient translations in over 100 languages. So if you want to automatically localize your iOS, iPadOS or macOS app, you can simply use this package.

## Features

  - **🌍 Source language detection**: The package automatically detects the language of the source `.strings` file
  - **📖 Translation using Google Translate**: The package can easily translate all of the individual strings using the Google Translate API
  - **📝 Saving new .strings files**: The results will be outputted into a new file, which you can directly use in your project

## Usage

### Installation

To get the package, simply use:

```bash
pip install strings-translate
```

### Translation of .strings files

If you want to translate a pure `.strings` file, simply create your `StringsTranslator` and then use its `translate_strings()` method:

```python
from stringstranslate import StringsTranslator

translator = StringsTranslator()
translator.translate_strings(file_name="Localizable.strings", target_lang="es", source_lang="en")
```

The `target_lang` and `source_lang` properties expect ISO codes for the relevant languages. The source language does not need to be entered, but then the detected language of the strings in the file will be used.

This will output a **output/output_es.strings** file with the translated strings.

### Translation of storyboards

If you want to translate a storyboard, the approach is very similar. You only need to use the `translate_storyboard()` method:

```python
from stringstranslate import StringsTranslator

translator = StringsTranslator()
translator.translate_storyboard(file_name="Main.strings", target_lang="es", source_lang="en")
```

Again, the `source_lang` property can be empty and this will output **output/output_es.strings** file.
