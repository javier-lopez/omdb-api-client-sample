import pytest

import omdb


def test_search():
    s = 'True Grit'
    results = omdb.search(s)
    assert results[0]['Title'] == s


def test_get_by_id():
    i = 'tt0065126'
    result = omdb.get_by_id(i)
    assert result['imdbID'] == i


def test_get_by_title():
    t = 'True Grit'
    result = omdb.get_by_title(t)
    assert result['Title'] == t


def test_empty_data():
    invalid = 'asdfghjkl'

    assert omdb.search(invalid) == []
    assert omdb.get_by_id(invalid) == {}
    assert omdb.get_by_title(invalid) == {}


def test_search_stem():
    s = 'stem'
    results = omdb.search(s)

    assert len(results) >= 30

    media_journal = {}
    media_videogame = {}

    for media in results:
        if media['Title'] == 'The STEM Journals':
            media_journal = media
        elif media['Title'] == 'Activision: STEM - in the Videogame Industry':
            media_videogame = media

    assert media_journal
    assert media_videogame

    media_videogame_details = omdb.get_by_id(media_videogame['imdbID'])

    assert media_videogame_details['Released'] == '23 Nov 2010'
    assert media_videogame_details['Director'] == 'Mike Feurstein'

    media_journal_details = omdb.get_by_title(media_journal['Title'])
    assert 'Science, Technology, Engineering and Math' in \
        media_journal_details['Plot']
    assert media_journal_details['Runtime'] == '22 min'
