<template>
  <div>
    <v-row>
      <v-col>
        <v-text-field v-model="search" label="Search" append-icon="mdi-magnify" />
      </v-col>
      <!-- Button to add a new vendor -->
      <v-col>
        <v-btn color="success" @click="dialog = true">Add New Vendor</v-btn>
      </v-col>
    </v-row>
    <h1 style="color: purple;">Vendors</h1>
    <v-table>
      <thead>
        <tr>
          <th>Vendor Name</th>
          <th>Phone</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(vendor, index) in vendors" :key="index">
          <td>{{ vendor.vendor_name }}</td>
          <td>{{ vendor.vendor_phone }}</td>
          <td>
            <v-icon small class="mr-2" @click="editVendor(vendor)">mdi-pencil</v-icon>
            <v-icon small class="mr-2" @click="deleteVendor(vendor)">mdi-delete</v-icon>
          </td>
        </tr>
      </tbody>
    </v-table>

    <!-- Dialog for adding a new vendor -->
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title>Add New Vendor</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-text-field v-model="newVendor.vendor_name" label="Vendor Name"></v-text-field>
              <v-text-field v-model="newVendor.vendor_phone" label="Vendor Phone"></v-text-field>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="saveNewVendor">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      headers: [
        { text: "Vendor Name", value: "vendor_name" },
        { text: "Vendor Phone", value: "vendor_phone" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      vendors: [
        {
          vendor_name: "Bukky Enterprise",
          vendor_phone: "281-552-2582",
        },
        {
         vendor_name: "Bomir Foods",
         vendor_phone:"931-683-7673",  
        },
        {
         vendor_name: "Spicy World", 
         vendor_phone:"832-752-8625",  
        },
        {
         vendor_name: "Fesojaye", 
         vendor_phone:"281-883-7728",  
        },
      ],
      dialog: false,
      newVendor: {
        vendor_name: "",
        vendor_phone: "",
      },
    };
  },
  methods: {
    editVendor(vendor) {
      // ... (existing editVendor logic) ...
    },
    deleteVendor(vendor) {
      // ... (existing deleteVendor logic) ...
    },
    saveNewVendor() {
      this.vendors.push(this.newVendor);
      this.dialog = false;
      this.newVendor = {
        vendor_name: "",
        vendor_phone: "",
      };
    },
  },
  async mounted() {
const vendorData = await axios.get('http://localhost:5000/vendor');
console.log(vendorData.data);
this.vendors = vendorData.data;
},
};
</script>

