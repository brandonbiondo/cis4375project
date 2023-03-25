<template>
  <v-dialog
      v-model="dialog"
      width="auto"
      v-if="!isLoggedIn"
  >
    <template v-slot:activator="{ props }">
      <v-btn variant="text" v-bind="props" >
        <div class="d-flex mr-1">
          <v-icon icon="mdi-login"></v-icon>
        </div>
        <span >Login</span>
      </v-btn>
    </template>
    <v-sheet width="600" class="mx-auto">
      <v-form class="d-flex pa-2">
        <v-container class="fluid">
          <v-text-field
              v-model="username"
              label="Username"
          ></v-text-field>
          <v-text-field
              v-model="password"
              label="Password"
              persistent-hint
              :type="'password'"
          ></v-text-field>

          <v-btn
              class="justify-right align-right"
              color="blue"
              @click="onSubmit()"
          >
            Login
          </v-btn>
          <span class="font-weight-bold pl-2" v-if="loginSuccess != null && loginSuccess === false">Login Failed</span>
        </v-container>

      </v-form>
    </v-sheet>
  </v-dialog>
  <v-btn variant="text" @click="onSubmit" v-else>
    <div class="d-flex mr-1">
      <v-icon icon="mdi-logout"> </v-icon>
    </div>
    <span> Logout</span>
  </v-btn>

</template>
<script>
import {useLoginStore} from "../stores/login";

export default {
  name: 'Login',
  setup() {


  },
  data() {
    return {
      username: "",
      password: "",
      dialog: false,
      loggedIn: false,
      loginSuccess: null,
    }
  },
  methods: {
     async onSubmit() {

       const loginStore = useLoginStore();
       if (this.isLoggedIn) {
          await loginStore.logout()
         this.dialog = false;
       } else {
         const loginSuccess = await loginStore.login(this.username, this.password);
         if (!loginSuccess) {
           this.loginSuccess = false;
         } else {
           this.loginSuccess = true;
           this.dialog = false;
         }

       }


    },
  },
  computed: {
    isLoggedIn() {
      const loginStore = useLoginStore();
      return this.loggedIn = loginStore.isLoggedIn()
    }
  },
}


</script>