const ourFetch = (url) => {
    let promise = new Promise((resolve, reject)=>{
        let xhr = new XMLHttpRequest();
        xhr.open('GET',url)
        xhr.send()

        xhr.onreadystatechange = () =>{ //this is our event listener for when the API info is ready
            if (xhr.readyState == 4 && xhr.status == 200){ //xhr.readyState can be 0(unsent),1(opened),2(Headers received),3(loading) or 4(Done). 
                //data has successfully arrived
                let data = JSON.parse(xhr.responseText)
                // console.log(data)
                resolve(data)
            }else if (xhr.readyState == 4 && xhr.status !== 200) {
                console.log(xhr.readyState)
                reject('error in retrieving data')

            }



        }
    })
    return promise;
}

window.ourFetch = ourFetch

// just like <fetch(url).then>, we can do 