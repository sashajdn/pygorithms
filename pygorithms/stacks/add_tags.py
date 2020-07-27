import bisect

from functools import total_ordering
from typing import Generator, List, Tuple


def add_tags(text: str, tags: List[Tuple[int, int, str]]) -> str:
    """
    Process:
        1. Build a sorted list of opening and closing tags.
           This is done using binary search (bisect) to insert
           into a list at a given position. Inserting right for
           opening and left for closing tags

           This will have a complexity O(n), since inserting causes in the
           worst case having to shift all ``n`` elements in the list, where ``n``
           is the length of the list.

           Since this is done k * 2 times, where ``k`` is the number of tags
           (opening & closing counted as 1),
           therefore will be O(nk) where n=k. Therefore O(k**2)

           With the space complexity being O(k). This couldn't be done in place
           without mutating the argument and with a different data structure at that

           But this is an area for improvement since I probably could have
           wrote a better sorting algorithm. I had to write one since it was the
           best place to include raising exceptions. But one that springs to
           mind is merge sort, using a key=`lambda tag: (tag[0], tag[1])` to retain
           the original positioning - this is what I did with the
           insort_left and insort_right effectively.

        2. The next step is to validate the tags. This is done using a Stack.
           Again the Time complexity here will be O(k), since it's a regular
           iteration. Again where k is the number of `tags`.

           The Space Complexity will be at worst case O(k), where by no tags are
           matched, and hence all pushed to the stack

        3. Finally there is merger between the list of tags and the
           text, length m. This is also with Time Complexity O(k), since the iteration
           is over the tags, and not the text itself.

           And since it's a generator function will itself not require extra space,
           giving it a Space Complexity of O(1)

        4. This is wrapped up by building a new string, which does require Space O(m + k)
           whereby m is the length of the text and k the number of tags,
           but no time
           since it builds from another generator, therefore O(1)

    Complexity:

        Time:
            O(k**2)

        Space:
            O(m + k)

    Comments:

    O(k**2) does sounds rather steep, but i'd assume in most cases n >> k, where n
    is the length of the text body. Improvements probably could have been made by
    combining a few of the functions, but that also leads into how well the code reads.

    In particular I'm not happy with how the swapping mechanism works. I think this logic
    should lie further up the chain. Whilst the finding indexes to swap and returing
    them isn't a pattern I've used before - so I was hesistant, but hey it works,
    and avoids another loop.

    Similarly in a production setting, the exceptions, helper classes and functions
    would also be moved out into their own separate modules.

    And likewise with some of the naming conventions for some of the args.
    Eg o, c and i and especially Tag.val - it should be Tag.index!

    But all in all a really good challenge!
    """
    sorted_tags = _sort_with_bounds_check(tags, bounds_size=len(text))
    is_valid, swaps_to_make = _validate_and_find_swaps(sorted_tags)

    if not is_valid:
        raise InvalidTagsError

    for swap in swaps_to_make:
        inplace_swap(sequence=sorted_tags, to_swap=swap)

    return ''.join(val for val in _merge_and_stringify(text, sorted_tags))


# Helper Classes
@total_ordering
class Tag:
    def __init__(self, *, val: int, tag:  str):
        self.tag = tag
        self._val = val

    @property
    def val(self):
        return self._val

    def __eq__(self, other):
        return self.val == other

    def __lt__(self, other):
        return self.val < other


class Open(Tag):
    def __str__(self):
        return f'<{self.tag}>'


class Closed(Tag):
    def __str__(self):
        return f'</{self.tag}>'


# Exceptions
class InvalidTagsError(Exception):
    pass


class TagPositionOutOfBoundsError(Exception):
    pass


class ClosingTagBeforeOpeningTagError(Exception):
    pass


# Util
def inplace_swap(*, sequence: List, to_swap: Tuple[int, int]) -> None:
    i, j = to_swap
    sequence[i], sequence[j] = sequence[j], sequence[i]


# Internal (Private) Functions
def _validate_bounds(*args, size: int):
    return all(0 <= arg <= size for arg in args)


def _sort_with_bounds_check(
    tags: List[Tuple[int, int, str]], bounds_size: int
) -> List[Tag]:

    sorted_tags: List[Tag] = []

    for tag in tags:
        o, c, t = tag  # open, close, tag
        if o >= c:
            raise ClosingTagBeforeOpeningTagError(
                f"opening: {o}, closing: {c}"
            )

        if not _validate_bounds(o, c, size=bounds_size):
            raise TagPositionOutOfBoundsError(
                f"Tags: {o}, {c} out of bounds: {bounds_size}"
            )

        bisect.insort_right(sorted_tags, Open(val=o, tag=t))
        bisect.insort_left(sorted_tags, Closed(val=c, tag=t))

    return sorted_tags


def _validate_and_find_swaps(sorted_tags: List) -> Tuple[bool, List]:
    stack: List[Tag] = []
    swaps_to_make: List[Tuple[int, int]] = []

    for i, tag in enumerate(sorted_tags):
        if isinstance(tag, Open):
            stack.append(tag)

        elif isinstance(tag, Closed):
            if len(stack) == 0:
                return False, swaps_to_make

            if tag.tag == stack[-1].tag:
                stack.pop()

            else:
                if len(stack) >= 2:
                    if stack[-1].val == stack[-2].val:
                        if tag.tag == stack[-2].tag:
                            swaps_to_make.append((i-1, i-2))
                            to_push = stack.pop()  # reorder stack
                            stack.pop()
                            stack.append(to_push)
                            continue

                return False, swaps_to_make

    return True, swaps_to_make


def _merge_and_stringify(
    text: str, sorted_tags: List[Tag]
) -> Generator[str, None, None]:

    current_idx = 0
    for tag in sorted_tags:
        yield from text[current_idx:tag.val]
        current_idx = tag.val
        yield str(tag)

    yield from text[current_idx:]
