let enemies = 1;

function increase_enemies() {
  enemies = 2;
  console.log(`enemies inside function: ${enemies}`);
}

increase_enemies();
console.log(`enemies outside function: ${enemies}`);
