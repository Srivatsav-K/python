const num = 20;

switch (num) {
  case 30:
    console.log("number is 30");
    break;
  default:
    console.log("Try again");
}

function guessTheNumber() {
  const answer = Math.ceil(Math.random() * 100);
  console.log(answer);

  const guess = Number(prompt("Guess the answer : "));
  console.log(typeof guess);

  switch (guess) {
    case guess > answer:
      alert("Guess is higher than the answer");
      guessTheNumber();

    case guess < answer:
      alert("Guess is lower than the answer");
      guessTheNumber();

    case guess == answer:
      alert("Yay you are right");
    default:
      return;
  }
}
