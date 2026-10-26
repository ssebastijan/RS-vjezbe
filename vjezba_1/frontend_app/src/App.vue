<script setup>
import { ref } from 'vue'

const count = ref(0)
const loadedAt = new Date().toLocaleString('hr-HR')
</script>

<template>
  <main>
    <h1>Raspodijeljeni sustavi: vježba 1</h1>
    <p>Vue frontend deployan na Render.com kao Static Site.</p>
    <p>Stranica učitana: {{ loadedAt }}</p>
    <button @click="count++">Klikova: {{ count }}</button>
  </main>
</template>
