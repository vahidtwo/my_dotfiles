# -*- coding: utf-8 -*-
import os
import tempfile
try:
    from ConfigParser import ConfigParser
    PY3 = False
except:
    from configparser import ConfigParser
    PY3 = True

__doc__ = """
:class:`~ConfigObject.ConfigObject` is a wrapper to the python ConfigParser_ to
allow to access sections/options with attribute names::

    >>> from ConfigObject import ConfigObject
    >>> config = ConfigObject()

    >>> config.section.value = 1

Values are stored as string::

    >>> config.section.value
    '1'

Values are returned as :class:`~ConfigObject.ConfigValue` to convert result to
other types::

    >>> config.section.value.as_int()
    1

Here is how list are stored::

    >>> config.section.value1 = list(range(2))
    >>> print(config.section.value1)
    0
    1
    >>> config.section.value1.as_list()
    ['0', '1']

You can use keys::

    >>> config['set']['value'] = 1
    >>> config['set']['value'].as_int()
    1

You can set a section as dict::

    >>> config.dict = dict(value=1, value2=['0', '1'])
    >>> config.dict.value.as_int()
    1
    >>> config.dict.value2.as_list()
    ['0', '1']

Update it::

    >>> config.dict.update(value2=[1, 2])
    >>> config.dict.value2.as_list()
    ['1', '2']

See what your section look like::

    >>> config['set']
    {'value': '1'}


Delete options::

    >>> del config['set'].value
    >>> config['set']
    {}

Playing with files::

    >>> filename=os.path.join(tempfile.gettempdir(), 'config.ini')
    >>> config = ConfigObject(filename=filename)
    >>> config.section = dict(value=1)
    >>> config.write()

    >>> config = ConfigObject(filename=filename)
    >>> config.section.value.as_int()
    1

::

    >>> os.remove(filename)

"""

__all__ = ('ConfigObject', 'config_module', 'Object')

class ConfigValue(str):

    def as_int(self):
        """convert value to int"""
        try:
            return int(self)
        except TypeError:
            raise TypeError('%s is not a valid int' % self)

    def as_float(self):
        """convert value to float"""
        try:
            return float(self)
        except TypeError:
            raise TypeError('%s is not a valid float' % self)

    def as_list(self, sep=None):
        """convert value to list::
            >>> config = ConfigObject()
            >>> config.listes = dict(liste=[0, 1], string='1;2;3')

            >>> print(config.listes.liste)
            0
            1
            >>> config.listes.liste.as_list()
            ['0', '1']
            >>> config.listes.string.as_list(sep=';')
            ['1', '2', '3']
        """
        if sep is None and '\n' in self:
            sep = '\n'
        return [ConfigValue(v) for v in self.split(sep) if v]

    def as_bool(self, true=True, false=False):
        """convert value to bool::

            >>> config = ConfigObject()
            >>> config.bools = dict(true=True, false=False)

            >>> config.bools.true
            'true'
            >>> config.bools.true.as_bool()
            True
            >>> config.bools.true.as_bool('on', 'off')
            'on'

            >>> config.bools.false
            'false'
            >>> config.bools.false.as_bool()
            False
            >>> config.bools.false.as_bool('on', 'off')
            'off'

            >>> config.bools.none.as_bool()
            False

        """
        if self.lower() in ('1', 'y', 'true', 'yes', 'on'):
            return true
        elif self.lower() in ('0', 'f', 'false', 'no', 'off'):
            return false
        elif not self:
            return false
        else:
            raise TypeError('%s is not a valid bool' % self)

    def __html__(self):
        return repr(self)


def _ConfigValue(value=''):
    """
        >>> _ConfigValue(1)
        '1'
        >>> _ConfigValue(.1)
        '0.1'
        >>> _ConfigValue(True)
        'true'
        >>> print(_ConfigValue(list(range(2))))
        0
        1
    """
    if value is True or value is False:
        value = value and 'true' or 'false'
    elif isinstance(value, set) or \
         isinstance(value, list) or \
         isinstance(value, tuple):
        value = '\n'.join([str(v) for v in value])
    return ConfigValue(value)

class ConfigDict(object):

    def __init__(self, parent, section):
        self.__parent = parent
        self.__section = section

    def __getattr__(self, attr, default=None):
        return self.get(attr, None)

    def __getitem__(self, attr):
        return self.get(attr, None)

    def get(self, attr, default=None):
        """dict api"""
        config = self.__parent
        section = self.__section
        if config.has_section(section) and config.has_option(section, attr):
            value = config.get(section, attr)
        else:
            value = default
        if value is None:
            value = _ConfigValue()
        elif not isinstance(value, ConfigValue):
            value = _ConfigValue(value)
        return value

    def __setattr__(self, attr, value):
        if attr.startswith('_ConfigDict__'):
            object.__setattr__(self, attr, value)
        else:
            self.__setitem__(attr, value)

    def __setitem__(self, attr, value):
        config = self.__parent
        if not config.has_section(self.__section):
            config.add_section(self.__section)
        if value is not None and not isinstance(value, ConfigValue):
            value = _ConfigValue(value)
        config.set(self.__section, attr, value)

    def __delattr__(self, attr):
        config = self.__parent
        if config.has_section(self.__section):
            if config.has_option(self.__section, attr):
                config.remove_option(self.__section, attr)

    __delitem__ = __delattr__

    def items(self):
        """dict api"""
        if self.__parent.has_section(self.__section):
            items = self.__parent.items(self.__section)
            return [(k, _ConfigValue(v)) for k, v in items]
        return []

    def keys(self):
        """dict api"""
        if self.__parent.has_section(self.__section):
            return self.__parent.options(self.__section)
        return []

    def update(self, *args, **kwargs):
        """dict api"""
        values = {}
        for arg in args:
            values.update(arg)
        values.update(kwargs)
        config = self.__parent
        if not config.has_section(self.__section):
            config.add_section(self.__section)
        for attr, value in values.items():
            if value is not None and not isinstance(value, ConfigValue):
                value = _ConfigValue(value)
            config.set(self.__section, attr, value)

    def __contains__(self, other):
        config = self.__parent
        section = self.__section
        if config.has_section(section) and config.has_option(section, other):
            return True
        return False

    def __repr__(self):
        return repr(dict(self.items()))

    __html__ = __repr__

class Object(dict):
    def __getattr__(self, attr):
        return self.get(attr)
    def __setattr__(self, attr, value):
        self[attr] = value


class ConfigObject(ConfigParser, object):
    """ConfigParser_ wrapper
    """

    def __init__(self, *args, **kwargs):
        self.__config = Object()
        self.filename = None
        if 'filename' in kwargs:
            self.filename = kwargs.pop('filename')
        ConfigParser.__init__(self, *args, **kwargs)
        if self.filename and os.path.isfile(self.filename):
            self.read(self.filename)

    def write(self, fd=None, space_around_delimiters=True):
        """Save to ``ConfigObject.filename`` if no fd is provided"""
        if fd is None:
            fd = open(self.filename, 'w')
            if PY3:
                ConfigParser.write(self, fd,
                    space_around_delimiters=space_around_delimiters)
            else:
                ConfigParser.write(self, fd)
            fd.close()
        else:
            if PY3:
                ConfigParser.write(self, fd,
                    space_around_delimiters=space_around_delimiters)
            else:
                ConfigParser.write(self, fd)

    def __getattr__(self, attr):
        return ConfigDict(self, attr)

    __getitem__ = __getattr__

    def __setattr__(self, attr, value):
        if attr.startswith('_') or isinstance(value, Object):
            object.__setattr__(self, attr, value)
        elif attr in ('default_section', 'filename'):
            object.__setattr__(self, attr, value)
        elif value:
            self.__setitem__(attr, value)

    def __setitem__(self, attr, value):
        if isinstance(value, dict):
            if not self.has_section(attr):
                self.add_section(attr)
            section = getattr(self, attr)
            for k, v in value.items():
                section[k] = v
        else:
            raise TypeError('Value must be a dict')

    def __delattr__(self, attr):
        if self.has_section(attr):
            self.remove_section(attr)

    __delitem__ = __delattr__

    def __contains__(self, other):
        if self.has_section(other):
            return True
        return False

    def __html__(self):
        return repr(self)

def config_module(name, file, *filenames, **defaults):
    """Allow to set a :class:`~ConfigObject.ConfigObject` as module. You have
    to add this to ``yourproject/config.py``:

    .. literalinclude:: ../ConfigObject/tests/config.py

    Then you are able to use ``from yourproject import config`` where
    ``config`` is the :class:`~ConfigObject.ConfigObject` itself.
    """
    config = ConfigObject(defaults=defaults)
    config.__name__ = name
    config.__file__ = file
    config.__path__ = file
    config.read(filenames)
    import sys
    sys.modules[name] = config
    return config


