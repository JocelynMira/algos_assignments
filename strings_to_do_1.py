### Remove Blanks ###
# Create a function that, given a string, returns all of that string’s contents, but without blanks. If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

def remove_blanks(string):
    #create empty variable to hold new string
    no_blank = ""
    # iterate through string
    for i in string:
        # if "i" isnt a blank space,
        if i != " ":
            # add "i" to no_blank variable
            no_blank += i
    return no_blank

print(remove_blanks(" Pl ayTha tF u nkyM usi c "))


### Get Digits ###
# Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.

def get_digits(string):
    just_digits = ""
    for i in string:
        if i.isdigit():
            just_digits += i
    return just_digits

print(get_digits("0s1a3y5w7h9a2t4?6!8?0"))


### Acronyms ###
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized)
# Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". Given "Live from New York, it's Saturday Night!", return "LFNYISN".

def acronyms(string):
    words = string.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(acronyms(" there's no free lunch - gotta pay yer way. "))

### Zip Arrays into Dictionary ###
# Dictionaries are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}

def zip_arrays(arr1, arr2):
    # create empty dictionary to put in the zipped array
    result = {}
    # iterate length of arr1 and add them to result and assign elements in arr2 as values
    for i in range(len(arr1)):
        result[arr1[i]] = arr2[i]
    return result

print(zip_arrays(["abc", 3, "yo"],[42, "wassup", "true"]))


### Invert Hash ###
# Dictionaries are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

def invert_hash(assocArr):
    result = {}
    for key, value in assocArr.items():
        result[value] = key
    return result

print(invert_hash({"name": "Zaphod", "charm": "high", "morals": "dicey"}))