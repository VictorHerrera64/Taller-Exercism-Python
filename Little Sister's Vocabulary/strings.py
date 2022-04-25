def add_prefix_un(word):
    """Add the prefix 'un' to a given word.
 
    :param word: str of a root word
    :return:  str of root word with un prefix
 
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    return "un" + word

# add_prefix_un()´s outputs
word = add_prefix_un("supported")
print(word)

def make_word_groups(vocab_words):
    """Add a prefix to a list of words.
 
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.
    """
    for index, word in enumerate(vocab_words[1:], start=1):
        vocab_words[index] = vocab_words[0] + word
    return " :: ".join(vocab_words)

# make_word_groups()´s outputs
vocab_words = ['en', 'close', 'joy', 'lighten']
word = make_word_groups(vocab_words)
print(word)

def remove_suffix_ness(word):
    """Remove the suffix 'ness' from a given word.
 
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
 
    This function takes in a word and returns the base word with `ness` removed.
    """
    if word.endswith("ness"):
        word = word[:-4]
        if word[-1] == "i":
            word = word[:-1] + "y"
    return word

# remove_suffix_ness()´s outputs
word = remove_suffix_ness("heaviness")
print(word)

def adjective_to_verb(sentence, index):
    """Convert a given edjective in s sentence to a verb.
 
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.
 
    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    # remove period from end of sentence
    sentence = sentence[:-1]
    word = sentence.split()[index]
    return word + "en"

# adjective_to_verb()´s outputs
print(adjective_to_verb("I need to make that bright.", -1))

