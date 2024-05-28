function insertionSort(a){
    for(let i=0; i<a.length ; i++){
        let number=a[i];
        let j=i-1;
        while(j>=0 && a[j] > number){
            a[j+1] = a[j]
            j--;
        }
        a[j+1] = number;
    }
    return a;
}



let array = [1,8,5,4,7,9,6,4,8,45,32,11,77]
console.log(insertionSort(array));