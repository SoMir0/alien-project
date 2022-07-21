<script>
export let toggleThemeFunc;
export let currentTheme;
</script>

<img src="https://st.depositphotos.com/1779253/5140/v/450/depositphotos_51405259-stock-illustration-male-avatar-profile-picture-use.jpg" alt="Default profile" class="pic" />
<button class="theme-button" on:click={toggleThemeFunc}>{#if currentTheme}Light{:else}Dark{/if}</button>
<h3>Your Name</h3>
<p>Lorem ipsum dolor sit amet, officia exce reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.</p>
<p class="planet">Planet: <b>HippoNiteniaLibosiRa</b></p>

<style>
.pic {
  width: 8rem; height: 8rem;
  border-radius: 50%;
}

.planet {
  border: 2px var(--light-white) dashed;
  background: var(--light-blue);
  color: var(--light-white);
  padding: 0.3rem;
  transition: transform 200ms ease-in;
}

.planet:hover {
  transform: scale(1.05);
}

.theme-button {
  background: var(--dark-gray); border: none; outline: none;
  color: var(--dark-white);
  text-transform: uppercase;
  font-size: 1rem;
  font-weight: bold;
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  cursor: pointer;
}
</style>
