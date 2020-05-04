from collections import abc

head = lambda x: x[0]
tail = lambda x: x[1:]
is_atom = lambda a: not(isinstance(a, abc.Sequence) and not isinstance(a, str))
cons = lambda x, y: [x] + y


def spiral_traversal(data):
    if len(data) == 0:
        return []

    return head(data) + spiral_traversal(
        list(reversed(
            list(zip(
                *tail(data)
            ))
        ))
    )
