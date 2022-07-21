<h3>Chat</h3>
<div class="messages">
  <article class="message">Hello!</article>
  <article class="message">Hi!</article>
</div>
<textarea class="textinput" placeholder="Type your message..." />

<style>
.messages {
  width: 90%;
  height: 90%;
  display: flex; flex-direction: column; gap: 2rem;
  background-color: #E4DCCF;
  background-size: 53px 53px;
  background-image: radial-gradient(
    transparent 28px,
    #ffffff 28px,
  #ffffff 32px,
    transparent 32px
  );
  background-position: 50% 44%;
}

.messages .message {
  background-color: #c7b8a1;
  width: 30%;
  border-radius: 0.8vmax;
  padding: 0.5rem 1rem;
  height: auto;
}

.messages .message:nth-child(2n) {
  margin-left: 50%;
}

.textinput {
  outline: none; border: none;
  resize: none;
  border-radius: 0.3rem;
  font-size: 1rem;
  width: 80%;
  height: 3rem;
  position: absolute; bottom: 5%;
  transition: 150ms ease-in;
}

.textinput:hover {
  background: #eee;
}
</style>
