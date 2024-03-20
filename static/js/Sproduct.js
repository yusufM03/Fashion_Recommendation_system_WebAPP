//localStorage.removeItem('basket');
//localStorage.removeItem('htmlbasket')
let basket = JSON.parse(localStorage.getItem('basket')) || [] ;


let htmlbasket = JSON.parse(localStorage.getItem('htmlbasket')) || [] ;

function savebasket (){
  localStorage.setItem('basket',JSON.stringify(basket));
}

function savehtmlbasket (){
  localStorage.setItem('htmlbasket',JSON.stringify(htmlbasket));
}


function add(){
// lors de l'appui sur le bouton add to cart , calculate the total price and access immediatly to the cart  
  
  var quantityy = document.getElementById('quantity').value;
  console.log(quantityy);
  alert('Added ' + quantityy + ' product(s) to the cart!');

  var productElement = document.querySelector('h1').textContent.trim();
  var price= document.querySelector('strong').textContent.trim().substring(1);

  var productImageElement = document.querySelector('.product-image img');
  var imageurl = productImageElement.src;

  console.log(product);
  var productPrice = parseInt(price); 

  var product={"id" :productElement ,"price" :productPrice , "img": imageurl} ;

  console.log(product);

  product.quantity =quantityy ;
  
  var html = `<div  class="product">
                <div class="product-image">
                   <img src=${imageurl} >
                </div> 
                <div class="product-details"> 
                  <h2>${product.id}</h2>
                  <div class="details-row">
                    <label for="quantity"> Quantity:</label>
                    <input type="number" id="quantity" min="1" value="${product.quantity}">
                  </div>
                  <div class="details-row">
                    <span>$ ${product.price}</span>
                  </div>
                  <button onclick="remove('${product.id}')"  class="delete-button" ><i style="font-size:24px" class="fa">&#xf00d;</i> </button>
               </div>
              </div>`; 

                  
                 
  struchtml=[html] ;
  basket.push(product);
  htmlbasket.push(struchtml) ;
  
  savebasket();
  savehtmlbasket();

 // Redirect to the cart page
 window.location.href = 'pannier';

}