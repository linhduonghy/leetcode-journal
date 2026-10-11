
// build Stack
class Stack<T> {

    private _top;

    constructor() {
        this._top = null;
    }

    public push(s: T) {
        let node = {
            data: s,
            next: null
        }
        // push node -> first node
        node.next = this._top;
        this._top = node;
    }

    public pop(): T {
        if (this._top == null) {
            return null;
        }
        let data: T = this._top.data;
        this._top = this._top.next;

        return data;
    }

    public isEmpty(): boolean {
        return this._top == null ? true : false;
    }
}

function isValid(s: string): boolean {

    let stack: Stack<string> = new Stack<string>();

    for (let i = 0; i < s.length; ++i) {

        let c = s.charAt(i);
        if (c == '{' || c == '(' || c == '[') {
            stack.push(c);
        } else {
            let c1 = stack.pop();
            if (c1 == null) {
                return false;
            }
            if (c == '}' && c1 != '{') {
                return false;
            }
            if (c == ')' && c1 != '(') {
                return false;
            }
            if (c == ']' && c1 != '[') {
                return false;
            }
        }
    }
    if (!stack.isEmpty()) {
        return false;
    }
    return true;
};