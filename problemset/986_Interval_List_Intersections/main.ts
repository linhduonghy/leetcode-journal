function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {

    let result = [];
    let i = 0, j = 0;
    while (i < firstList.length && j < secondList.length) {
        if (firstList[i][1] < secondList[j][0]) {
            // console.log(1, i, j);
            ++i;
        } else if (secondList[j][1] < firstList[i][0]) {
            // console.log(2, i, j);
            ++j;
        } else if (firstList[i][1] < secondList[j][1]) {
            // console.log(3, i, j);
            if (firstList[i][0] > secondList[j][0]) {
                result.push([firstList[i][0], firstList[i][1]]);
            } else {
                result.push([secondList[j][0], firstList[i][1]]);
            }
            ++i;
        } else if (firstList[i][1] > secondList[j][1]) {
            // console.log(4, i, j);
            if (firstList[i][0] > secondList[j][0]) {
                result.push([firstList[i][0], secondList[j][1]]);
            } else {
                result.push([secondList[j][0], secondList[j][1]]);
            }
            ++j;
        } else if (firstList[i][1] == secondList[j][1]) {
            // console.log(5, i, j);
            if (firstList[i][0] > secondList[j][0]) {
                result.push([firstList[i][0], firstList[i][1]]);
                ++i;
            } else {
                result.push([secondList[j][0], secondList[j][1]]);
                ++j;
            }
        }
    }
    return result;
};