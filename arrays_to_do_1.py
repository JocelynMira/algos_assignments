### Shuffle ###
# In JavaScript, the Array object has numerous useful methods. It does not, however, contain a method that will randomize the order of an array’s elements. Let’s create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?


import random

def shuffle(arr):
    for i in range(len(arr)):
        # randomize number between 0 and length of arr -1
        rand_num = random.randint(0,len(arr)-1)
        # make a temp variable to hold the element value for i
        temp = arr[i]
        # swap the element with rand_num
        arr[i] = arr[rand_num]
        arr[rand_num] = temp
    return arr

print(shuffle([3, 7, 47, -2, 4, 90]))



### Skyline Heights ###
# Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are given an array with heights of consecutive buildings, starting closest to you and extending away. Array [-1,7,3] would represent three buildings: first is actually out of view below street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind the 7-story). You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().

def heights(list):
    # create empty list to add all visible buildings
    visible = []
    # iterate through list 
    for i in list:
        # if there isnt anything in the list, 
        if len(visible) == 0:
            # and building is above ground (i > 0),
            if i > 0:
                # append building in visible list
                visible.append(i)
        # if there are buildings in visible list,
        if len(visible) > 0:
            # if building is above ground and not in visible list,
            if i > 0 and i not in visible:
                # if building is taller than the last listed
                if i > visible[-1]:
                    # add to list
                    visible.append(i)
    return visible

print(heights([-4, 1, 2, 7, 9, 13, 11]))

### Zip It ###
# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100]

def zipit(arr1, arr2):
    zipped = []
    for i in range(max(len(arr1), len(arr2))):
        if i <= len(arr1)-1:
            zipped.append(arr1[i])
        if i <= len(arr2)-1:
            zipped.append(arr2[i])
    return zipped

print(zipit([2,10,34,1],[3,8,1,39]))

