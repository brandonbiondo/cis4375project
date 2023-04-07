import 'vuetify/styles'
import { createApp } from 'vue'
import { createVuetify } from 'vuetify'
import App from './App.vue'
import {router} from './router'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import axios from 'axios'
import { createPinia } from "pinia";



const app = createApp(App)
const vuetify = createVuetify({
    components,
    directives,
  })
app.use(vuetify)
app.use(router)
app.use(mdi)
app.use(createPinia())

app.mount('#app')
