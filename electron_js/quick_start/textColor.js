function changeTextColor(){
    var textColor = document.getElementById('greeting').style.color;
    if (textColor === 'green'){
      document.getElementById('greeting').style.color = 'black';
    }
    else {
      document.getElementById('greeting').style.color = 'green';
    };
};