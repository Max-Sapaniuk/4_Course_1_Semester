TextToWork = prompt('Введіть вихідний текст')
UserStep = Number(prompt('Введіть крок зсуву:'))

var OtherSymbols = [' ', ',', '.', ':', ';', '!', '?', '-', '_', '=', '+', '(', ')', '[', ']', '@', '`', "'", '"', '<', '>', '|', '/', '%', '$', '^', '&', '*', '~'];
var Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
var EngAlfUp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
var EngAlfLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
var EngAlfUpEncrypt = Array(26);
var EngAlfLowerEncrypt = Array(26);
var NumbersEncrypt = Array(10);

initEncrypt();

function initEncrypt() {
    NumbersEncrypt = CezarEncrypt(UserStep, Numbers);
    EngAlfUpEncrypt = CezarEncrypt(UserStep, EngAlfUp);
    EngAlfLowerEncrypt = CezarEncrypt(UserStep, EngAlfLower);
}

function CezarEncrypt(step, arr) {
    var copy = arr.slice();
    for (i = 0; i < step; i += 1) {
        copy.unshift(copy.pop())
    }
    return copy;
}

function contains(symb, arr) {
    var letter = symb;
    pos = 0;
    for (var i = 0; i < arr.length; i++) {
        if (letter === arr[i]) {
            pos = i;
            return true;
        }
    }
}

function encrypt(text) {
    var result = '';
    for (var i = 0; i <= text.length; i++) {
        var symbol = text[i];
        if (contains(symbol, OtherSymbols)) {
            result += symbol;
        }
        if (contains(symbol, Numbers)) {
            symbol = NumbersEncrypt[pos];
            result += symbol;
        }
        if (contains(symbol, EngAlfUp)) {
            symbol = EngAlfUpEncrypt[pos];
            result += symbol;
        }
        if ((contains(symbol, EngAlfLower))) {
            symbol = EngAlfLowerEncrypt[pos];
            result += symbol;
        }
    }
    return result;
}

alert(encrypt(TextToWork))
