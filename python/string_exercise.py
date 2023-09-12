# Create a new variable, that is a text to normalize.
value = 'homEwork: ' \
        'tHis iz your homeWork, copy these Text to variable. You NEED TO normalize it fROM letter CASEs point oF ' \
        'View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this ' \
        'Paragraph. it iZ misspeLLing here. fix “iZ” with correct “is”, but ONLY when it Iz a mistAKE. last iz TO ' \
        'calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I ' \
        'got 87. '

# Split text into smaller sentences.
parts = value.split('. ')

# Create two new lists. First on to save capitalize sentences. Second one to save a new sentence.
string_capitalize = []
new_sentence = []

for i in range(len(parts)):
    # Split each sentence to separate the last word.
    last_word = parts[i].split(" ")
    length = len(last_word)
    # Add the last word to the new_sentence list.
    new_sentence.append(last_word[length - 1])
    # Add capitalize sentence to string_capitalize list.
    string_capitalize.append(parts[i].capitalize())

# Join all words from new_sentence list to create one string.
string_one = ' '.join(new_sentence).capitalize()

# Join all words from string_capitalize list to create one string.
string_two = '. '.join(string_capitalize)

# Replace word 'iz' with the word 'is' to correct all mistakes.
string_two = string_two.replace(' iz ', ' is ')

# Join both strings together to create final text.
text = string_two + string_one


# Method to count spaces in the text.
def check_space(string):
    count = 0
    for i in string:
        if i.isspace():
            count += 1
    return count


# Print final text and number of spaces.
print(text)
print('Number of spaces in the text: ', check_space(text))
