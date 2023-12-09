<template>
  <div id="app">
    <h1>Регистрация</h1>
    <form @submit.prevent="register">
      <label for="username">Имя пользователя:</label>
      <input v-model="username" type="text" id="username" required>

      <label for="password">Пароль:</label>
      <input v-model="password" type="password" id="password" required>

      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async register() {
      try {
        const response = await fetch('http://localhost:5000/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            firstName: this.username,  // Исправлено на firstName
            password: this.password,
          }),
        });

        const data = await response.json();
        console.log(data);

        // Здесь вы можете добавить переход на страницу входа или другие действия
      } catch (error) {
        console.error('Ошибка при регистрации:', error);
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

form {
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: 0 auto;
}

label {
  margin-top: 10px;
}

input {
  margin-bottom: 10px;
  padding: 5px;
}

button {
  background-color: #3498db;
  color: #fff;
  padding: 10px;
  cursor: pointer;
}
</style>
