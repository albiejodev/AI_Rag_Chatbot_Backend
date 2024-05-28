function mergesort(a){
    if(a.length < 2){
        return a;
    }

    let mid = Math.floor(a.length/2)
    const lefta = a.slice(0 , mid);
    const righta = a.slice(mid);
    return merge(mergesort(lefta)   , mergesort(righta)); 

}


function merge(left , right){
    let sorted  =[];
    while(left.length &&  right.length){
        if(left[0] < right[0]){
            sorted.push(left.shift())
        }else{
            sorted.push(right.shift())
        }
    }
    return[...sorted , ...left , ...right]
}


let array = [1,8,5,4,7,9,6,4,8,45,32,11,77]
console.log(mergesort(array));