from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(caesar_text, caesar_shift, caesar_direction):

  index = []
  cipher = []

  caesar_text_list = list(caesar_text)

  if caesar_direction == "encode":
    for x in caesar_text_list:
        index.append(alphabet.index(x) + caesar_shift)
  
  elif caesar_direction == "decode":
    for x in caesar_text_list:
        index.append(alphabet.index(x) - caesar_shift)

  for y in index:
    if y >= 26:
      y = y - 26
      cipher.append(alphabet[y])
    else:
      cipher.append(alphabet[y])

  cipher = ''.join(cipher)
  print(f"The {caesar_direction}d text is {cipher}.")

end_program = False
while not end_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)

  restart = input("Would you like to restart the program? Enter Yes or No. ").lower()

  if restart == "no":
    end_program = True
    print("This is the end of the program.")