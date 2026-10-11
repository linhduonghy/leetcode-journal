/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

 var solution = function(isBadVersion: any) {

    return function(n: number): number {
        let l = 1, r = n;
        let result = n;
        while (l <= r) {
            let mid = Math.floor((l + r) / 2);
            
            if (isBadVersion(mid)) {
                result = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        return result;
    };
};