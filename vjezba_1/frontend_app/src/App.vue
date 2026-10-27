<script setup>
import { ref, onMounted } from 'vue'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const menu = ref([])
const error = ref('')
const loading = ref(true)
const name = ref('')
const price = ref('')

async function loadMenu() {
  loading.value = true
  error.value = ''
  try {
    const res = await fetch(`${API_URL}/jelovnik`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    menu.value = await res.json()
  } catch (e) {
    error.value = `Could not load menu: ${e.message}`
  } finally {
    loading.value = false
  }
}

async function addItem() {
  error.value = ''
  try {
    const res = await fetch(`${API_URL}/jelovnik`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name.value, price: Number(price.value) }),
    })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    name.value = ''
    price.value = ''
    await loadMenu()
  } catch (e) {
    error.value = `Could not add item: ${e.message}`
  }
}

onMounted(loadMenu)
</script>

<template>
  <main>
    <h1>Raspodijeljeni sustavi: vježba 1</h1>

    <h2>Jelovnik</h2>
    <p v-if="loading">Učitavanje...</p>
    <p v-if="error" class="error">{{ error }}</p>
    <ul>
      <li v-for="item in menu" :key="item.id">{{ item.name }}: {{ item.price.toFixed(2) }} €</li>
    </ul>

    <form @submit.prevent="addItem">
      <input v-model="name" placeholder="Naziv" required />
      <input v-model="price" type="number" step="0.01" min="0" placeholder="Cijena" required />
      <button type="submit">Dodaj</button>
    </form>
  </main>
</template>
