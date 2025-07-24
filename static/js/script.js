document.addEventListener('DOMContentLoaded',function(){
  M.FormSelect.init(document.querySelectorAll('select'));
  M.Modal.init(document.querySelectorAll('.modal'));

  //show booking form
  const bookingForm = document.getElementById('bookingForm');
  const bookBtn = document.getElementById('bookBtn');

  bookBtn.onclick = ()=>{
    bookingForm.style.display = bookingForm.style.display =='block'?'none':'block';
  console.log(true)
  }
})
