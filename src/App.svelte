<script>
import Profile from './lib/Profile.svelte';
import Chat from './lib/Chat.svelte';
import Navbar from './lib/Navbar.svelte';

let profileExtended = false;
let chatExtended = false;
</script>

<main>
  <div class="container" style={chatExtended ? "margin-right: 17rem" : ""}>
    <Navbar />
    <button class="toggleButton left" on:click={() => {profileExtended = !profileExtended}}>👽</button>
    <button class="toggleButton right" on:click={() => {chatExtended = !chatExtended}}>{#if chatExtended}⤫{:else}⤆{/if}</button>
  </div>

  <aside class="profile" style={profileExtended ? "" : "left: -17rem"}>
    <Profile />
  </aside>

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

.profile {
  top: 0; left: 0;
}

.container {
  display: flex; justify-content: center;
  transition: margin 100ms linear;
  padding: 1rem;
  margin-top: 5rem;
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

.chat:hover {
  box-shadow: rgba(108, 108, 108, .5) 0 0 1rem;
}

.left {
  left: 0;
}

.right {
  right: 0;
}
</style>
