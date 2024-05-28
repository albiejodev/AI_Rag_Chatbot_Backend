//bubblesort


function bubblesort(a){
    let swapped;
    do{
        swapped = false;
        for(let i=0; i<a.length ; i++){
            if(a[i] > a[i+1]){
                let temp = a[i];
                a[i] = a[i+1];
                a[i+1] = temp;
                swapped = true;
            }
        }
    }
    while(swapped)

    return a;
}

let array = [1,8,5,4,7,9,6,4,8,45,32,11,77]
console.log(bubblesort(array));