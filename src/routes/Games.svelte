<div class="game-list">
  <a href="/" class="game">Pong</a>
  <a href="/" class="game">Snake</a>
  <a href="/" class="game">Tetris</a>
  <a href="/" class="game">Space Invaders</a>
</div>

<style>

.game-list {
  display: flex; flex-direction: row; flex-wrap: wrap;
  gap: 1rem;
}

.game {
  display: flex; align-items: center; justify-content: center;
  text-align: center;
  text-decoration: none;
  color: #111;
  background: #e1d9cc;
  width: 5rem; height: 5rem;
  border-radius: 1rem;
  user-select: none;
  cursor: pointer;
  transition: 150ms ease-in-out;
}

.game:hover {
  transform: translatey(-10%);
  box-shadow: #2229 0 5px 1rem;
}

</style>
