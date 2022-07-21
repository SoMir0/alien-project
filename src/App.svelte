<script>
import Profile from './lib/Profile.svelte';
import Chat from './lib/Chat.svelte';

let profileExtended = false;
let chatExtended = false;
</script>

<main>
  <aside class="profile" style={profileExtended ? "" : "left: -17rem"}>
    <Profile />
  </aside>
  <div class="container" style={chatExtended ? "margin-right: 17rem" : ""}>
    <button class="toggleButton left" on:click={() => {profileExtended = !profileExtended}}>👾</button>
    <button class="toggleButton right" on:click={() => {chatExtended = !chatExtended}}>{#if chatExtended}⤇{:else}⤆{/if}</button>
    <div class="game-list">
      <div class="game">Pong</div>
      <div class="game">Snake</div>
      <div class="game">Tetris</div>
      <div class="game">Space Invaders</div>
    </div>
  </div>
  <aside class="chat" style={chatExtended ? "" : "right: -17rem"}>
    <Chat />
  </aside>
</main>

<style>
main {
  position: fixed; top: 0; left: 0;
  width: 100vw; height: 100vh;
  font-family: monospace, sans-serif;
  background: #f0ebe3;
}

aside {
  background: #e4dccf;
  transition: 200ms linear;
  display: flex; flex-direction: column; align-items: center;
  position: absolute;
  width: 15rem;
  height: 100%;
  padding: 1rem;
}

aside:hover {
  box-shadow: rgba(108, 108, 108, .5) 0 0 1rem;
}

.profile {
  top: 0; left: 0;
}

.container {
  display: flex; justify-content: center;
  transition: margin 200ms linear;
  padding: 1rem;
}

.container .game-list {
  display: flex; flex-direction: row; flex-wrap: wrap;
  gap: 1rem;
}

.game {
  display: flex; align-items: center; justify-content: center;
  text-align: center;
  background: #e1d9cc;
  width: 5rem; height: 5rem;
  border-radius: 1rem;
  transition: 150ms ease-in-out;
}

.game:hover {
  transform: translatey(-10%);
  box-shadow: #2229 0 5px 1rem;
}

.container .toggleButton {
  position: absolute;
  top: 0;
  background: none;
  outline: none; border: none;
  border-radius: 0.5rem;
  font-size: 1.5rem;
  cursor: pointer;
  z-index: 9;
}

.chat {
  top: 0; right: 0;
}

.left {
  left: 0;
}

.right {
  right: 0;
}
</style>
