<script>
import { ref } from 'vue'
import axios from 'axios'
export default {
    setup() {
    },
    data() {
        return {
            inventory: [],
            inventoryLoaded: false
        }
    },
    methods: {
        formatNumber(num) {
            return parseFloat(num).toFixed(2)
        },
        addQuantity(item) {
            const inventoryIndex = this.inventory.findIndex(function (i) {
                return i.name === item.name;
            });
            item.item_quantity++
            this.inventory.splice(inventoryIndex, 1, item)
        },
        removeQuantity(item) {
            const inventoryIndex = this.inventory.findIndex(function (i) {
                return i.name === item.name;
            });
            item.item_quantity--
            this.inventory.splice(inventoryIndex, 1, item)
        },
        //This would be an item id when the endpoint is created. In the endpoint we then check the quantity to the reorder quantity
        toReorder(item) {
            const fakeReorderQuantity = 5
            return (item.item_quantity < fakeReorderQuantity)
        },
        async getProducts() {
            //Getting products combined with category, vendor, and quantity 
            const productsResponse = await axios.get('http://localhost:5000/products')
            const inventoryResponse = await axios.get('http://localhost:5000/inventory')
            const vendorResponse = await axios.get('http://localhost:5000/vendor')
            let data = productsResponse.data
            let combinedProducts = []
            for (let prod of data) {
                let invIndex = inventoryResponse.data.findIndex(item => prod.product_id === item.product_id);
                let vendorIndex = vendorResponse.data.findIndex(item => prod.vendor_id === item.vendor_id);
                let newProd = { ...prod, ...inventoryResponse.data[invIndex], ...vendorResponse.data[vendorIndex] };
                console.log(newProd)
                combinedProducts.push(newProd)
            }
            this.inventory = combinedProducts
            this.inventoryLoaded = true
        }
    },
    async mounted() {
        await this.getProducts()
    }
}
</script>

<template>
    <div class="d-flex align-self-center mt-3" id="searchDiv">
        <v-text-field prepend-icon="mdi-magnify" variant="underlined" label="Search"></v-text-field>
    </div>
    <div class="d-flex justify-center" v-if="!inventoryLoaded">
        <v-progress-circular indeterminate model-value="20"></v-progress-circular>
    </div>
    <div class="d-flex" v-if="this.inventory.length != 0">
        <v-card max-width="1000px" class="mx-auto">
            <v-container>
                <v-row dense v-for="item in inventory">
                    <v-col cols="12">
                        <v-card elevation="3" min-width="800px" min-height="200px" max-height="400px">
                            <v-row>
                                <v-col>
                                    <v-card-title>
                                        <div class="d-flex">
                                            <h3>
                                                {{ item.product_name }}
                                            </h3>
                                            <div>
                                                <v-icon color="blue" size="x-small" v-if="toReorder(item)">
                                                    mdi-flag
                                                </v-icon>
                                            </div>
                                        </div>
                                    </v-card-title>
                                    <v-card-subtitle>
                                        <span>


                                            {{ item.product_description }}
                                        </span>

                                    </v-card-subtitle>
                                    <v-card-subtitle>
                                        <span>
                                            {{ item.category }}
                                        </span>
                                    </v-card-subtitle>
                                </v-col>
                                <v-col>
                                    <v-card-text>
                                        <div class="d-flex">
                                            <div style="width:250px">

                                                <v-text-field density="compact" variant="underlined" persistent-hint
                                                    hint="Quantity" v-model="item.item_quantity">
                                                    <template v-slot:append>
                                                        <v-btn @click="addQuantity(item)" variant="text">
                                                            <v-icon color="blue">
                                                                mdi-plus
                                                            </v-icon>
                                                        </v-btn>
                                                    </template>
                                                    <template v-slot:prepend>
                                                        <v-btn @click="removeQuantity(item)" variant="text">
                                                            <v-icon color="blue">
                                                                mdi-minus
                                                            </v-icon>
                                                        </v-btn>
                                                    </template>
                                                </v-text-field>
                                            </div>
                                        </div>
                                    </v-card-text>
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col>
                                    <div style="width:250px">

                                        <v-card-text>
                                            <div class="d-flex">
                                                <v-text-field hide-details :label="formatNumber(item.product_price)"
                                                    density="compact" variant="plain">
                                                    <template v-slot:prepend>
                                                        <v-icon color="green-darken-1"> mdi-currency-usd </v-icon>
                                                    </template>


                                                </v-text-field>
                                            </div>
                                        </v-card-text>
                                    </div>
                                </v-col>
                            </v-row>



                            <div class="d-flex">


                                <v-card-text>
                                    <div class="d-flex">
                                        <div class="d-flex mr-20">
                                            <v-icon>
                                                mdi-store
                                            </v-icon>
                                        </div>
                                        <div class="d-flex">
                                            {{ item.vendor_name }}
                                        </div>
                                    </div>
                                </v-card-text>
                                <v-btn variant="text" color="blue" icon="mdi-pencil">

                                </v-btn>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>

    </div>
</template>

<style>
#searchDiv {
    width: 500px
}

#quantityButton {
    min-width: 0;
    padding: 1;
}
</style>