//Utilizando o Axios
//Enviando uma requisição GET para API, para listar todos as Skins


//Capturar botão de Criar Jogo
const createBtn = document.getElementById("createBtn")

createBtn.addEventListener("click", createGame)

//Capturar botão de Edição
const updateBtn = document.getElementById("updateBtn")

updateBtn.addEventListener("click", updateGame)

axios.get("http://localhost:5000/leagueofskins").
then(response => {
    const skins = response.data
    const listSkins = document.getElementById("skins")
    skins.forEach(skin => {
        let item = document.createElement("li")

        //setando o Atributo ID para cada game
        item.setAttribute("data-id", skin._id)
        item.setAttribute("data-name", skin.name)
        item.setAttribute("data-hero", skin.hero)
        item.setAttribute("data-value", skin.value)

        //const id = listItem.getAttibute("data-id")

        item.innerHTML = `<h4> ${skin.name}</h4>
        <p>Descrição: ${skin.hero}</p>
        <p>ano: ${skin.value}</p>
        <p>id: ${skin._id}</p>`

        
        
        var deleteBTN = document.createElement("button")
        deleteBTN.innerHTML = "Deletar"
        deleteBTN.classList.add("btn", "btn-danger", "mb-3", "mx-2")
        //quando clickar no botão
        deleteBTN.addEventListener("click", function(){
            deleteSkin(item)
        })

        var editBTN = document.createElement("button")
        editBTN.innerHTML = "Editar"
        editBTN.classList.add("btn", "btn-warning", "mb-3")
        editBTN.addEventListener("click", function(){
            loadForm(item)
        })

        listSkins.appendChild(item)
        item.appendChild(deleteBTN)
        item.appendChild(editBTN)

    })
})


//Função para deletar um game
function deleteSkin(listItem){

    const id = listItem.getAttribute("data-id")
    axios.delete(`http://localhost:5000/leagueofskins/${id}`).
    then(response => {
        window.alert("Skin deletada com sucesso:", response.data)
        listItem.remove()
    })
    .catch(error =>{
        window.alert("Erro ao deletar Skin", error)
    })

}

    function createSkin(){

        const form = document.getElementById("createForm")
        form.addEventListener("submit" , function(event){
            event.preventDefault() //Evita o envio padrão do formulário
        })

        const nameInput = document.getElementById("name")
        const heroInput = document.getElementById("hero")
        const valueInput = document.getElementById("value")

        const skin = {
            name: nameInput.value,
            hero: heroInput.value,
            value: valueInput.value
        }

        console.log(skin)

        //Enviando as informações do game para API
axios.post("http://localhost:5000/leagueofskins", game).then(response =>{

if (response.status ==201){
    alert("Skin Cadastrada com sucesso!")
    location.reload()
}
}).catch(error => {
    console.log(error)
})

    }


    //Função para carregar o formiulário de edição

    function loadForm(listItem){
        const id = listItem.getAttribute("data-id")
        const name = listItem.getAttribute("data-name")
        const hero = listItem.getAttribute("data-hero")
        const value = listItem.getAttribute("data-value")
        document.getElementById("idEdit").value = id
        document.getElementById("nameEdit").value = name
        document.getElementById("heroEdit").value = hero
        document.getElementById("valueEdit").value = value

    }

    //Função para alterar o game

    function updateGame(){

        
        const form = document.getElementById("editForm")
        form.addEventListener("submit", function(event){
            event.preventDefault() // Evita o envio padrão do formulário
        })


        const idInput = document.getElementById("idEdit")
        const nameInput = document.getElementById("nameEdit")
        const heroInput = document.getElementById("heroEdit")
        const valueInput = document.getElementById("valueEdit")
        
        const skin = {
            name: nameInput.value,
            hero: heroInput.value,
            value: valueInput.value
            }

        var id = idInput.value

        axios.put(`http://localhost:5000/leagueofskins/${id}`, game).then(response => {
            if(response.status == 200){
                alert("Skin Atualizada com sucesso")
                location.reload()
            }
        }).catch(error => {
            console.log(error)
        })

    }

