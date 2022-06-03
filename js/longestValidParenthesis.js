/**
 * @param {string} s
 * @return {number}
 */


// Brute Force

// let validLineLength = (arr) => {
//     let openArr = [];
//     let fallbackCount = 0;
//     let count = 0;

//     const isAllArrCorrect = arr.every(char => {
//         if (!openArr.length) {
//             fallbackCount = count;
//         }

//         if (char === "(") {
//             openArr.push(char);
//             count++;
//             return true;
//         } else if (openArr.length) {
//             openArr.pop();
//             count++;
//             return true;
//         } else {
//             return false;
//         }
//     }) && openArr.length === 0;

//     return isAllArrCorrect ? count : fallbackCount;
// }

// var longestValidParentheses = function(s) {
//     const arr = s.split("");
//     let longest = 0;
//     arr.forEach((char, index) => {
//         if (char === "(") {
//             const length = validLineLength(arr.slice(index));
//             if (length > longest) {
//                 longest = length;
//             }
//         }
//     })

//     return longest;
// };




// Stack Solution

// var longestValidParentheses = function(s) {
//     const stack = [-1];
//     let maxLength = 0;

//     s.split("").forEach((char, index) => {
//         if (char === "(") {
//             stack.push(index);
//         } else {
//             stack.pop();

//             if (!stack.length) {
//                 stack.push(index);
//             } else {
//                 maxLength = Math.max(maxLength, index - stack[stack.length - 1]);
//             }
//         }
//     });

//     return maxLength;
// };




// No extra space

var longestValidParentheses = function(s) {
    let left = 0;
    let right = 0;

    let arr = s.split("");
    let maxLength = 0;

    arr.forEach(char => {
        if (char === "(") {
            left++;
        } else {
            right++;
        }

        if (left === right) {
            maxLength = Math.max(maxLength, left + right);
        } else if (right > left) {
            left = 0;
            right = 0;
        }
    });

    left = 0;
    right = 0;

    for (let i = arr.length - 1; i>=0; i--) {
        let char = arr[i];

        if (char === ")") {
            right++;
        } else {
            left++;
        }

        if (left === right) {
            maxLength = Math.max(maxLength, left + right);
        } else if (left > right) {
            left = 0;
            right = 0;
        }
    }

    return maxLength;
};




// Dynamic programming

// var longestValidParentheses = function(s) {
//     let maxLength = 0;
//     let arr = s.split("");
//     const dp = [];

//     arr.forEach((char, index) => {
//         if (index === 0) {
//             dp.push(0);
//             return;
//         };

//         if (char === ")") {
//             if (arr[index - 1] === "(") {
//                 if (index < 2) {
//                     dp.push(2);
//                 } else {
//                     dp.push(dp[index - 2] + 2);
//                 }
//             } else {
//                 if (arr[index - dp[index - 1] - 1] === "(") {
//                     console.log('fuckup', dp, index);
//                     let prevValidSubstringIndex = index - dp[index - 1] - 2;
//                     if (prevValidSubstringIndex > 0) {
//                         dp.push(dp[index - 1] + dp[prevValidSubstringIndex] + 2);
//                     } else {
//                         dp.push(dp[index - 1] + 2);
//                     }
//                 } else {
//                     dp.push(0);
//                 }
//             }
//         } else {
//             dp.push(0);
//         }

//         maxLength = Math.max(maxLength, dp[index]);
//     });

//     return maxLength;
// };


console.log("Answer:", longestValidParentheses("(()())"));