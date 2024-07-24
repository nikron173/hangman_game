__all__ = ["hangman_ascii_list"]
stage_1 = '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
stage_2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
'''
stage_3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
'''
stage_4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
'''
stage_5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
'''
stage_6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''

hangman_ascii_list = [stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]
