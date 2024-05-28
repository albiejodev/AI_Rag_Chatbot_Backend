function quicksort(a){
    if(a.length < 2){
        return a;
    }

    let pivot = a[a.length -1];
    let left = [];
    let right =[];

    for(let i=0; i<a.length -1 ; i++){
        if(a[i] < pivot ){
            left.push(a[i])
        }else{
            right.push(a[i])
        }
    }
    return [...quicksort(left) , pivot , ...quicksort(right)]
}



let array = [1,8,5,4,7,9,6,4,8,45,32,11,77]
console.log(quicksort(array));