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


let department_field = document.getElementById('id_department')
let supervisor_field = document.getElementById('id_supervisor')

department_field.addEventListener("change", getDepartmentId)

function getDepartmentId(e){
    // console.log(e.target.value)
    let department_id = e.target.value


    async function postJSON(data) {
        try {
          const response = await fetch(url, {
            method: "POST", // or 'PUT'
            headers: {
                
              "Content-Type": "application/json",
              'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify(data),
          });
      
          const result = await response.json();
          console.log("Success:", result);

          supervisor_field.innerHTML = '<option value="" selected="">----------</option>'
          for(let i = 0; i < result.length; i++){
            supervisor_field.innerHTML = `<option value="${result[i]['id']}"selected="">${result[i]['first_name']}</option>`
          }
        } catch (error) {
          console.error("Error:", error);
        }
      }
      
      const data = { id: department_id };
      let url = "http://127.0.0.1:8000/supervisor/"
      postJSON(data);
      
}


