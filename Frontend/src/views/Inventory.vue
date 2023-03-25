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
            editDialog: false,
            newDialog: false,
            editId: null,
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
                reorder_id: 0,
                reorder_level: "",
                reorder_time_in_days: "",
                qunatity_in_reorder: "",
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
        async updateCurrency(index) {
            const item = this.inventory[index]
            await axios.put('http://localhost:5000/products', item, { params: { "product_id": item.product_id } })
        },
        async addQuantity(item) {
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
        async deleteInventory(index) {
            const item = this.inventory[index]
            await axios.delete("http://localhost:5000/category", {params: {"category_id": item.category_id}})
            await axios.delete("http://localhost:5000/reorder", {params: {"reorder_id": item.reorder_id}})
            await axios.delete("http://localhost:5000/inventory", {params: {"inventory_id": item.inventory_id}})
            await axios.delete("http://localhost:5000/products", {params: {"product_id": item.product_id}})
            this.inventory.splice(index, 1)
        },
        updateInventoryDialog(id){
          this.editDialog = true;
          this.editId = id;
        },
        async updateInventory(item) {
            const store_id = this.stores.find(i => item.store_name === i.store_name).store_id;
            const vendor_id = this.vendors.find(i => item.vendor_name === i.vendor_name).vendor_id;
            item.vendor_id = vendor_id
            item.store_id = store_id
            item.category_id = category_id
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
            const newProduct = await axios.post('http://localhost:5000/products', this.newForm)
            this.newForm.product_id = newProduct.data.product_id
            const newInventory = await axios.post('http://localhost:5000/inventory', this.newForm)
            const newCategory = await axios.post('http://localhost:5000/category', {"category_name": this.newForm.product_category, "product_id": newProduct.data.product_id})
            const newReorder = await axios.post('http://localhost:5000/reorder', {"reorder_level": this.newForm.reorder_level, "reorder_time_in_days": this.newForm.reorder_time_in_days,
                "quantity_in_reorder": this.newForm.item_quantity, "product_id": newProduct.data.product_id, "inventory_id": newInventory.data.inventory_id})
            const newCombinedProduct = {...newProduct.data, ...newInventory.data, ...newCategory.data, ...newReorder.data}
            newCombinedProduct.store_name = this.newForm.store_name
            newCombinedProduct.vendor_name = this.newForm.vendor_name
            this.inventory.push(newCombinedProduct)
            this.newForm =  {
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
                reorder_id: 0,
                reorder_level: "",
                reorder_time_in_days: "",
                qunatity_in_reorder: "",
            }
        },
        async getProducts() {
            const vendorResponse = await axios.get('http://localhost:5000/vendor')
            const categoryResponse = await axios.get('http://localhost:5000/category')
            const storeResponse = await axios.get('http://localhost:5000/store')
            const productsResponse = await axios.get('http://localhost:5000/combined_products')
            this.inventory = productsResponse.data
            this.inventoryLoaded = true
            this.stores = storeResponse.data
            this.vendors = vendorResponse.data
            this.categories = categoryResponse.data
        },
    },
    async created() {
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
                <v-row dense v-for="(item, index) in inventory">
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
                                                <v-icon color="blue" size="x-small" v-if="item.item_quantity < item.reorder_level">
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
                                                <v-text-field hide-details
                                                    density="compact" variant="plain" v-model="item.product_price" @keydown.enter.prevent="updateCurrency(index)">
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
                                                mdi-cart
                                            </v-icon>
                                        </div>
                                        <div class="d-flex">
                                            {{ item.vendor_name }}
                                        </div>
                                    </div>
                                </v-card-text>
                                <v-card-text>
                                    <div class="d-flex">
                                        <div class="d-flex mr-20">
                                            <v-icon>
                                                mdi-store
                                            </v-icon>
                                        </div>
                                        <div class="d-flex">
                                            {{ item.store_name }}
                                        </div>
                                    </div>
                                </v-card-text>
                                <v-btn variant="text" color="blue" icon="mdi-pencil" @click="updateInventoryDialog(index)">
                                </v-btn>
                                <v-btn variant="text" color="red" icon="mdi-delete-outline" @click="deleteInventory(index)">
                                </v-btn>
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
            <v-dialog v-model="editDialog" persistent width="1024">
                <v-card>
                    <v-card-title>
                        <span class="text-h5">Edit Product</span>
                    </v-card-title>
                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12" sm="6" md="4">
                                    <v-text-field persistent-hint v-model="this.inventory[editId].product_name" hint="Product Name"
                                                  required></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6" md="4">
                                    <v-text-field persistent-hint v-model="this.inventory[editId].product_description"
                                                  hint="Product Desciprtion"></v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6">
                                    <v-autocomplete :items="this.stores" item-title="store_name" v-model="this.inventory[editId].store_name"
                                                    hint="Store" persistent-hint> </v-autocomplete>
                                </v-col>
                                <v-col cols="12" sm="6">
                                    <v-autocomplete  :items="this.vendors"
                                                     item-title="vendor_name" hint="Vendor" persistent-hint v-model="this.inventory[editId].vendor_name"></v-autocomplete>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn color="blue-darken-1" variant="text" @click="(editDialog = false)">
                            Close
                        </v-btn>
                        <v-btn color="blue-darken-1" variant="text" @click="updateInventory(this.inventory[editId]),(editDialog = false)">
                            Save
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-dialog v-model="newDialog" persistent width="1024">
                <template v-slot:activator="{ props }">
                    <div class="d-flex justify-center align-center">
                        <v-btn icon="mdi-plus-circle-outline" color="blue" variant="text" @click="newDialog=true"> </v-btn>
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
                                    <v-text-field hint="Item Category" item-title="category_name" v-model="this.newForm.product_category"
                                        persistent-hint> </v-text-field>
                                </v-col>
                                <v-col cols="12" sm="6">
                                    <v-autocomplete :items="this.stores" item-title="store_name" v-model="this.newForm.product_store"
                                        hint="Store" persistent-hint> </v-autocomplete>
                                </v-col>
                                <v-col cols="12" sm="6">
                                    <v-autocomplete  :items="this.vendors"
                                        item-title="vendor_name" hint="Vendor" persistent-hint v-model="this.newForm.product_vendor"></v-autocomplete>
                                </v-col>
                                <v-col cols="12" sm="2" md="4">
                                    <v-text-field hint="Reorder Level" item-title="category_name" v-model="this.newForm.reorder_level"
                                                  persistent-hint> </v-text-field>
                                </v-col>
                                <v-col cols="12" sm="2" md="4">
                                    <v-text-field hint="Reorder Time" item-title="category_name" v-model="this.newForm.reorder_time_in_days"
                                                  persistent-hint> </v-text-field>
                                </v-col>
                                <v-col cols="12" sm="2" md="4">
                                    <v-text-field hint="Quantity in Reorder" item-title="category_name" v-model="this.newForm.qunatity_in_reorder"
                                                  persistent-hint> </v-text-field>
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