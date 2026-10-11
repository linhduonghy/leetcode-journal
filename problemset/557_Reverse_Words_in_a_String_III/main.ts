function reverseWords(s: string): string {
    
    let sa: string[] = s.split(" ");
    
    for (let i = 0; i < sa.length; ++i) {
        sa[i] = reverseString(sa[i]);
        // sa[i] = [...s].reverse().join("");
    }
    
    return sa.join(" ");
};

function reverseString(s: string) : string {
    
    let arr = [...s];
    let end = arr.length - 1;
    for (let start = 0; start <= end; ++start, --end) {
        let temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
    }
    return arr.join("");
}
