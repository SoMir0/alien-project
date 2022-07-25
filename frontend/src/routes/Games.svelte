<script>
import { link } from "svelte-routing";
</script>

<div class="game-list">
  <a href="/pong" class="game" use:link style="background-image: url('https://cdn.vox-cdn.com/thumbor/ti0KbF0NyLx7-xz7uyvUJ55GNNo=/0x33:800x566/1820x1213/filters:focal(0x33:800x566)/cdn.vox-cdn.com/assets/1812005/Pong.png')"><p>Pong</p></a>
  <a href="/snake" class="game" use:link style="background-image: url('https://image.winudf.com/v2/image/Y29tLnNuYWtlY29tcGFueS5zbmFrZWdhbWVfc2NyZWVuXzFfanhsM21pams/screen-1.jpg?fakeurl=1&type=.jpg');"><p>Snake</p></a>
  <a href="/tetris" class="game" use:link style="background-image: url('https://assets.vg247.com/current/2014/04/bg-tetris-10.png')"><p>Tetris</p></a>
  <a href="/space-invaders" class="game" use:link style="background-image: url('https://1.bp.blogspot.com/-VoKIrzdjBuk/Xn1q3LhNToI/AAAAAAAAW64/O7jRIrhA7rYrOy3iDQMkbSxEOiFw9bcOACLcBGAsYHQ/s1600/space-invaders.jpg')"><p>Space Invaders</p></a>
</div>

<style>

.game-list {
  display: flex; flex-direction: row; flex-wrap: wrap;
  gap: 1rem;
}

.game {
  display: flex; align-items: center; justify-content: center;
  background: var(--light-blue);
  background-size: 5rem;
  width: 5rem; height: 5rem;
  border-radius: 1rem;
  user-select: none;
  cursor: pointer;
  transition: 150ms ease-in-out;
  text-align: center;
  text-decoration: none;
  color: var(--dark-gray);
}

.game p {
  position: relative;
  top: 4rem;
}

.game:hover {
  transform: translatey(-10%);
  box-shadow: var(--box-shadow-color) 0 5px 1rem;
}

</style>
