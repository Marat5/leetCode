function addToSortedArr(sortedArr, num) {
    for(let i = 0; i < sortedArr.length; i++) {
        if(sortedArr[i] > num) {
            sortedArr.splice(i, 0, num);
            return;
        }
    }
    sortedArr.push(num);
}

function furthestBuilding(heights, bricks, ladders) {
    let min_heap = [];

    for (let i = 0; i < heights.length - 1; i++) {
        let diff = heights[i + 1] - heights[i];
        if (diff < 0) {
            continue;
        }

        addToSortedArr(min_heap, diff);

        if (min_heap.length > ladders) {
            let bricksNeeded = min_heap.shift();
            bricks -= bricksNeeded;
        }

        if (bricks < 0) {
            return i;
        }
    }

    return heights.length - 1;
}