const Wegener = (text, k) => {
    const chars = text.split('');
    const encodedData = chars
        .map((char) => String.fromCharCode(char.charCodeAt() + k))
        .join('');
    console.log(
        `\nУспішно закодовано дані за допомогою алгоритма Віженера!\n`
    );
    console.log(encodedData)
}
Wegener('dima', 3)