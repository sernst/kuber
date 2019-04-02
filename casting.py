import typing

class Foo:
    pass


class Bar(Foo):

    def __init__(self):
        self.barvar = 2

class Baz(Foo):
    pass


def create(kind: str) -> typing.Any:
    choices = {'bar': Bar, 'baz': Baz}
    return choices[kind]()


# bar: Bar = create('bar')  # type: ignore
# bar: Bar = create('bar')  # cast: Bar
bar: Bar = typing.cast(Bar, create('bar'))
# bar_3: Bar = create('bar') as
bar.barvar
