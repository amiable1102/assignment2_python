def counter(fname):
   num_lines = 0
   num_words = 0
   num_letters = 0
   with open(fname,'r') as f:
       for line in f:
           num_lines += 1
           wor = 'Y'
           for word in line:
               if (word != ' ' and wor == 'Y'):
                   wor = 'N'
                   num_words += 1
               elif (word == ' '):
                   wor = 'Y'
               for chr in word:
                   if (chr != " " and chr != "\n"):
                       num_letters += 1
   print("total number of lines are: ", num_lines)
   print("total number of words are: ", num_words)
   print("total number of characters are: ", num_letters)

if __name__ == '__main__':
   fname = 'sampleText.txt'
   counter(fname)
