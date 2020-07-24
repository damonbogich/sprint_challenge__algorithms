'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #set 'th' to variable
    counter = 0
    th = 'th'
    #base case? word has no instances of 'th'
    if word.find(th) == -1:
        return counter
    if word.find(th) != -1:
        #set variable to index of t
        counter += 1
        starting_index = word.find(th)
        #change word by getting rid of every index
        #through starting_index + 1
        new_word = word[starting_index + 2:]
        result = counter + count_th(new_word)
        # return result
        
    return result
