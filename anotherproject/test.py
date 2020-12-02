from exampleproject import example
from exampleproject2 import example as example2
from json import load
from pkg_resources import resource_stream


if __name__=='__main__':
    print(example.get_zeros())

    json = load(resource_stream('exampleproject', 'data/some_data.json'))
    print(json['test'])

    print(example2.get_zeros())