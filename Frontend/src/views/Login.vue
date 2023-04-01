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
          <v-progress-circular v-if="loading" indeterminate model-value="20" class="ml-5"></v-progress-circular>
          <span class="font-weight-bold pl-2" v-if="loginSuccess != null && loginSuccess === false">Login Failed</span>
        </v-container>

      </v-form>
    </v-sheet>
  </v-dialog>
  <v-menu open-on-hover v-else>
    <template v-slot:activator="{ props }">
      <v-btn variant="text" v-bind="props">
        <div class="d-flex mr-1">
          <v-icon icon="mdi-account-check"> </v-icon>
        </div>
        <span> Account </span>

      </v-btn>
    </template>
    <v-card>

    <v-card-item>
    <v-btn variant="text" @click="onSubmit">
      <div class="d-flex mr-1">
        <v-icon icon="mdi-logout"> </v-icon>
      </div>
      <span> Logout</span>

    </v-btn>
    </v-card-item>
      <v-card-item>
        <v-dialog
            v-model="editDialog"
            width="auto"
        >
          <template v-slot:activator="{ props }">
            <v-btn variant="text" v-bind="props">
              <div class="d-flex mr-1">
                <v-icon icon="mdi-account-plus"> </v-icon>
              </div>
              <span> Change Username/Password </span>

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
                    @click="updateLogin()"
                >
                  Update
                </v-btn>
              </v-container>

            </v-form>
          </v-sheet>
        </v-dialog>


      </v-card-item>
    </v-card>

  </v-menu>
</template>
<script>
import {useLoginStore} from "../stores/login";
import axios from "axios";

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
      loading: false,
      editDialog: false,
    }
  },
  methods: {
     async onSubmit() {

       const loginStore = useLoginStore();
       if (this.isLoggedIn) {
          await loginStore.logout()
         this.dialog = false;
       } else {
         this.loading = true;
         const loginSuccess = await loginStore.login(this.username, this.password);
         this.username = "";
         this.password = "";
         this.loading = false;
         if (!loginSuccess) {
           this.loginSuccess = false;
         } else {
           this.loginSuccess = true;
           this.dialog = false;
         }

       }


    },
    async updateLogin() {
       const loginStore = useLoginStore();
       await axios.put("http://localhost:5000/login", {"login_username": this.username, "login_password": this.password, "employee_id": loginStore.user.employee_id})
      this.username = "";
       this.password = "";
      this.editDialog = false;
    }
  },
  computed: {
    isLoggedIn() {
      const loginStore = useLoginStore();
      return this.loggedIn = loginStore.isLoggedIn()
    }
  },
}


</script>