function calc() {
    let firstNumberElement = document.getElementById('num1')
    let secondNumberElement = document.getElementById('num2')

    let firstNumber = Number(firstNumberElement.value);
    let secondNumber = Number(secondNumberElement.value);

    let result = firstNumber + secondNumber;

    let resultElement = document.getElementById('sum');
    resultElement.value = result;

    console.log(firstNumberElement.value);
    
}   
