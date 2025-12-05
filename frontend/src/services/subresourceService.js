import api from './api.js'

export async function getComentario(mensagemId) {
  try {
    const resposta = await api.get(`/mensagens/${mensagemId}/comentarios`)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao carregar comentários.',
      status: 500
    }
  }
}

export async function criarComentario(mensagemId, dados) {
  try {
    const resposta = await api.post(`/mensagens/${mensagemId}/comentarios`, dados)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao criar comentário.',
      status: 500
    }
  }
}

export async function atualizarComentario(mensagemId, id, dados) {
  try {
    const resposta = await api.put(`/mensagens/${mensagemId}/comentarios/${id}`, dados)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao atualizar comentário.',
      status: 500
    }
  }
}

export async function removerComentario(mensagemId, id) {
  try {
    const resposta = await api.delete(`/mensagens/${mensagemId}/comentarios/${id}`)
    return resposta.data
  } catch (erro) {
    throw erro.response?.data || {
      erro: 'NetworkError',
      message: 'Falha ao remover comentário.',
      status: 500
    }
  }
}
