function create(words) {
   let parentElement = document.getElementById('content');
   let elements = words;

   for(let i = 0; i < elements.length; i++){

   let div = document.createElement('div');
   let p = document.createElement('p');
   let text = document.createTextNode(elements[i]);

   p.appendChild(text);
   p.style.display = 'none';
   div.appendChild(p);
   div.addEventListener('click', showParagraphs);
   parentElement.appendChild(div);
}

function showParagraphs(event){
   event.target.children[0].style.display = 'inline';
}

}