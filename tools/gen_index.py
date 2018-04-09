from os import listdir, getcwd, chdir
from contextlib import contextmanager
from re import compile as comp

roteiros = 'roteiros'
regex = comp(r'(#|#{2}|#{3}|#{4}) (\d\d?\.\d?\.?\d?) (.+)')


@contextmanager
def cd(_dir):
    old_dir = getcwd()
    chdir(_dir)
    yield
    chdir(old_dir)


@cd('{}/roteiros'.format(getcwd()))
def read_file(_file):
    with open(_file) as md:
        return regex.findall(md.read())


def order(val):
    for x in sorted(val):
        yield from x


def write(_file, _dir):
    with open(_file, 'w') as md:
        for x in order([read_file(el) for el in listdir(_dir)]):
            md.writelines('#### {} {}\n'.format(x[1], x[2]))


write('sumario.md', roteiros)
