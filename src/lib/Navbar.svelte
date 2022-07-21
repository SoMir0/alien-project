<script>
import { Router, link, Route } from "svelte-routing";

import Games from '../routes/Games.svelte';
import Aliens from '../routes/Aliens.svelte';
import Explore from '../routes/Explore.svelte';

function getProps() {
  return { class: 'navlink' }
}

export let url = '';
</script>

<Router url="{url}">
  <nav class="navigation">
    <a href="/" class="navlink" use:link>Home</a>
    <a href="/aliens" class="navlink" use:link>Aliens</a>
    <a href="/explore" class="navlink" use:link>Explore</a>
  </nav>
  <div>
    <Route path="/"><Games /></Route>
    <Route path="aliens" component="{Aliens}" />
    <Route path="explore" component="{Explore}" />
  </div>
</Router>

<style>
    .navigation {
        background-color: var(--dark-white);
        height: 5rem;
        width: 100%;
        display: flex; flex-direction: row; justify-content: center; align-items: center;
        gap: 0.5rem;
        position: absolute;
        top: 0;
    }

    .navlink {
        text-decoration: none;
        background-color: var(--white);
        font-weight: bold;
        color: var(--dark-gray);
        padding: 1rem 2rem;
    }
</style>
