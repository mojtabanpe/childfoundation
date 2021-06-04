function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function loadDoc(mode) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      
      if (this.readyState == 4 && this.status == 200) {
        console.log('salam');
        document.getElementById("ghafeloo").innerHTML = 'ghafeloo';
      }
    };
    xhttp.open("POST", "/helpers/send_email", true);

    var params = 'mode='+ mode;
    xhttp.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    xhttp.send(params);
  }

  function loadDoc1() {
  //   $.ajax({
  //     url: "https://cubber.zendesk.com/api/v2/users/"+a+"/organizations.json",
  //     type: 'GET',
  //     dataType: 'jsonp',
  //     cors: true ,
  //     contentType:'application/json',
  //     secure: true,
  //     headers: {
  //       'Access-Control-Allow-Origin': '*',
  //     },
  //     beforeSend: function (xhr) {
  //       xhr.setRequestHeader ("Authorization", "Basic " + btoa(""));
  //     },
  //     success: function (data){
  //       console.log(data.organizations[0].name);
  //       var organisation = data.organizations[0].name;
  //       $("#company").text(organisation);
  //     }
  // })
  $.ajax({
    url: "/helpers/send_email",
    type: 'GET', // This is the default though, you don't actually need to always mention it
    dataType: 'jsonp',
    success: (data) => {
        alert(data);
    },
    failure: (data) => { 
        alert('Got an error dude');
    }
}); 
  }

  function showContent(showMode) {
    document.getElementById("ghafeloo").innerHTML = showMode;  
  }

 