
function getComputerChoice(){
    var choices = ['rock','paper','scissors'];
    var randomIndex = Math.floor(Math.random()*choices.length);
    return choices[randomIndex]
}

function playRound(pSelection, computerSelection){
    var playerSelection = pSelection.toLowerCase()
    var result = "Draw"
    if(playerSelection=="rock"){
        if(computerSelection=="paper"){
            result = "Lose";
        }
        else if(computerSelection=="scissors"){
            result = "Win";
        }
    }
    else if(playerSelection=="paper"){
        if(computerSelection=="scissors"){
            result = "Lose";
        }
        else if(computerSelection=="rock"){
            result = "Win";
        }
    }
    else if(playerSelection=="scissors"){
        if(computerSelection=="rock"){
            result = "Lose";
        }
        else if(computerSelection=="paper"){
            result = "Win";
        }
    }
    return result
}

function game(){
    let score = 0
    for (let i=0; i<5; i++){
        let playerSelection = prompt("Choose rock, paper, or scissors!");
        let computerChoice = getComputerChoice()
        console.log("The computer choice: " + computerChoice)
        let result = playRound(playerSelection, computerChoice);
        console.log(result)
        if(result=="Win"){
            score++;
        }else if(result=="Lose"){
            score--;
        }
    }
    if(score>1){
        console.log("You win!")
    }else if(score<0){
        console.log("You lose!")
    }else{
        console.log("It's a tie!")
    }
}

game()