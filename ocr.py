numbersDictionary = {
  ' _ | ||_|': '0',
  '     |  |': '1',
  ' _  _||_ ': '2',
  ' _  _| _|': '3',
  '   |_|  |': '4',
  ' _ |_  _|': '5',
  ' _ |_ |_|': '6',
  ' _   |  |': '7',
  ' _ |_||_|': '8',
  ' _ |_| _|': '9'
}

def returnNumberFromDictionary(passedLine):
  if passedLine in numbersDictionary:
    return numbersDictionary[passedLine]
  else:
    return '?'

def scan(input):
  account_number = ''
  lines = input.split('\n')[:3]
  char_at = 0
  characters_array = []
  for i in range(0, 9):
    default_string = ''

    # string_list = [
    #   line[char_at:char_at + 3] 
    #   for line in lines
    # ]
    # default_string ''.join(string_list)

    for line in lines:
      default_string += line[char_at:char_at + 3]
    char_at += 3
    characters_array.append(default_string)
    account_number += returnNumberFromDictionary(default_string)
  return account_number

def checkSum(acc_number):
  c = 0
  for i, n in enumerate(reversed(acc_number), start = 1):
    c += i * int(n)

  return c % 11 != 0

def validated_scan(input):
  scanned_number = scan(input)
  return checkSum(scanned_number)