<script>
// imports
import Profile from './components/Profile.svelte';
import Chat from './components/Chat.svelte';
import Navbar from './components/Navbar.svelte';

import { onMount } from "svelte";


// variables
let userPrefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

let profileExtended = false;
let chatExtended = false;

let username = "Loading...";

// functions
if(userPrefersDark && !window.document.body.classList.contains('dark')) window.document.body.classList.toggle('dark');

const toggleTheme = () => {
  userPrefersDark = !userPrefersDark;
  window.document.body.classList.toggle('dark');
}

onMount(async () => {
  let resp = await fetch("/api/greet").then((res) => res.json());
  username = resp.username;
});

</script>

<main>
  <div class="container" style={chatExtended ? "margin-right: 17rem" : ""}>
    <Navbar />
  </div>

  <button class="toggleButton left" on:click={() => {profileExtended = !profileExtended}}>👽</button>
  <button class="toggleButton right" on:click={() => {chatExtended = !chatExtended}}>{#if chatExtended}⤫{:else}⤆{/if}</button>

  <aside class="profile" style={profileExtended ? "" : "left: -17rem"}>
    <Profile toggleThemeFunc={toggleTheme} currentTheme={userPrefersDark} userInfo={username} />
  </aside>

  <aside class="chat" style={chatExtended ? "" : "right: -17rem"}>
    <Chat />
  </aside>
</main>

<style>
:global(body), :global(html) {
  width: 100%; height: 100%;
  margin: 0; padding: 0;
}

:root {
  --light-white: #fff;
  --white: #FEFBF6;
  --dark-white: #EDEAE5;
  --light-blue: #73A0B3;
  --purple: #7F5283;
  --dark-gray: #3D3C42;
  --gray: #727272;
  --box-shadow-color: rgba(108, 108, 108, .5);
}

:global(body.dark) {
  --light-white: #000;
  --white: #3D3C42;
  --dark-white: #2D2C32;
  --light-blue: #A6D1E6;
  --purple: #7F5283;
  --dark-gray: #FEFBF6;
  --gray: #b8b8b8;
  --box-shadow-color: rgba(18, 18, 18, .5);
}

main {
  position: fixed; top: 0; left: 0;
  width: 100%; height: 100%;
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
  height: 97vh;
  padding: 1rem;
}

.container {
  margin-top: 5rem;
  padding: 1rem;
  display: flex; justify-content: center;
  transition: 100ms linear;
}

.profile {
  top: 0; left: 0;
}

.toggleButton {
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
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  gap: 0.5rem; padding: 1rem;
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
