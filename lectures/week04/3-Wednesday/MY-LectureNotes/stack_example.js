class Stack {

    // __init__()
    // self.array =[] 

    constructor(){
        this.array = []
    }

    push(val){
        this.array.push(val)
    }

    pop(){

        let removedElement = this.array.pop()
        return removedElement
    }
}

// let stack = new Stack()