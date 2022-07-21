<h3>Chat</h3>
<div class="messages">
  <article class="message">Hello!</article>
  <article class="message">Hi!</article>
</div>
<textarea class="textinput" placeholder="Type your message..." />

<style>
.messages {
  width: 90%;
  height: 100%;
  display: flex; flex-direction: column; gap: 2rem;
  background-color: var(--dark-white);
  background-size: 53px 53px;
  background-image: radial-gradient(
    transparent 28px,
    var(--light-white) 28px,
    var(--light-white) 32px,
    transparent 32px
  );
  background-position: 50% 44%;
}

.messages .message {
  background-color: var(--purple);
  width: 30%;
  border-radius: 0.8vmax;
  padding: 0.5rem 1rem;
  height: auto;
  color: var(--light-white);
}

.messages .message:nth-child(2n) {
  margin-left: 50%;
}

.textinput {
  background: var(--white);
  outline: none; border: none;
  resize: none;
  border-radius: 0.3rem;
  font-size: 1rem;
  width: 80%;
  height: 3rem;
  transition: 150ms ease-in;
}

.textinput::-webkit-input-placeholder {
  color: var(--dark-gray);
}

.textinput:-moz-placeholder { /* Firefox 18- */
  color: var(--dark-gray);
}

.textinput::-moz-placeholder {  /* Firefox 19+ */
  color: var(--dark-gray);
}

.textinput:-ms-input-placeholder {
  color: var(--dark-gray);
}

.textinput::placeholder {
  color: var(--dark-gray);
}

.textinput:hover {
  background: var(--dark-white);
}
</style>
