<template>
    <div class="d-flex">
        <v-toolbar>
            <v-toolbar-title>
                <div class="d-flex">
                    <v-btn :active="false" variant="text" :to="{name: 'home'}">Hisway African Grocery Store</v-btn>
                </div>

            </v-toolbar-title>
            <v-toolbar-items>
              <Login/>
              <v-btn variant="text" v-if="isLoggedIn" :to="{name: 'inventory'}">
                <div class="d-flex mr-1">
                  <v-icon icon="mdi-view-list"></v-icon>
                </div>
                <span>Inventory</span>
              </v-btn >
              <v-btn variant="text" v-if="isLoggedIn">
                <div class="d-flex mr-1">
                  <v-icon icon="mdi-account-tie"></v-icon>
                </div>
                <span>Employees</span>
              </v-btn >
              <v-btn v-if="isLoggedIn">
                <div class="d-flex mr-1">
                  <v-icon icon="mdi-cart"></v-icon>
                </div>
                <span>Vendors</span>
              </v-btn>

                <v-btn variant="text" href="tel:+1-832-542-2551">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-phone"></v-icon>
                    </div>
                    <span>Call Now</span>
                </v-btn>
                <v-btn variant="text" href="https://www.google.com/maps/dir//Hisway+African+Grocery+Store/data=!4m8!4m7!1m0!1m5!1m1!1s0x864127667b37dced:0x1e7bc43b53716dd1!2m2!1d-95.7781103!2d29.822653499999998">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-directions"></v-icon>
                    </div>
                    <span>Get Directions</span>
                </v-btn>
                <v-btn variant="text" href="https://www.google.com/search?q=Hisway+African+Grocery+Store&ludocid=2196565002355305937&source=sh/x/localposts&lsig=AB86z5UuY2ZQapFTf79I9WXM4AOd#lrd=0x864127667b37dced:0x1e7bc43b53716dd1,1,,,,">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-star"></v-icon>
                    </div>
                    <span>Customer Reviews</span>
                </v-btn>
            </v-toolbar-items>


        </v-toolbar>
    </div>
</template>

<style>
</style>
<script>
import Login from "@/views/Login.vue";
import {useLoginStore} from "../stores/login";

export default {
    components: {
        Login
    },
        data() {
            return {
                dialog: false,
            }
        },
        computed: {
          isLoggedIn() {
            const loginStore = useLoginStore()
            return loginStore.isLoggedIn()
          }
        }
    }
</script>