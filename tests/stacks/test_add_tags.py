from add_tags import (
    add_tags,
    inplace_swap,
    ClosingTagBeforeOpeningTagError,
    InvalidTagsError,
    TagPositionOutOfBoundsError,
    Open,
    Closed,
)

import pytest


def test_open_tag_class_str():
    assert (
        str(Open(val=0, tag='a')) ==
        '<a>'
    )


def test_close_tag_class_str():
    assert (
        str(Closed(val=0, tag='a')) ==
        '</a>'
    )


def test_open_ordering():
    assert (
        Open(val=1, tag='we-do-not-care') ==
        1
    )
    assert (
        Open(val=1, tag='we-do-not-care') <
        10
    )


def test_in_place_swap():
    seq = [0, 1, 2, 4]
    inplace_swap(sequence=seq, to_swap=(1, 2))
    assert seq == [0, 2, 1, 4]


def test_add_tags_swappable_position():
    tags = [
        (5, 7, 'b'),
        (0, 4, 'i'),
        (5, 15, 'em'),
        (15, 16, 'b'),
    ]
    text_to_test = 'this is a string'
    res = add_tags(text_to_test, tags)

    assert (
        res ==
        '<i>this</i> <em><b>is</b> a strin</em><b>g</b>'
    )


def test_add_tags_same_starting_index():
    tags = [
        (0, 2, 'a'),
        (0, 2, 'b'),
    ]
    text_to_test = 'xy'
    res = add_tags(text_to_test, tags)

    assert (
        res ==
        '<a><b>xy</b></a>'
    )


def test_add_tags_same_starting_index_diff_closing_index():
    tags = [
        (0, 1, 'a'),
        (0, 2, 'b'),
    ]
    text_to_test = 'xy'
    res = add_tags(text_to_test, tags)

    assert (
        res ==
        '<b><a>x</a>y</b>'
    )


def test_add_tags_interweaving_no_swaps():
    tags = [
        (3, 7, 'b'),
        (4, 8, 'c'),
    ]
    text_to_test = 'this is a string with over 10 chars'

    with pytest.raises(InvalidTagsError):
        add_tags(text_to_test, tags)


def test_add_tags_tag_out_of_bounds():
    tags = [
        (4, 100, 'c'),
    ]
    text_to_test = 'this is a string with over 10 chars'

    with pytest.raises(TagPositionOutOfBoundsError):
        add_tags(text_to_test, tags)


def test_add_tags_bad_tag_ordering():
    tags = [
        (7, 2, 'b'),
    ]
    text_to_test = 'this is a string with over 10 chars'

    with pytest.raises(ClosingTagBeforeOpeningTagError):
        add_tags(text_to_test, tags)
