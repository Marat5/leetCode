/**
 * @param {number[][]} courses
 * @return {number}
 */

// Brute force
// Fails because of time limit
// const permutator = (inputArr) => {
//     let result = [];

//     const permute = (arr, m = []) => {
//         if (arr.length === 0) {
//         result.push(m)
//         } else {
//         for (let i = 0; i < arr.length; i++) {
//             let curr = arr.slice();
//             let next = curr.splice(i, 1);
//             permute(curr.slice(), m.concat(next))
//         }
//         }
//     }

//     permute(inputArr)

//     return result;
// }

// var scheduleCourse = function(courses) {
//     let allOptions = permutator(courses);
//     let bestResult = 0;
//     allOptions.forEach(option => {
//         let currentDay = 0;
//         let resultPerPermutation = 0;

//         option.forEach(([d, e]) => {
//             if (currentDay + d <= e) {
//                 currentDay += d;
//                 resultPerPermutation++;
//             }
//         });
//         bestResult = Math.max(bestResult, resultPerPermutation);
//     });

//     return bestResult;
// };


// Recursion/Memo
// Fails because of stack overflow
// const schedule = (courses, i, time, memo) => {
//     if (i === courses.length) {
//         return 0;
//     }

//     if (memo[i] && memo[i][time]) {
//         return memo[i][time];
//     }

//     let taken = 0;
//     if (time + courses[i][0] <= courses[i][1]) {
//         taken = 1 + schedule(courses, i + 1, time + courses[i][0], memo);
//     }
//     let not_taken = schedule(courses, i + 1, time, memo);

//     if (!memo[i]) {
//         memo[i] = {};
//     }
//     memo[i][time] = Math.max(taken, not_taken);

//     return memo[i][time];
// }

// var scheduleCourse = function(courses) {
//     courses.sort(([d1, e1], [d2, e2]) => e1 - e2);
//     let memo = {};
//     return schedule(courses, 0, 0, memo);
// }


// Iterative
// Accepted
// var scheduleCourse = function(courses) {
//     courses.sort(([d1, e1], [d2, e2]) => e1 - e2);

//     let taken = 0;
//     let time = 0;

//     courses.forEach(([duration, end], i) => {

//         if (time + duration <= end) {
//             taken++;
//             time += duration;
//         } else {
//             let max_i = i;
//             for (let j = 0; j < i; j++) {
//                 if (courses[j][0] > courses[max_i][0]) {
//                     max_i = j;
//                 }
//             }

//             if (courses[max_i][0] > courses[i][0]) {
//                 time -= courses[max_i][0] - courses[i][0];
//             }

//             // Means this course was not taken
//             courses[max_i][0] = 0;
//         }
//     });
    
//     return taken;
// }



// Iterative optimized
// var scheduleCourse = function(courses) {
//     courses.sort(([d1, e1], [d2, e2]) => e1 - e2);

//     let taken = 0;
//     let time = 0;

//     courses.forEach(([duration, end], i) => {
//         if (time + duration <= end) {
//             courses[taken] = [duration, end];
//             taken++;
//             time += duration;
//         } else {
//             let max_i = i;
//             for (let j = 0; j < taken; j++) {
//                 if (courses[j][0] > courses[max_i][0]) {
//                     max_i = j;
//                 }
//             }

//             if (courses[max_i][0] > courses[i][0]) {
//                 time -= courses[max_i][0] - courses[i][0];
//                 courses[max_i] = courses[i];
//             }
//         }
//     });
    
//     return taken;
// }

// Extra list
// Just like iterative optimized, but with extra list instead of mutating input array
// var scheduleCourse = function(courses) {
//     courses.sort(([d1, e1], [d2, e2]) => e1 - e2);

//     const takenCourses = [];
//     let time = 0;

//     courses.forEach(([duration, end], i) => {
//         if (time + duration <= end) {
//             takenCourses.push([duration, end]);
//             time += duration;
//         } else {
//             let longestDuration = 0;
//             let longestDurationIndex = -1;
//             takenCourses.forEach(([duration, end], j) => {
//                 if (duration > longestDuration) {
//                     longestDuration = duration;
//                     longestDurationIndex = j;
//                 }
//             });

//             if (longestDuration && longestDuration > duration) {
//                 time -= longestDuration - duration;
//                 takenCourses[longestDurationIndex] = courses[i];
//             }
//         }
//     });
    
//     return takenCourses.length;
// }


// Priority queue
function addToSortedArr(sortedArr, num) {
    for(let i = 0; i < sortedArr.length; i++) {
        if(sortedArr[i] > num) {
            sortedArr.splice(i, 0, num);
            return;
        }
    }
    sortedArr.push(num);
}

var scheduleCourse = function(courses) {
    courses.sort(([d1, e1], [d2, e2]) => e1 - e2);

    let sortedDurationsOfTakenCourses = [];
    let time = 0;

    courses.forEach(([duration, end]) => {
        if (time + duration <= end) {
            addToSortedArr(sortedDurationsOfTakenCourses, duration);
            time += duration;
        } else {
            if (sortedDurationsOfTakenCourses[sortedDurationsOfTakenCourses.length - 1] > duration) {
                let longestDuration = sortedDurationsOfTakenCourses.pop();
                addToSortedArr(sortedDurationsOfTakenCourses, duration);
                time -= longestDuration - duration;
            }
        }
    });
    return sortedDurationsOfTakenCourses.length;
}

// console.log(scheduleCourse([[1,2],[2,3]]));
// console.log(scheduleCourse([[5,5],[4,6],[2,6]]));
// console.log(scheduleCourse([[100,200],[200,1300],[1000,1250],[2000,3200]]));
// console.log(scheduleCourse([[7,16],[2,3],[3,12],[3,14],[10,19],[10,16],[6,8],[6,11],[3,13],[6,16]]));
// console.log(scheduleCourse([[3,2],[4,3]]));
console.log(scheduleCourse([[7,17],[3,12],[10,20],[9,10],[5,20],[10,19],[4,18]]))