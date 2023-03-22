<script>
import { ref } from 'vue'
import axios from 'axios'
export default {
    setup() {
    },
    data() {
        return {
            inventory: [],
            products: [],
            stores: [],
            vendors: [],
            categories: [],
            inventoryLoaded: false,
            dialog: false,
            newDialog: false,
            newForm : {
                product_name: "",
                item_name: "",
                product_description: "",
                product_category: "",
                vendor_name: "",
                store_name: "",
                item_quantity: 1,
                product_price: 1,
                inventory_value: 1,
                store_id: 0,
                vendor_id: 0,
                product_id: 0,
            }
        }
    },
    methods: {
        formatNumber(num) {
            return parseFloat(num).toFixed(2)
        },
        updateQuantity(item) {
            axios.put('http://localhost:5000/inventory', item, { params: { "inventory_id": item.inventory_id } })
        },
        async addQuantity(item) {
            console.log(this.inventory)
            const inventoryIndex = this.inventory.findIndex(function (i) {
                return i.name === item.name;
            });
            console.log(inventoryIndex)
            item.item_quantity++
            await axios.put('http://localhost:5000/inventory', item, { params: { "inventory_id": item.inventory_id } })
        },
        async removeQuantity(item) {
            const inventoryIndex = this.inventory.findIndex(function (i) {
                return i.name === item.name;
            });
            item.item_quantity--
            await axios.put('http://localhost:5000/inventory', item, { params: { "inventory_id": item.inventory_id } })
        },
        updateInventory(item) {
            const inventoryIndex = this.inventory.findIndex(function (i) {
                return i.name === item.name;
            });
            console.log(inventoryIndex)
            console.log("hello")
            axios.put('http://localhost:5000/inventory', item, { params: { "inventory_id": item.inventory_id } })
            axios.put('http://localhost:5000/products', item, { params: { "product_id": item.product_id } })
        },
        async createInventory() {
            const storeResponse = this.stores.find(item => this.newForm.product_store === item.store_name);
            const vendorResponse = this.vendors.find(item => this.newForm.product_vendor === item.vendor_name);
            this.newForm.store_id = storeResponse.store_id
            this.newForm.vendor_id = vendorResponse.vendor_id
            this.newForm.item_name = this.newForm.product_name
            this.newForm.store_name = storeResponse.store_name
            this.newForm.vendor_name = vendorResponse.vendor_name
            await axios.post('http://localhost:5000/products', this.newForm)
            const productsResponse = await axios.get('http://localhost:5000/products')
            //resetting the current product data
            const newProducts = productsResponse.data
            console.log(newProducts)
            //getting id of the just inserted data
            const foundObject = newProducts.find(item => this.newForm.product_name === item.product_name);
            this.newForm.product_id = foundObject.product_id
            axios.post('http://localhost:5000/inventory', this.newForm)
            this.inventory.push(this.newForm)
            this.newForm =  {
                product_name: "",
                item_name: "",
                product_description: "",
                product_category: "",
                product_store: null,
                product_vendor: null,
                product_quantity: 1,
                product_price: 1,
                inventory_value: 1,
                store_id: 0,
                vendor_id: 0,
                product_id: 0,
            }
        },
        toReorder(item) {
            const fakeReorderQuantity = 5
            return (item.item_quantity < fakeReorderQuantity)
        },
        async getProducts() {
            //Getting products combined with category, vendor, and quantity 
            const productsResponse = await axios.get('http://localhost:5000/products')
            const inventoryResponse = await axios.get('http://localhost:5000/inventory')
            const vendorResponse = await axios.get('http://localhost:5000/vendor')
            const categoryResponse = await axios.get('http://localhost:5000/category')
            const storeResponse = await axios.get('http://localhost:5000/store')
            let data = productsResponse.data
            let combinedProducts = []
            for (let prod of data) {
                let invIndex = inventoryResponse.data.findIndex(item => prod.product_id === item.product_id);
                let vendorIndex = vendorResponse.data.findIndex(item => prod.vendor_id === item.vendor_id);
                let categoryIndex = categoryResponse.data.findIndex(item => prod.product_id === item.product_id);
                if (invIndex == -1 || vendorIndex == -1) {
                    console.log("Not showing product because a matching inventory and/or vendor could not be found")
                    continue
                }
                let storeIndex = storeResponse.data.findIndex(item => inventoryResponse.data[invIndex].store_id === item.store_id);
                let newProd = { ...prod, ...inventoryResponse.data[invIndex], ...vendorResponse.data[vendorIndex], ...categoryResponse.data[categoryIndex], ...storeResponse.data[storeIndex] };
                combinedProducts.push(newProd)
            }
            this.inventory = combinedProducts
            this.stores = storeResponse.dataS
            this.vendors = vendorResponse.data
            this.products = productsResponse.data
            this.categories = categoryResponse.data
            this.inventoryLoaded = true
        },
    },
    async created() {
        await this.getProducts()
    }
}
</script>fF

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
                                            {{ item.category_name }}
                                        </span>
                                    </v-card-subtitle>
                                </v-col>
                                <v-col>
                                    <v-card-text>
                                        <div class="d-flex">
                                            <div style="width:250px">

                                                <v-text-field density="compact" variant="underlined" persistent-hint
                                                    hint="Quantity" v-model="item.item_quantity"
                                                    @change="updateQuantity(item)">
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
                                <v-dialog v-model="dialog" persistent width="1024">
                                    <template v-slot:activator="{ props }">
                                        <v-btn variant="text" color="blue" icon="mdi-pencil" v-bind="props">
                                        </v-btn>
                                    </template>
                                    <v-card>
                                        <v-card-title>
                                            <span class="text-h5">Edit Product</span>
                                        </v-card-title>
                                        <v-card-text>
                                            <v-container>
                                                <v-row>
                                                    <v-col cols="12" sm="6" md="4">
                                                        <v-text-field persistent-hint hint="Product Name"
                                                            v-model="item.product_name" required></v-text-field>
                                                    </v-col>
                                                    <v-col cols="12" sm="6" md="4">
                                                        <v-text-field v-model="item.product_description" persistent-hint
                                                            hint="Product Desciprtion"></v-text-field>
                                                    </v-col>
                                                    <v-col cols="12" sm="6" md="4">
                                                        <v-text-field v-model="item.category_name" hint="Item Category"
                                                            persistent-hint></v-text-field>
                                                    </v-col>
                                                    <v-col cols="12" sm="6">
                                                        <v-autocomplete :items="this.stores" item-title="store_name"
                                                            v-model="item.store_name" hint="Store" persistent-hint multiple>
                                                        </v-autocomplete>
                                                    </v-col>
                                                    <v-col cols="12" sm="6">
                                                        <v-autocomplete v-model="item.vendor_name" :items="this.vendors"
                                                            item-title="vendor_name" hint="Vendor" persistent-hint
                                                            multiple></v-autocomplete>
                                                    </v-col>
                                                </v-row>
                                            </v-container>
                                        </v-card-text>
                                        <v-card-actions>
                                            <v-spacer></v-spacer>
                                            <v-btn color="blue-darken-1" variant="text" @click="(dialog = false)">
                                                Close
                                            </v-btn>
                                            <v-btn color="blue-darken-1" variant="text"
                                                @click="(dialog = false), updateInventory(item)">
                                                Save
                                            </v-btn>
                                        </v-card-actions>
                                    </v-card>
                                </v-dialog>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
            <v-dialog v-model="newDialog" persistent width="1024">
                <template v-slot:activator="{ props }">
                    <div class="d-flex justify-center align-center">
                        <v-btn icon="mdi-plus-circle-outline" color="blue" variant="text" v-bind="props"> </v-btn>
                    </div>
                </template>
                <v-card>
                    <v-card-title>
                        <span class="text-h5">Create Product</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12" sm="6" md="4">
                                    <v-text-field persistent-hint v-model="this.newForm.product_name" hint="Product Name"
                                        required></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                    <v-text-field persistent-hint v-model="this.newForm.product_description"
                                        hint="Product Desciprtion"></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                    <v-autocomplete hint="Item Category" item-title="category_name" :items="this.categories" v-model="this.newForm.product_category"
                                        persistent-hint> </v-autocomplete>
                                </v-col>
                                <v-col cols="12" sm="6">
                                    <v-autocomplete :items="this.stores" item-title="store_name" v-model="this.newForm.product_store"
                                        hint="Store" persistent-hint> </v-autocomplete>
                                </v-col>
                                <v-col cols="12" sm="6">
                                    <v-autocomplete  :items="this.vendors"
                                        item-title="vendor_name" hint="Vendor" persistent-hint v-model="this.newForm.product_vendor"></v-autocomplete>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="(newDialog = false)">
                            Close
                        </v-btn>
                        <v-btn color="blue-darken-1" variant="text" @click="createInventory(),(newDialog = false)">
                            Save
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>

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