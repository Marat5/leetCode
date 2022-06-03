/**
 * @param {number[][]} matrix
 */

var NumMatrix = function(matrix) {
    this.dp = Array(matrix.length + 1).fill().map(() => Array(matrix[0].length + 1).fill(0));

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            this.dp[i + 1][j + 1] = this.dp[i + 1][j] + this.dp[i][j + 1] + matrix[i][j] - this.dp[i][j];
        }
    }
};

/** 
 * @param {number} row1 
 * @param {number} col1 
 * @param {number} row2 
 * @param {number} col2
 * @return {number}
 */
NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
    return this.dp[row2 + 1][col2 + 1] - this.dp[row1][col2 + 1] - this.dp[row2 + 1][col1] + this.dp[row1][col1];
};

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */


// This solution makes dp same size as the matrix (above it's 1 elem wider and 1 elem higher)
// But we have to handle 3 extra cases both in constructor and in sumRegion function
// So the above solution is cleaner

// var NumMatrix = function(matrix) {
//     this.dp = Array(matrix.length).fill().map(() => Array(matrix[0].length).fill(0));

//     for (let i = 0; i < matrix.length; i++) {
//         for (let j = 0; j < matrix[0].length; j++) {
//             if (i === 0 && j === 0) {
//                 this.dp[i][j] = matrix[i][j];
//             } else if (i === 0) {
//                 this.dp[i][j] = this.dp[i][j - 1] + matrix[i][j];
//             } else if (j === 0) {
//                 this.dp[i][j] = this.dp[i - 1][j] + matrix[i][j];
//             } else {
//                 this.dp[i][j] = this.dp[i - 1][j] + this.dp[i][j - 1] + matrix[i][j] - this.dp[i - 1][j - 1];
//             }
//         }
//     }
// };

// NumMatrix.prototype.sumRegion = function(row1, col1, row2, col2) {
//     if (row1 === 0 && col1 === 0) {
//         return this.dp[row2][col2];
//     } else if (row1 === 0) {
//         return this.dp[row2][col2] - this.dp[row2][col1 - 1];
//     } else if (col1 === 0) {
//         return this.dp[row2][col2] - this.dp[row1 - 1][col2];
//     } else {
//         return this.dp[row2][col2] - this.dp[row1 - 1][col2] - this.dp[row2][col1 - 1] + this.dp[row1 - 1][col1 - 1];
//     }
// };

var obj = new NumMatrix([[1,2,3], [1,2,3], [1,2,3]]);
var param_1 = obj.sumRegion(0,0,2,2);

console.log(param_1);