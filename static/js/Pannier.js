//localStorage.removeItem('basket');
//localStorage.removeItem('htmlbasket')
let basket = JSON.parse(localStorage.getItem('basket')) || [] ;

let htmlbasket = JSON.parse(localStorage.getItem('htmlbasket')) || [] ;


function remove(productid) {
  // Find the index of the product in the basket array
  var index = basket.findIndex(product => product.id === productid);
  var indexx = htmlbasket.findIndex(htmlString => {
    // Convert the HTML string to a DOM element
    var tempDiv = document.createElement('div');
    tempDiv.innerHTML = htmlString;
    var productIdElement = tempDiv.querySelector(".product-details h2");

    if (productIdElement) {
        // Compare text content after trimming any leading or trailing spaces
        return productIdElement.textContent.trim() === productid;
    }
    return false; // Return false if the element is not found
  });


  console.log(htmlbasket);
  if (index !== -1) {
      // Remove the product from the basket array
      basket.splice(index, 1);
      htmlbasket.splice(indexx, 1);
      console.log(htmlbasket);

  
     
    
      // Save the updated basket array to local storage
      savebasket();
      savehtmlbasket();
   
      // Update the total price after removing the product
      
      window.location.href = 'pannier';

      // Redirect the user to the cart page after the DOM is updated
    
  }
}



function savebasket (){
  localStorage.setItem('basket',JSON.stringify(basket));
}

function savehtmlbasket (){
  localStorage.setItem('htmlbasket',JSON.stringify(htmlbasket));
}

function getTotalPrice(){

  var total=0 ;

  for (const product of basket ) {
      total+= product.price *product.quantity ;

      
      }
  document.querySelector('.js-total_cost').innerHTML=total;
}

function affichage(){


  // adding the product to the list
  for (const html of htmlbasket ) {
      document.getElementById("liste-articles").innerHTML += html;
  }
  
  getTotalPrice() ; 
    
  savebasket () ;
  savehtmlbasket ()  ;
}



affichage();





