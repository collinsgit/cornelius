import spacy
from spacy.symbols import nsubj, VERB

nlp = spacy.load("en_core_web_sm")


class Sentence(object):
    """
    General class for parsing and representing a sentence.

    Provides access to words, parts-of-speech, phrases, and dependencies.
    """

    def __init__(self, text):
        """
        Initialize the sentence, storing the text in its tokenized form
        :param text: The input text, formatted as a proper sentence.
        """
        self.text = nlp(text)

    def entities(self, proper=False):
        """
        Creates a list of all perceived entities in the text, in the order they occur.
        Entities represented as a list of word strings.
        :param proper: If true, only properly named entities are included.
        :return: A list of lists of strings.
        """

        if proper:
            return list(self.text.ents)
        else:
            return list(self.text.noun_chunks)

    def root(self):
        """
        Find the possible root verbs of the sentence.
        :return:  A set of Tokens
        """

        verbs = set()
        for possible_subject in self.text:
            if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
                verbs.add(possible_subject.head)

        return verbs


if __name__ == '__main__':
    s = Sentence('Jack is a very tall boy.')
    print(s.root())
