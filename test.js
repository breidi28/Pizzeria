// print all the prime numbers from 1 to 100

// 1 is not a prime number

let isPrime = (num) => {
    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
        return false;
        }
    }
    return true;
    }

for (let i = 2; i <= 100; i++) {
    if (isPrime(i)) {
        console.log(i);
    }
}