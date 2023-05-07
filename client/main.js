const host = 'http://localhost:5000/datos'
let load = window.addEventListener('load',function(){
    let object = new XMLHttpRequest()
    object.open('GET',host)
    object.onload=function(){
        let myJson = JSON.parse(this.responseText);
        let template = '';
        myJson.resultados.forEach(myJson=> {
            template += `<ul>
            <li>${myJson.id} ${myJson.nombre} ${myJson.apellido} ${myJson.edad} ${myJson.sexo} ${myJson.nacionalidad} ${myJson.profecion}</li>
            </ul>`
            document.getElementById('data').innerHTML = template
        });
        
       
    }
    object.send()
    
})
