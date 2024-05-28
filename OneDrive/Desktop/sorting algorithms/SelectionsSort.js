function selectionSort(a){
    for (let i = 0; i < a.length-1; i++) {
        let minimum = i;

        for(let j=i+1; j<a.length ; j++){
            if(a[j] < a[i]){
                minimum = j
            }
        }

        if(minimum !== i){
            let temp = a[i];
            a[i] = a[minimum];
            a[minimum] = temp
        }
        
    }

    return a
}


let array = [1,8,5,4,7,9,6,4,8,45,32,11,77]

console.log(selectionSort(array));