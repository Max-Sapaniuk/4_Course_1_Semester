function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

var input, output, key;

var inp = [], k = [];

input = prompt("Введіть вихідний текст");

key = prompt("Введіть ключ");

if ((key.length) < (input.length)) {
    alert("Ключ коротше повідомлення це небезпечно. Скопіюйте новий згенерований ключ із консолі браузера.");
    key = "";
    for (var i = 0; i < input.length; i++) {
        key += String.fromCharCode(getRandomInt(0, 66535));
    }
    console.log("Скопіюйте новий ключ:");
    console.log(key);

}

output = [];
for (i = 0; i < input.length; i++) {
    inp.push(input.charCodeAt(i));
    k.push(key.charCodeAt(i));
    output.push(inp[i] ^ k[i]);
}

alert(`Вихідний текст у кодуванні UTF-16: \n${inp}
Ключ у кодуванні UTF-16: \n${k}
Результат роботи алгоритма у кодуванні UTF-16: \n${output}`);
