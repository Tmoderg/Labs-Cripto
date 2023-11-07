// ==UserScript==
// @name         Descifrar Mensajes Cifrados
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Descifrar mensajes cifrados en una página web y mostrarlos en texto plano
// @author       Tu Nombre
// @match        https://cripto.tiiny.site/
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js
// ==/UserScript==

(function() {
    'use strict';

    // Espera a que la página esté completamente cargada
    window.addEventListener('load', function() {
        // Obtén la clave en mayúsculas
        var texto = document.body.textContent;
        var clave = texto.match(/[A-Z]/g).join('');
        console.log('La llave es: ' + clave);

        // Detecta la cantidad de mensajes cifrados
        var mensajesCifrados = document.querySelectorAll('div[class^="M"]');

        // Muestra la cantidad de mensajes cifrados en la consola
        console.log('Los mensajes cifrados son: ' + mensajesCifrados.length);

        let script = document.createElement('script');
        script.src = "https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js";
        script.integrity = "sha384-S3wQ/l0OsbJoFeJC81UIr3JOlx/OzNJpRt1bV+yhpWQxPAahfpQtpxBSfn+Isslc";
        script.crossOrigin = 'anonymous';
        let keys= CryptoJS.enc.Utf8.parse(clave);
        script.onload = function() {
    //
    for(let i = 0 ; i < mensajesCifrados.length; i++){
        let desencriptar = CryptoJS.TripleDES.decrypt(mensajesCifrados[i].id,keys , { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8);
        console.log(mensajesCifrados[i].id+" "+desencriptar);// Muestra por consola los mensajes y la palabra descifrada
        let resultadoElemento = document.createElement('p');
        resultadoElemento.textContent = desencriptar;
        document.body.appendChild(resultadoElemento);
    }
  };
        document.head.appendChild(script);
    });
})();
