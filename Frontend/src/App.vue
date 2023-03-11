<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Header from './components/Header.vue';
</script>

<template>
  <header>
    <Header/>
  </header>
  <v-app id=”app”>
    <router-view />
  </v-app>
</template>

