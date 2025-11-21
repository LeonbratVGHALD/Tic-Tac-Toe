// Client-side Tic-Tac-Toe implementation mirroring your Tkinter app.
const BOARD_SIZE = 3;
let board = [];
let currentPlayer = 'X';
let gameOver = false;
let vsCPU = false; // true when in singleplayer

const menu = document.getElementById('menu');
const game = document.getElementById('game');
const boardDiv = document.getElementById('board');
const info = document.getElementById('info');
const modeSpan = document.getElementById('mode');

// Custom confirm modal elements
const confirmModal = document.getElementById('confirmModal');
const confirmMessage = document.getElementById('confirmMessage');
const confirmOk = document.getElementById('confirmOk');
const confirmCancel = document.getElementById('confirmCancel');

/**
 * Show a custom confirm dialog with the given message.
 * Returns a Promise that resolves to true (OK) or false (Cancel).
 */
function showConfirm(message){
  return new Promise((resolve)=>{
    if(!confirmModal) {
      // Fallback to native confirm if modal not present
      resolve(window.confirm(message));
      return;
    }
    confirmMessage.textContent = message;
    confirmModal.classList.remove('hidden');
    confirmModal.setAttribute('aria-hidden','false');

    function cleanup(){
      confirmModal.classList.add('hidden');
      confirmModal.setAttribute('aria-hidden','true');
      confirmOk.removeEventListener('click', onOk);
      confirmCancel.removeEventListener('click', onCancel);
    }

    function onOk(){ cleanup(); resolve(true); }
    function onCancel(){ cleanup(); resolve(false); }

    confirmOk.addEventListener('click', onOk);
    confirmCancel.addEventListener('click', onCancel);
  });
}

function init() {
  document.getElementById('btn-single').addEventListener('click', startSingle);
  document.getElementById('btn-multi').addEventListener('click', startMulti);
  document.getElementById('btn-quit').addEventListener('click', () => window.close());
  document.getElementById('btn-restart').addEventListener('click', restart);
  document.getElementById('btn-back').addEventListener('click', showMenu);
  buildBoardUI();
  restart();
}

function buildBoardUI(){
  boardDiv.innerHTML = '';
  for(let r=0;r<BOARD_SIZE;r++){
    for(let c=0;c<BOARD_SIZE;c++){
      const cell = document.createElement('div');
      cell.className = 'cell';
      cell.dataset.r = r; cell.dataset.c = c;
      cell.addEventListener('click', () => onClick(r,c));
      boardDiv.appendChild(cell);
    }
  }
}

function showMenu(){
  game.classList.add('hidden');
  menu.classList.remove('hidden');
}
function showGame(){
  menu.classList.add('hidden');
  game.classList.remove('hidden');
}

function startSingle(){
  vsCPU = true;
  modeSpan.textContent = 'Modus: Enspiller';
  restart();
  showGame();
}
function startMulti(){
  vsCPU = false;
  modeSpan.textContent = 'Modus: Flerspiller';
  restart();
  showGame();
}

function restart(){
  board = Array.from({length: BOARD_SIZE}, () => Array(BOARD_SIZE).fill(null));
  gameOver = false;
  currentPlayer = 'X';
  info.textContent = `Tur: ${currentPlayer}`;
  const cells = document.querySelectorAll('.cell');
  cells.forEach(c => { c.textContent = ''; c.classList.remove('disabled','win'); c.style.pointerEvents = ''; });
}

function onClick(r,c){
  if(gameOver) return;
  if(board[r][c] !== null) return;
  setCell(r,c,currentPlayer);
  const res = checkWinner();
  if(res.winner){ endGame(res.winner, res.line); return; }
  if(isBoardFull()){ endGame(null, null); return; }
  currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
  info.textContent = `Tur: ${currentPlayer}`;
  if(vsCPU && currentPlayer === 'O') cpuMove();
}

function setCell(r,c,val){
  board[r][c] = val;
  const selector = `.cell[data-r="${r}"][data-c="${c}"]`;
  const cell = document.querySelector(selector);
  if(cell){ cell.textContent = val; cell.classList.add('disabled'); }
}

function getEmptyCells(){
  const empties = [];
  for(let r=0;r<BOARD_SIZE;r++) for(let c=0;c<BOARD_SIZE;c++) if(board[r][c]===null) empties.push([r,c]);
  return empties;
}

function findWinningMove(player){
  // Check rows
  for(let r=0;r<BOARD_SIZE;r++){
    const row = board[r];
    if(row.filter(x=>x===player).length===BOARD_SIZE-1 && row.filter(x=>x===null).length===1){
      return [r, row.indexOf(null)];
    }
  }
  // Check cols
  for(let c=0;c<BOARD_SIZE;c++){
    const col = [];
    for(let r=0;r<BOARD_SIZE;r++) col.push(board[r][c]);
    if(col.filter(x=>x===player).length===BOARD_SIZE-1 && col.filter(x=>x===null).length===1){
      return [col.indexOf(null), c];
    }
  }
  // Diag1
  const diag1 = []; for(let i=0;i<BOARD_SIZE;i++) diag1.push(board[i][i]);
  if(diag1.filter(x=>x===player).length===BOARD_SIZE-1 && diag1.filter(x=>x===null).length===1){
    const i = diag1.indexOf(null); return [i,i];
  }
  // Diag2
  const diag2 = []; for(let i=0;i<BOARD_SIZE;i++) diag2.push(board[i][BOARD_SIZE-1-i]);
  if(diag2.filter(x=>x===player).length===BOARD_SIZE-1 && diag2.filter(x=>x===null).length===1){
    const i = diag2.indexOf(null); return [i, BOARD_SIZE-1-i];
  }
  return null;
}

function cpuMove(){
  if(gameOver) return;
  const empties = getEmptyCells();
  if(empties.length===0) return;
  let move = findWinningMove('O');
  if(!move){
    const strategy = Math.random() < 0.5 ? 'random' : 'block';
    if(strategy === 'block'){
      const block = findWinningMove('X');
      if(block) move = block;
    }
    if(!move){ move = empties[Math.floor(Math.random()*empties.length)]; }
  }
  const [r,c] = move;
  setCell(r,c,'O');
  const res = checkWinner();
  if(res.winner){ endGame(res.winner, res.line); return; }
  if(isBoardFull()){ endGame(null,null); return; }
  currentPlayer = 'X';
  info.textContent = `Tur: ${currentPlayer}`;
}

function checkWinner(){
  // rows
  for(let r=0;r<BOARD_SIZE;r++){
    const vals = board[r];
    if(vals[0] && vals.every(v=>v===vals[0])) return {winner: vals[0], line: [[r,0],[r,1],[r,2]]};
  }
  // cols
  for(let c=0;c<BOARD_SIZE;c++){
    const vals = [board[0][c], board[1][c], board[2][c]];
    if(vals[0] && vals.every(v=>v===vals[0])) return {winner: vals[0], line: [[0,c],[1,c],[2,c]]};
  }
  // diag1
  const vals1 = [board[0][0], board[1][1], board[2][2]];
  if(vals1[0] && vals1.every(v=>v===vals1[0])) return {winner: vals1[0], line: [[0,0],[1,1],[2,2]]};
  // diag2
  const vals2 = [board[0][2], board[1][1], board[2][0]];
  if(vals2[0] && vals2.every(v=>v===vals2[0])) return {winner: vals2[0], line: [[0,2],[1,1],[2,0]]};
  return {winner: null, line: null};
}

function isBoardFull(){
  for(let r=0;r<BOARD_SIZE;r++) for(let c=0;c<BOARD_SIZE;c++) if(board[r][c]===null) return false;
  return true;
}

function endGame(winner, line){
  gameOver = true;
  if(winner){
    info.textContent = `${winner} vant!`;
    line.forEach(([r,c]) => {
      const selector = `.cell[data-r="${r}"][data-c="${c}"]`;
      const cell = document.querySelector(selector);
      if(cell) cell.classList.add('win');
    });
    setTimeout(()=>{
      showConfirm(`${winner} vant!\nSpille igjen?`).then(res => { if(res) restart(); else showMenu(); });
    }, 30);
  } else {
    info.textContent = 'Uavgjort!';
    setTimeout(()=>{
      showConfirm('Uavgjort!\nSpille igjen?').then(res => { if(res) restart(); else showMenu(); });
    }, 30);
  }
}

window.addEventListener('load', init);
