import api from './api.js'

export async function login(email, senha) {
  const resposta = await api.post('/auth/login/', { email, senha })
  return resposta.data
}

export async function register(nome, email, senha) {
  const resposta = await api.post('/usuarios/', { nome, email, senha })
  return resposta.data
}

export function logout() {
  localStorage.removeItem('access_token')
}
