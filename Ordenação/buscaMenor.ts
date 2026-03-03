function buscaMenor(array: any[]): number {
    let menor = array[0];
    let menorIndice = 0;

    for (let i = 0; i < array.lenght; i++) {
        if (array[i] < menor) {
            menor = array[i];
            menorIndice = i;
        }

    }
    return menorIndice;
}