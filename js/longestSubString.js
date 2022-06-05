/**
 * @param {string} s
 * @return {number}
 */

// Initial brute force solution
// let substringLength = (s) => {
//     let count = 0;
//     s.split("").some((char, index) => {
//         let usedChars = s.slice(0, index);
//         if (usedChars.includes(char)) {
//             return true;
//         } else {
//             count++;
//         }
//     });

//     return count;
// }

//  var lengthOfLongestSubstring = function(s) {
//      let maxLength = 0;
//     s.split("").forEach((char, index) => {
//         let length = substringLength(s.slice(index));
//         maxLength = Math.max(length, maxLength);
//     });
//     return maxLength;
// };

// Sliding window
// var lengthOfLongestSubstring = function(s) {
//     let chars = Array(128).fill(0);
//     let left = 0;
//     let right = 0;

//     let res = 0;
//     while (right < s.length) {
//         r = s[right];
//         chars[r.charCodeAt(0)] += 1;
//         while (chars[r.charCodeAt(0)] > 1) {
//             l = s[left];
//             chars[l.charCodeAt(0)] -= 1;
//             left += 1;
//         }

//         res = Math.max(res, right - left + 1);
//         right += 1;
//     }
//     return res;
// }

// Optimized sliding window
// var lengthOfLongestSubstring = function(s) {
//     let chars = Array(128).fill(null);
//     let left = 0;
//     let right = 0;

//     let res = 0;
//     while (right < s.length) {
//         r = s[right];
//         index = chars[r.charCodeAt(0)];
//         if (index !== null && index >= left && index < right) {
//             left = index + 1;
//         }

//         res = Math.max(res, right - left + 1);
//         chars[r.charCodeAt(0)] = right;
//         right += 1;
//     }
//     return res;
// }

// Just another version of optimized sliding window
var lengthOfLongestSubstring = function(s) {
    const chars = {};
    let left = 0;
    let right = 0;
    let res = 0;

    while (right < s.length) {
        const rightChar = s[right];
        // Last right char index in string before the current right
        const index = chars[rightChar];

        if (index !== undefined && index >=left && index < right) {
            left = index + 1;
        }
        chars[rightChar] = right;
        res = Math.max(res, right - left + 1);
        right++;
    }
    return res;
}


let res = lengthOfLongestSubstring("abcabcbb");
console.log(res);