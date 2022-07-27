function balanced_brackets(codeString){

    if(!codeString.length){
        return true
    }

    let stack = []

    let opening = {
        "(" : true, 
        "{" : true, 
        "[" : true
    }

    let closing = {
        ")": "(", 
        "}": "{", 
        "]" : "["
    }

    for(let i = 0; i< codeString.length; i++){

        let char = codeString[i] 

        if(opening[char]){ 
            stack.push(char)  
        }

        if(char in closing){ 
            let lastChar = stack.pop()  

            if(lastChar !== closing[char]){
                return false
            }
        }

    }

    if(stack.length == 0){
        return true
    }
    else{
        return false
    }
}



console.log(balanced_brackets('{}'))