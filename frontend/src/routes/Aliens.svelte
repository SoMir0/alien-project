<script>
    const aliens = [
        {
            name: "Lehvicon",
            lastname: "Armadios",
            age: 246,
            planet: "Hermedittiosa"
        },
        {
            name: "Taylona",
            lastname: "Neontran",
            age: 152,
            planet: "Menoetes"
        },
        {
            name: "Yosalazar",
            lastname: "Skyllen",
            age: 26,
            planet: "1989 PO"
        },
        {
            name: "Autotaylor",
            lastname: "Hansenwalker",
            age: 849,
            planet: "Giausar r"
        },
    ];
</script>

<div class="list">
  {#if aliens.length == 0}
    There are no aliens in your local area!
  {:else}
    {#each aliens as alien}
      <div class="alien"><p><em>{alien.name} {alien.lastname}</em> from <b>{alien.planet}</b>, age <mark>{alien.age}</mark>.</p>
      <button>Add friend</button>
      </div>
    {/each}
  {/if}
</div>

<style>
.list {
  background-color: var(--dark-white);
  height: 90vh;
  width: 100vw;
  margin-top: -0.5rem;
  overflow-x: hidden;
  overflow-y: auto;
}

.list::-webkit-scrollbar {
  width: 0.5rem;
}

.list::-webkit-scrollbar-track {
  background: none;
}
 
.list::-webkit-scrollbar-thumb {
  background: var(--purple); 
}

.alien {
  display: flex; flex-direction: row; justify-content: space-around;
  height: 2rem; padding: 1rem;
  width: 100%;
}

.alien b {
  background: var(--light-blue);
  color: var(--dark-white);
}

.alien mark {
  background: var(--purple);
  color: var(--dark-white);
}

.alien button {
  background-color: var(--light-blue);
  outline: none; border: none;
  cursor: pointer;
}

.alien button:hover {
  transform: scale(1.05);
}

.alien:hover {
  background: var(--purple)
}
</style>