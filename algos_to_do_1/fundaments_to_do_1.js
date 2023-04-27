// 1. Multiples of Three – but Not All
// Using FOR, print multiples of 3 from -300 to 0. Skip -3 and -6.

for(var i = -300; i <= 0; i++){
    if (i == -3 || i == -6){
        continue;
    }
    if (i % 3){
        continue;
    }
console.log(i)
}

// 2. Printing Integers with While
// Print integers from 2000 to 5280, using a WHILE.

var num = 2000;

while (num < 5281) {
    console.log (num);
    num++
}

// 3. Counting, the Dojo Way
// Print integers 1 to 100. If divisible by 5, print "Coding" instead. If by 10, also print " Dojo".

for (var i = 1;  i < 101; i++){
    if  (i % 5 == 0 && i % 10 == 0){
        console.log("Coding Dojo")
    }
    else if (i % 5 == 0){
        console.log("Coding")
    }
    else{
        console.log(i)
    }
}

// 4. Flexible Countdown
// Given lowNum, highNum, mult, print multiples of mult from highNum down to lowNum, using a FOR. For (2,9,3), print 9 6 3 (on successive lines)

function flexible_countdown(low_num, high_num, mult){
    for (var i = high_num; i >= low_num; i--) {
        if (i % mult == 0) {
            console.log(i)
        }
    }
}

flexible_countdown(2,9,3)
