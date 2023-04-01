<template>
  <div>
    <v-row>
      <v-col>

        <div class="d-flex align-self-center mt-3 justify-center" id="searchDiv">
          <v-text-field v-model="search" prepend-icon="mdi-magnify" variant="underlined" label="Search"></v-text-field>
        </div>
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
        <tr v-for="(vendor, index) in filteredVendors" :key="index">
          <td>{{ vendor.vendor_name }}</td>
          <td>{{ vendor.vendor_phone }}</td>
          <td>
            <v-icon small class="mr-2" @click="openEditDialog(index)">mdi-pencil</v-icon>
            <v-icon small class="mr-2" @click="deleteVendor(index)">mdi-delete</v-icon>
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
    <v-dialog v-model="editDialog" max-width="600px">
      <v-card>
        <v-card-title>Edit Vendor</v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-text-field v-model=this.vendors[editId].vendor_name label="Vendor Name"></v-text-field>
              <v-text-field v-model="this.vendors[editId].vendor_phone" label="Vendor Phone"></v-text-field>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="editDialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="editVendor(this.vendors[editId])">Save</v-btn>
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
      vendors: [],
      dialog: false,
      editDialog: false,
      search: "",
      newVendor: {
        vendor_name: "",
        vendor_phone: "",
      },
      editId: null,
    };
  },
  methods: {
    openEditDialog(index) {
      this.editDialog = true;
      this.editId = this.vendors.findIndex(x => x.vendor_name === this.filteredVendors[index].vendor_name)
    },
    editVendor(item) {
      this.vendors.splice(this.editId, 1, item)
      axios.put("http://localhost:5000/vendor", item, {params: {"vendor_id" :item.vendor_id}})
      this.editDialog = false;
    },
    deleteVendor(index) {
      this.editId = this.vendors.findIndex(x => x.vendor_name === this.filteredVendors[index].vendor_name)
      axios.delete("http://localhost:5000/vendor", {params: {"vendor_id": this.vendors[this.editId].vendor_id}})
      this.vendors.splice(this.editId, 1);
    },
    async saveNewVendor() {
      this.dialog = false;
      const response = await axios.post("http://localhost:5000/vendor", this.newVendor)
      this.vendors.push(response.data);
      this.newVendor = {
        vendor_name: "",
        vendor_phone: "",
      };
    },
  },
  computed: {
    filteredVendors() {
      return this.vendors.filter(p => {
        return p.vendor_name.toLowerCase().indexOf(this.search.toLowerCase()) != -1;
      })},
  },
  async mounted() {
const vendorData = await axios.get('http://localhost:5000/vendor');
this.vendors = vendorData.data;
},
};
</script>

