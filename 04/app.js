var button = document.getElementById('button');
var input = document.getElementById("input");
var list = document.getElementById('list');

button.addEventListener('click', clickButton)

var listCount = 2;

function clickButton(){
    console.log(input.value);
    var li = document.createElement('li');
    li.setAttribute("id", "li"+listCount)
    
    var checkbox = document.createElement('input');
    checkbox.type="checkbox";
    checkbox.setAttribute("onclick", "clickCheckbox("+listCount+")")

    li.appendChild(checkbox);

    li.innerHTML += input.value;

    var buttonHtml = "<button type='button' style='float: right;' onclick='removeToDo(" + listCount + ")'>삭제</button>"
    li.innerHTML = li.innerHTML + buttonHtml
    list.appendChild(li);
    listCount = listCount + 1
}

function removeToDo(count){
    var li = document.getElementById("li"+count)
    list.removeChild(li)
}

function clickCheckbox(count){
    var li = document.getElementById('li'+count)
    console.log((li.style.textDecoration))
    if (li.style.textDecoration == 'line-through'){
        li.style.textDecoration = 'none'
    } else {
        li.style.textDecoration = 'line-through'
    }
}