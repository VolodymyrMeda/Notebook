import notebook


def notebook_researching(obj):
    '''
    Researching of the Notebook class
    '''
    print(obj)
    print('\n')

    print('Attributes and methods of Notebook instance:')
    print(dir(obj))
    print('\n')
    print('Attributes and methods of Notebook instance method:')
    print(dir(obj.new_note('hello')))
    print('\n')
    print('Attributes and methods of the attribute:')
    print(dir(obj.notes))
    print('\n')

    print('Isinstance func shows that instance of the class and the method '
          'of the class are objects (actually, everything is an object): ')
    print(isinstance(obj, object))
    print(isinstance(obj.new_note('hello'), object))
    print(isinstance(obj.__init__(), object))
    print(isinstance(obj.notes, object))
    print('\n')

    print('Init and str methods have their attributes too: ')
    print(dir(obj.__init__()))
    print(dir(obj.__str__()))


if __name__ == '__main__':
    obj = notebook.Notebook()
    notebook_researching(obj)
