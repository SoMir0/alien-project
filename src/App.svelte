<script>
// imports
import Profile from './lib/Profile.svelte';
import Chat from './lib/Chat.svelte';
import Navbar from './lib/Navbar.svelte';

// variables
let userPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

let profileExtended = false;
let chatExtended = false;

// functions
if(userPrefersDark && !window.document.body.classList.contains('dark')) window.document.body.classList.toggle('dark');
const toggleTheme = () => {
  userPrefersDark = !userPrefersDark;
  window.document.body.classList.toggle('dark');
}
</script>

<main>
  <div class="container" style={chatExtended ? "margin-right: 17rem" : ""}>
    <Navbar />
    <button class="toggleButton left" on:click={() => {profileExtended = !profileExtended}}>👽</button>
    <button class="toggleButton right" on:click={() => {chatExtended = !chatExtended}}>{#if chatExtended}⤫{:else}⤆{/if}</button>
  </div>

  <aside class="profile" style={profileExtended ? "" : "left: -17rem"}>
    <Profile toggleThemeFunc={toggleTheme} currentTheme={userPrefersDark} />
  </aside>

  <aside class="chat" style={chatExtended ? "" : "right: -17rem"}>
    <Chat />
  </aside>
</main>

<style>
:root {
  --light-white: #fff;
  --white: #FEFBF6;
  --dark-white: #EDEAE5;
  --light-blue: #73A0B3;
  --purple: #7F5283;
  --dark-gray: #3D3C42;
  --box-shadow-color: rgba(108, 108, 108, .5);
}

:global(body.dark) {
  --light-white: #000;
  --white: #3D3C42;
  --dark-white: #2D2C32;
  --light-blue: #A6D1E6;
  --purple: #7F5283;
  --dark-gray: #FEFBF6;
  --box-shadow-color: rgba(18, 18, 18, .5);
}

main {
  position: fixed; top: 0; left: 0;
  width: 100vw; height: 100vh;
  font-family: monospace, sans-serif;
  background: var(--white);
  color: var(--dark-gray);
}

aside {
  background: var(--dark-white);
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
  color: var(--dark-gray);
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
  box-shadow: var(--box-shadow-color) 0 0 1rem;
}

.left {
  left: 0;
}

.right {
  right: 0;
}
</style>
