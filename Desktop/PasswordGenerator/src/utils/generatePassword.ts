type generatePasswordOptions = {
    length : number 
    includeuppercase : boolean
    includelowercase : boolean
    includeNumbers : boolean
    includeSymbols : boolean
}


const LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz";
const UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const NUMBERS = "0123456789";
const SYMBOLS = " !@#$%^&*( )_+-={}[]|; :<>, .?/~`";


function generatePassword({length , includeuppercase , includelowercase , includeNumbers , includeSymbols } : generatePasswordOptions) {

    let char = "";
    if(includeuppercase){
        char = char + UPPERCASE_LETTERS
    }

    if(includelowercase){
        char = char + LOWERCASE_LETTERS
    }

    if(includeNumbers){
        char = char + NUMBERS
    }

    if(includeSymbols){
        char = char + SYMBOLS
    }


    let password = "";
    for(let i=0; i<length; i++){
        password = password + char.charAt(Math.floor(Math.random() * char .length)) ; 
    }

    return password; 
}

export {generatePassword}