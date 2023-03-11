<template>
    <div class="d-flex">
        <v-toolbar>
            <v-toolbar-title>
                <div class="d-flex">
                    <v-btn :active="false" variant="text" :to="{name: 'home'}">Hisway African Grocery Store</v-btn>
                </div>

            </v-toolbar-title>
            <v-toolbar-items>
                <v-btn variant="text" >
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-login"></v-icon>
                    </div>
                    <span>Login</span>
                </v-btn>
                <v-btn variant="text">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-account-tie"></v-icon>
                    </div>
                    <span>Call Now</span>
                </v-btn>
                <v-btn variant="text">
                    <div class="d-flex mr-1">
                        <v-icon icon="mdi-directions"></v-icon>
                    </div>
                    <span>Get Directions</span>
                </v-btn>
                <v-btn variant="text">
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