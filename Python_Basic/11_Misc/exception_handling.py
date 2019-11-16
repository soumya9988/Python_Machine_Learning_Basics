class ShortExceptionError(Exception):
    def __init__(self, length):
        Exception.__init__(self)
        self.length = length


try:
    name = input('Enter your name..')
    if len(name) < 3:
        raise ShortExceptionError(len(name))
except EOFError:
    print('\nOhh EoF.. Enter name to avoid hard stop error!!')
except KeyboardInterrupt:
    print('\nKey board interruption. Enter name to avoid hard stop error!!')
except ShortExceptionError as e:
    print('The name is too short(%d letters only) to be printed.' % e.length)
else:
    print('\nHello %s' % name)
finally:
    print('cleaning up...')
