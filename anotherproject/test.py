from exampleproject import example
from json import load
from pkg_resources import resource_stream

if __name__=='__main__':
    print(example.get_zeros())

    json = load(resource_stream('exampleproject', 'data/some_data.json'))
    print(json['test'])