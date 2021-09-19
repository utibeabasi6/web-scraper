form = document.getElementById("form")

form.onsubmit = (e) =>{
    url = document.getElementById("url").value
    if(url == ""){
        alert("Please input a url")
        return false
    }

    if(url.startsWith("http://") == false && url.startsWith("https://") == false){
        alert("Please enter a valid url")
        return false
    }
    return true
}