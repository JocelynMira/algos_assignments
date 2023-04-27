// 1. Countdown
// Create a function that accepts a number as an input. Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). How long is this array?

function countdown(num){
    array = [];
    for (var i = num; i >= 0; i--){
        array.push(i);
    }
    return array;
}
array = countdown(5);

console.log(array)

// 2. First Plus Length
// Given an array, return the sum of the first value in the array, plus the array’s length. What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

function first_plus_len(array){
    if (typeof array[0] != 'number'){
        return "Not a number!"
    }
    sum = array[0] + array.length;
    return sum
}

console.log(first_plus_len([2,3,1,6]))

// 3. Values Greater than Second
// For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

function greater_than_second(array){
    num_count = 0
    for (var i = 0; i < array.length; i++){
        if (array[i] > array[1]){
            num_count ++;
            console.log(array[i]);
        }
    }
    return 'Count is '+ num_count;
}

console.log(greater_than_second([4, 3, 1, 0, 7, 2, 9, 6]))


// 4. Values Greater than Second, Generalized
// Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. Print how many values this is. What will you do if the array is only one element long?

function gen_greater_than_second(array){
    if (array.length < 2){
        return "Array is too short!"
    }
    new_array = [];
    count = 0;
    for (var i = 0; i < array.length; i++){
        if (array[i] > array[1]) {
            count ++;
            new_array.push(array[i])
        }
    }
    console.log(new_array);
    return "Count is " + count;
}

console.log(gen_greater_than_second([24, 10, 9, 12]))


// 5. This Length, That Value
// Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

function this_that(num1,num2){
    if (num1 === num2){
        return "Jinx!"
    }
    result = []
    for (var i = 0; i < num1; i++){
        result.push(num2)
    }
    return result
}

console.log(this_that(4,2))


// 6. Fit the First Value
// Your function should accept an array. If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

function fit_the_first(array){
        if (array[0] > array.length){
            console.log("Too Big!");
        }
        else if (array[0] < array.length){
            console.log ("Too Small!");
        }
        else {
            console.log("Just Right!");
        }
    }


fit_the_first([5, 2, 3, 9, 29])


// 7. Fahrenheit to Celsius
// Kelvin wants to convert between temperature scales. Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit and returns the equivalent temperature as expressed in Celsius degrees. For review, Fahrenheit = (9/5 * Celsius) + 32.

function fahrenheitToCelsius(fahrenheit){
    celsius = (fahrenheit - 32) * 5/9;
    return celsius
}

console.log(fahrenheitToCelsius(60))