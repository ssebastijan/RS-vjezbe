<script setup>
import { ref, computed, onMounted } from 'vue'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const menu = ref([])
const error = ref('')
const loading = ref(true)
const saving = ref(false)
const name = ref('')
const price = ref('')

const total = computed(() => menu.value.length)

async function loadMenu() {
  loading.value = true
  error.value = ''
  try {
    const res = await fetch(`${API_URL}/jelovnik`)
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    menu.value = await res.json()
  } catch (e) {
    error.value = `Ne mogu učitati jelovnik (${e.message})`
  } finally {
    loading.value = false
  }
}

async function addItem() {
  saving.value = true
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
    error.value = `Ne mogu dodati stavku (${e.message})`
  } finally {
    saving.value = false
  }
}

onMounted(loadMenu)
</script>

<template>
  <div class="page">
    <header class="hero">
      <span class="badge">Raspodijeljeni sustavi · Vježba 1</span>
      <h1>Jelovnik</h1>
      <p>Stavke se dohvaćaju s backenda preko HTTP-a i prikazuju uživo.</p>
    </header>

    <main class="content">
      <section class="card">
        <div class="card-head">
          <h2>Stavke <span v-if="!loading && !error" class="count">{{ total }}</span></h2>
          <button class="ghost" :disabled="loading" @click="loadMenu">Osvježi</button>
        </div>

        <ul v-if="loading" class="list">
          <li v-for="n in 3" :key="n" class="row skeleton"><span></span><span></span></li>
        </ul>

        <div v-else-if="error" class="alert" role="alert">
          <span>{{ error }}</span>
          <button class="ghost" @click="loadMenu">Pokušaj ponovo</button>
        </div>

        <p v-else-if="!menu.length" class="empty">Jelovnik je prazan.</p>

        <ul v-else class="list">
          <li v-for="item in menu" :key="item.id" class="row">
            <span class="item-name">{{ item.name }}</span>
            <span class="price">{{ item.price.toFixed(2) }} €</span>
          </li>
        </ul>
      </section>

      <section class="card">
        <h2>Dodaj stavku</h2>
        <form class="form" @submit.prevent="addItem">
          <label>
            Naziv
            <input v-model="name" placeholder="npr. Palačinke" required />
          </label>
          <label>
            Cijena (€)
            <input v-model="price" type="number" step="0.01" min="0" placeholder="0.00" required />
          </label>
          <button type="submit" class="primary" :disabled="saving">
            {{ saving ? 'Spremam...' : 'Dodaj' }}
          </button>
        </form>
      </section>
    </main>
  </div>
</template>
