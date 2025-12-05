<template>
  <div class="register">
    <h2>Criar Conta</h2>
    <form @submit.prevent="registrar">
      <div class="grupo">
        <label for="nome">Nome</label>
        <input id="nome" v-model.trim="nome" type="text" placeholder="Seu nome" required />
      </div>
      <div class="grupo">
        <label for="email">Email</label>
        <input id="email" v-model.trim="email" type="email" placeholder="seu@email.com" required />
      </div>
      <div class="grupo">
        <label for="senha">Senha</label>
        <input id="senha" v-model.trim="senha" type="password" placeholder="••••••" required />
      </div>
      <button type="submit" class="criar" :disabled="carregando">{{ carregando ? 'Criando...' : 'Criar Conta' }}</button>
      <p v-if="erro" class="erro">{{ erro }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { register, login } from '../services/authService.js'

const emit = defineEmits(['registrado'])

const nome = ref('')
const email = ref('')
const senha = ref('')
const carregando = ref(false)
const erro = ref(null)

async function registrar() {
  if (!nome.value || !email.value || !senha.value) return
  carregando.value = true
  erro.value = null
  try {
    await register(nome.value, email.value, senha.value)
    const dados = await login(email.value, senha.value)
    localStorage.setItem('access_token', dados.access_token)
    emit('registrado', dados.user)
  } catch (e) {
    erro.value = e?.response?.data?.error || 'Falha ao registrar'
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.register {
  max-width: 420px;
  margin: 0 auto 2rem;
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 12px;
  background: #fff;
}
.grupo { display: flex; flex-direction: column; margin-bottom: 12px; }
label { font-weight: 600; margin-bottom: 4px; }
input { border: 1px solid #d1d5db; border-radius: 8px; padding: 8px 10px; font-size: 15px; }
.criar { background: #10b981; color: #fff; border: none; padding: 10px 14px; border-radius: 8px; font-weight: 600; cursor: pointer; }
.erro { margin-top: 10px; color: #c62828; }
</style>
