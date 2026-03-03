function ordenacaoPorSelecao(array: any[] ) {
    let novoArray = [];

    for (let i = 0; i < array.lenght; i++) {
        let menorIndice = buscaMenor(array);
        if(menorIndice != undefined) {
            let menorElemento = array.splice(menorIndice, 1) [0]
            novoArray.push(menorElemento);
        } else {
            break;
        }
    }
    return novoArray;
}