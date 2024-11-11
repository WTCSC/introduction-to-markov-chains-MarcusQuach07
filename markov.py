import random
import string

"""
Create the sample text and the dictionary to store word transitions

TODO: Replace the sample text with a larger text for more interesting results
"""
text = "Le cadre d’un palabre n’augmente guère le faste royal de la cour d’Anno. Le public est plus nombreux cependant, et c’est un peu plus original, la parole n’étant portée que par les porte-canne, sorte de factotums qui ont en main une canne sculptée et ne font que répéter les paroles du roi ou des intéressés qui viennent solliciter une mission ou en rendre compte. Dans ces palabres souvent il y a aussi des individus faisant fonction d’huissiers : ils indiquent les places à occuper par les assistants, leur font donner des tabourets, en un mot s’occupent de l’ordre des préséances, etc. ; on reconnaît ces individus à une tête de singe qu’ils portent suspendue au cou : c’est la chaîne de nos huissiers."
transitions = {}

"""
Build the Markov Chain

1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions

TODO: Handle punctuation and capitalization for better results
"""
words = text.split()
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)
"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:

1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string

TODO: Clean up the generated text for better formatting and readability,
e.g., capitalization, punctuation, line breaks, etc.
"""
def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word]
    
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            result.append(next_word)
            current_word = next_word
        else:
            break
    
    # Join the words into a single string and capitalize the first word
    generated_text = " ".join(result)
    generated_text = generated_text[0].upper() + generated_text[1:]  # Capitalize the first letter

    # Add punctuation at the end (a basic approach)
    if generated_text[-1] not in string.punctuation:
        generated_text += "."

    return generated_text


"""
Example usage, generating 10 words starting with "Mary"

TODO: Accept user input for the starting word and number of words to generate
"""
input_word = input("Enter a word: ").strip()
number_of_words = int(input("Enter number of words to generate: "))
print(generate_text(input_word, number_of_words))
