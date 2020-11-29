from typing import List

from natasha import (
    Doc,
    MorphVocab,
    Segmenter,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
)

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)


class NatashaExtractor:
    def __init__(self, text: str):
        self.doc = Doc(text)
        self.doc.segment(segmenter)
        self.doc.tag_morph(morph_tagger)
        self.doc.parse_syntax(syntax_parser)
        self.doc.tag_ner(ner_tagger)
        for span in self.doc.spans:
            span.normalize(morph_vocab)

    def find_locations(self) -> List[str]:
        locations = list(filter(lambda span: span.type == 'LOC', self.doc.spans))

        return list(map(lambda span: span.normal, locations))
