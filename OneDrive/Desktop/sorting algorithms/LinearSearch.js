//linear search 




function LinearSearch(array , target){

    for(let i=0; i< array.length; i++){
        if(array[i] === target){
            return i
        }
    }

    return -1
}


const array = [1,2,3,4,5]

console.log(LinearSearch(array , 3))