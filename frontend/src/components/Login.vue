<template>
  <div class="login">
    <h2>Entrar</h2>
    <form @submit.prevent="entrar">
      <div class="grupo">
        <label for="email">Email</label>
        <input id="email" v-model.trim="email" type="email" placeholder="seu@email.com" required />
      </div>
      <div class="grupo">
        <label for="senha">Senha</label>
        <input id="senha" v-model.trim="senha" type="password" placeholder="••••••" required />
      </div>
      <button type="submit" class="entrar" :disabled="carregando">{{ carregando ? 'Entrando...' : 'Entrar' }}</button>
      <p v-if="erro" class="erro">{{ erro }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { login } from '../services/authService.js'

const emit = defineEmits(['logado'])

const email = ref('')
const senha = ref('')
const carregando = ref(false)
const erro = ref(null)

async function entrar() {
  if (!email.value || !senha.value) return
  carregando.value = true
  erro.value = null
  try {
    const dados = await login(email.value, senha.value)
    localStorage.setItem('access_token', dados.access_token)
    emit('logado', dados.user)
  } catch (e) {
    erro.value = e?.response?.data?.error || 'Falha no login'
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.login {
  max-width: 420px;
  margin: 0 auto 2rem;
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: #fff;
}
.grupo {
  display: flex;
  flex-direction: column;
  margin-bottom: 12px;
}
label {
  font-weight: 600;
  margin-bottom: 4px;
}
input {
  border: 1px solid #d1d5db;
  border-radius: 8px;
  padding: 8px 10px;
  font-size: 15px;
}
.entrar {
  background: #3b82f6;
  color: #fff;
  border: none;
  padding: 10px 14px;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
}
.erro {
  margin-top: 10px;
  color: #c62828;
}
</style>
