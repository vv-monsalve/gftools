import pytest


@pytest.mark.parametrize(
    "url,want",
    [
        ("https://www.google.com", "google.com"),
        ("https://google.com", "google.com"),
        ("http://www.google.com", "google.com"),
        ("http://google.com", "google.com"),
        ("google.com", "google.com"),
        ("", ""),
    ]
)
def test_remove_url_prefix(url, want):
    from gftools.utils import remove_url_prefix
    got = remove_url_prefix(url)
    assert got == want


def test_format_html():
    from gftools.utils import format_html

    input = """<p>
First sentence. Second sentence.
Sentence that uses an abbreviation, e.g. "for example".    Sentence that uses an abbreviation, eg. "for example".
Sentence that uses another abbreviation, i.e. "for example".    Sentence that uses another abbreviation, ie. "for example".
Sentence that ends in etc. Another sentence after it.
Sentence that uses etc. but then doesn't end.
The characters of the film were designed by H.R. Giger. His alien characters became iconic throughout pop culture.
The characters of the film were designed by H.R. Giger, a Swiss sculptural artist. His alien characters became iconic throughout pop culture.
He was referred to H.R. Giger, who headed the H.R. department at the time, then told them they're fired. <-- Can't have it both ways. Legitimate abbreviations at the end of sentences can only be caught if they are known in advance, e.g. etc.
</p>
"""

    output = """<p>
 First sentence.
 Second sentence.
 Sentence that uses an abbreviation, e.g. "for example".
 Sentence that uses an abbreviation, eg. "for example".
 Sentence that uses another abbreviation, i.e. "for example".
 Sentence that uses another abbreviation, ie. "for example".
 Sentence that ends in etc.
 Another sentence after it.
 Sentence that uses etc. but then doesn't end.
 The characters of the film were designed by H.R.
 Giger.
 His alien characters became iconic throughout pop culture.
 The characters of the film were designed by H.R.
 Giger, a Swiss sculptural artist.
 His alien characters became iconic throughout pop culture.
 He was referred to H.R.
 Giger, who headed the H.R. department at the time, then told them they're fired.
 <-- Can't have it both ways.
 Legitimate abbreviations at the end of sentences can only be caught if they are known in advance, e.g. etc.
</p>
"""
    assert format_html(input) == output
