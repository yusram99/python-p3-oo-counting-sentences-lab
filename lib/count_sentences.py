#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")
    
    @property
    def value(self):
        return self._value
    
    def is_sentence(self):
        return self._value.endswith('.')
    
    def is_question(self):
        return self._value.endswith('?')
    
    def is_exclamation(self):
        return self._value.endswith('!')
    
    def count_sentences(self):
        modified_value = self._value.replace('.', '. ').replace('?', '? ').replace('!', '! ')
        segments = modified_value.split()
        return len([segment for segment in segments if segment.strip()])

      
