<template>
  <div id="registration-form">
    <h1>{{ isRegister ? 'Регистрация' : 'Вход' }}</h1>
    <form @submit.prevent="isRegister ? register() : login()">
      <label v-if="isRegister" for="email">Email:</label>
      <input v-if="isRegister" v-model.trim="email" type="email" id="email" required>

      <label for="username">Имя пользователя:</label>
      <input v-model.trim="username" type="text" id="username" required>

      <label for="password">Пароль:</label>
      <input v-model.trim="password" type="password" id="password" required>

      <button type="submit">{{ isRegister ? 'Зарегистрироваться' : 'Войти' }}</button>
    </form>
    <button @click="toggleForm">{{ isRegister ? 'Уже есть аккаунт? Войти' : 'Нет аккаунта? Зарегистрироваться' }}</button>
  </div>
</template>

<script>
import { useVuelidate } from '@vuelidate/core';
import { required, minLength, email } from '@vuelidate/validation';

export default {
  setup() {
    const state = useVuelidate({
      email: { required, email },
      username: { required, minLength: minLength(3) },
      password: { required, minLength: minLength(6) },
    });

    const register = () => {
      if (state.$pending) return;
      // Ваша логика обработки регистрации
    };

    const login = () => {
      if (state.$pending) return;
      // Ваша логика обработки входа
    };

    return { state, register, login };
  },
  data() {
    return {
      isRegister: true,
      email: '',
      username: '',
      password: '',
    };
  },
  methods: {
    toggleForm() {
      this.isRegister = !this.isRegister;
    },
  },
};
</script>

<style scoped>
#registration-form {
  font-family: 'Arial', sans-serif;
  text-align: center;
  margin-top: 60px;
}

form {
  display: flex;
  flex-direction: column;
  width: 300px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  background-color: #f8f9fa;
}

label {
  margin-top: 10px;
  font-size: 16px;
  font-weight: bold;
}

input {
  margin-bottom: 10px;
  padding: 10px;
  border: 1px solid #ced4da;
  border-radius: 5px;
}

button {
  background-color: #007bff;
  color: #fff;
  padding: 12px;
  cursor: pointer;
  border: none;
  border-radius: 5px;
}
</style>
