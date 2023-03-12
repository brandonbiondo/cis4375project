<script>
import { ref } from 'vue'

export default {     
  setup() {
  },
  data() {
    return {
        fakeInventory: []
    }
  },
  methods: {
  formatNumber (num) {
    return parseFloat(num).toFixed(2)
  },
  addQuantity (item) {
    const inventoryIndex = this.fakeInventory.findIndex(function (i) {
	return i.name === item.name;
    });
    item.quantity++
    this.fakeInventory.splice(inventoryIndex, 1, item)
  },
  removeQuantity (item) {
    const inventoryIndex = this.fakeInventory.findIndex(function (i) {
	return i.name === item.name;
    });
    item.quantity--
    this.fakeInventory.splice(inventoryIndex, 1, item)
  },
  //This would be an item id when the endpoint is created. In the endpoint we then check the quantity to the reorder quantity
  toReorder(item) {
    const fakeReorderQuantity = 5
    return (item.quantity < fakeReorderQuantity)
  }
},
  mounted() {
    this.fakeInventory.push({"name": "Banana", "category": "Fruit", "vendor": "Vendor1", "description": "A banana", "quantity": 5, "reorder": false, "sku": 34212, "price": 1.42})
    this.fakeInventory.push({"name": "Apple", "category": "Fruit", "vendor": "Vendor2", "quantity": 1, "description": "An apple", "reorder": false, "sku": 12345, "price": 2.00})

  }
}
</script>

<template>
    <div class="d-flex align-self-center ma-10" id="searchDiv">
        <v-text-field prepend-icon="mdi-magnify" variant="underlined" label="Search"></v-text-field>
    </div>
    <div class="d-flex">
    <div class="d-flex ma-4" v-for="item in fakeInventory">
        <v-card elevation="3" min-width="200px" min-height="200px">
            <v-card-title>
                <div class="d-flex">
                <h3>
                {{ item.name }}
               </h3>
               <div>
               <v-icon color="blue" size="x-small" v-if="toReorder(item)">
                        mdi-flag
                </v-icon>
                </div>            
                </div>
            </v-card-title>
            <v-card-subtitle>
                {{ item.description }}
            </v-card-subtitle>
            <v-card-text> 
                <div class="d-flex">
                    <v-text-field  density="compact" variant="underlined" persistent-hint hint="Quantity" v-model="item.quantity">
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
            </v-card-text>
            <v-card-text> 
                <div class="d-flex">
                    <v-text-field  density="compact" variant="underlined">
                        <template v-slot:prepend>        
                            <v-icon color="green-darken-1"> mdi-currency-usd </v-icon> 
                        </template>
                        {{ formatNumber(item.price) }}
                    </v-text-field>  
                </div>
            </v-card-text  >
            <v-card-text> 
                <h4>
                    Category: 
                </h4>
                {{ item.category }} 
            </v-card-text  >
            <v-card-text>
            <div class="d-flex">
                <div class="d-flex mr-20">
                    <v-icon>
                        mdi-store
                    </v-icon>   
                </div>
                <div class="d-flex">
                    {{ item.vendor }}
                </div>
            </div>
        </v-card-text>
        </v-card>
    </div>
    </div>
</template>

<style>
#searchDiv {
    width:500px
    
}
#quantityButton{
    min-width: 0;   
    padding: 1; 
}
</style>